import importlib
import frappe
from eda.event_handler.utility import json_validater
from eda.doc_event.consumer_doc import Consumer

# @frappe.whitelist(methods="POST",allow_guest=True)
def executer(payload):
    """
    {
        "module":"",
        "function":"",
        "hash":"",
        "doc_uuid":"",
        "argument":{
            
        }
    }
    """
    try:
        def set_log_doctype(doc_uuid,hash,payload_,error_log=None,status=None):
            return {
                "doc_uuid":doc_uuid,
                "hash":hash,
                "payload":payload_,
                "error_log":error_log,
                "status":status
            }
        doc = Consumer()
        new_doc = doc.insert(set_log_doctype(doc_uuid=payload["doc_uuid"],hash=payload["hash"],payload_=payload))
        error = None
        status = "Processed"
        try:
            json_validate = json_validater(payload)
            module_name = json_validate.get_module()
            function_name = json_validate.get_function()
            function_argument = json_validate.get_argument()
            my_module = importlib.import_module(module_name)
            my_function = getattr(my_module, function_name)
            my_function(function_argument)
        except Exception as e:
            error = frappe.get_traceback()
            frappe.log_error("Consumer Executer function faild inner try",message=error)
        if error != None:
            status = "Error" 
        doc.update_status({"status":status},new_doc.name)
    except Exception as er:
        frappe.log_error("Consumer Executer function faild",message=frappe.get_traceback())