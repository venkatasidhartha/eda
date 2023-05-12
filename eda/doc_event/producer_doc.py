import frappe
import calendar
import time


class Producer:
    def insert(self,record:dict):
        """{
                "doctype_name":"",
                "docname":"",
                "routed_to":"",
                "hash":"",
                "payload":"",
                "error_log":""
            }"""
        doc = {
            "doctype":"Producer Logs",
            "doctype_name":record["doctype_name"],
            "docname":record["docname"],
            "timestamp":calendar.timegm(time.gmtime()),
            "routed_to":record["routed_to"],
            "hash":record["hash"],
            "payload":record["payload"],
            "error_log":record["error_log"]
        }
        new_doc = frappe.get_doc(doc)
        new_doc.save(ignore_permissions=True)

    def update(self,record:dict):
        pass
