import frappe
import importlib
from eda.doc_event.utility import validater
import ast
from eda.doc_event.consumer_doc import Consumer_log

def schedule_pub(doc,event=None):
    frappe.enqueue("eda.event_handler.consumer_trigger.trigger_consumer",doc=doc,queue="short")

def trigger_consumer(doc):
    update_doc = {
        "error_log":"",
        "status":"Processed"
    }
    con_doc = Consumer_log()
    try:
        json_payload = ast.literal_eval(doc.payload)
        validater(json_payload,["module","function","argument"])
        module_name = json_payload["module"]
        function_name = json_payload["function"]
        function_argument = json_payload["argument"]
        my_module = importlib.import_module(module_name)
        my_function = getattr(my_module, function_name)
        my_function(function_argument)
    except Exception as err:
        update_doc["error_log"] = frappe.get_traceback()
        update_doc["status"] = "Error"
        con_doc.update_status(update_doc,doc.name)


        