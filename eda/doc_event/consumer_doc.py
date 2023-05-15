import frappe
import calendar
import time


class Consumer_log:
    def insert(self,record:dict):
        """{
                "doc_uuid":"",
                "hash":"",
                "payload":""
            }"""
        try:
            doc = {
                "doctype":"Consumer Logs",
                "doc_uuid":record["doc_uuid"],
                "timestamp":calendar.timegm(time.gmtime()),
                "hash":record["hash"],
                "payload":str(record["payload"])
                }
            if "error_log" in record:
                doc["error_log"] = str(record["error_log"])
            if "status" in record and record["status"] != None:
                doc["status"] = record["status"]
            
            new_doc = frappe.get_doc(doc)
            new_doc.save(ignore_permissions=True)
            frappe.db.commit()
            return new_doc
        except Exception as e:
            frappe.log_error(title="Consumer Logs Doctype Insert Failed",message=frappe.get_traceback())

    def update_status(self,record:dict,id):
        """{
                "error_log":"",
                "status":""
        }"""
        try:
            update_doc = frappe.get_doc("Consumer Logs",id)
            if "error_log" in record:
                update_doc.error_log = str(record["error_log"])
            if "status" in record:
                update_doc.status = record["status"]
            update_doc.save(ignore_permissions=True)
        except Exception as e:
            frappe.log_error(title="Consumer Logs Doctype Update Failed",message=frappe.get_traceback())

        
