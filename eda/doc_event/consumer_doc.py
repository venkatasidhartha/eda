import frappe
import calendar
import time


class Consumer:
    def insert(self,record:dict):
        """{
                "doc_uuid":"",
                "hash":"",
                "payload":"",
                "error_log":"",
                "status":""
            }"""
        try:
            doc = {
                "doctype":"Consumer Logs",
                "doc_uuid":record["doc_uuid"],
                "timestamp":calendar.timegm(time.gmtime()),
                "hash":record["hash"],
                "payload":record["payload"]
                }
            if "error_log" in record:
                doc["error_log"] = record["error_log"]
            if "status" in record and record["status"] != None:
                doc["status"] = record["status"]
            
            new_doc = frappe.get_doc(doc)
            new_doc.save(ignore_permissions=True)
            return new_doc
        except Exception as e:
            frappe.log_error(title="Consumer Logs Doctype Insert Failed",message=frappe.get_traceback())

    def update_status(self,record:dict,id):
        """{
                "status":""
        }"""
        update_doc = frappe.get_doc("Consumer Logs",id)
        if "status" in record:
            update_doc.status = record["status"]
        update_doc.save(ignore_permissions=True)

        