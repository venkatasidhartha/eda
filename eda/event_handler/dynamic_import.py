import importlib
import frappe
from eda.event_handler.utility import json_validater


# @frappe.whitelist(methods="POST",allow_guest=True)
def executer(payload):
    """
    {
        "module":"",
        "function":"",
        "argument":{
            
        }
    }
    """
    try:
        json_validate = json_validater(payload)
        module_name = json_validate.get_module()
        function_name = json_validate.get_function()
        function_argument = json_validate.get_argument()
        my_module = importlib.import_module(module_name)
        my_function = getattr(my_module, function_name)
        my_function(function_argument)
    except Exception as error:
        frappe.log_error(title="Consumer executer Failed",message=frappe.get_traceback())
