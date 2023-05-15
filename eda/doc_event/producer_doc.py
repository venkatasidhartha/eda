import frappe
import calendar
import time
from eda.hashing import generate_hash
from eda.doc_event.utility import validater

class Producer_log:
    def insert(self,record:dict):
        """{
                "doc_uuid":"",
                "routed_to":"",
                "payload":"",
            }"""
        try:
            validate = validater(record,["doc_uuid","routed_to","payload"])
            doc = {
                "doctype":"Producer Logs",
                "doc_uuid":record["doc_uuid"],
                "timestamp":calendar.timegm(time.gmtime()),
                "routed_to":record["routed_to"],
                "hash":generate_hash(),
                "payload":str(record["payload"]),
            }
            new_doc = frappe.get_doc(doc)
            new_doc.save(ignore_permissions=True)
            frappe.db.commit()
            return new_doc
        except Exception as error:
            frappe.log_error(title="Producer Logs Doctype Insert Failed",message=frappe.get_traceback())


    def update(self,record:dict,id):
        pass


