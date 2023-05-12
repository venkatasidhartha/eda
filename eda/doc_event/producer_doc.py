import frappe



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
        try:
            doc = {
                "doctype":"Producer Logs",
                "doctype_name":record["doctype_name"],
                "docname":record["docname"],
                "timestamp":"",
                "routed_to":record["routed_to"],
                "hash":record["hash"],
                "payload":record["payload"],
                "error_log":record["error_log"]
            }
            new_doc = frappe.get_doc(doc)
            new_doc.save(ignore_permissions=True)
        except:
            frappe.log_error(title="Producer Logs Insert Failed",message=frappe.get_traceback())

    def update(self,record:dict):
        pass
