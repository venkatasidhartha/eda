import frappe
import calendar
import time


class Producer:
    def insert(self,record:dict):
        """{
                "doc_uuid":"",
                "routed_to":"",
                "hash":"",
                "payload":"",
                "error_log":""
            }"""
        try:
            doc = {
                "doctype":"Producer Logs",
                "doc_uuid":record["doc_uuid"],
                "timestamp":calendar.timegm(time.gmtime()),
                "routed_to":record["routed_to"],
                "hash":record["hash"],
                "payload":record["payload"],
                "error_log":record["error_log"]
            }
            new_doc = frappe.get_doc(doc)
            new_doc.save(ignore_permissions=True)
            return new_doc
        except Exception as error:
            frappe.log_error(titile="Producer Logs Doctype Insert Failed",message=frappe.get_traceback())


    def update(self,record:dict):
        pass
