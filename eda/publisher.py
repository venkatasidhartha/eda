from eda.rabbitMQ.producer import publisher
import frappe

class site_routing_key:
    erp = ""
    supplier = ""
    procurement = ""

class Publisher:

    def servers(self):
        return site_routing_key()

    def send(self,message,which_server):
        try:
            publisher(message,which_server)
        except Exception as e:
            frappe.log_error(title="Publisher Failed",message=frappe.get_traceback())    



