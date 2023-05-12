from eda.rabbitMQ.producer import publisher
import frappe
from uuid import uuid4
from eda.event_handler.utility import json_validater
from eda.doc_event.producer_doc import Producer
class site_routing_key:
    erp = ""
    supplier = ""
    procurement = ""

class Publisher:

    def servers(self):
        return site_routing_key()

    def send(self,message:dict,to_server:str,doctype:str,doc_name:str):
        """
            {
                "module":"",
                "function":"",
                "argument":{
                    
                }
            }
        """
        hash = str(uuid4())
        error = ""
        try:
            valid = json_validater(message)
            self.__set_hash(message=message,hash=hash)
            publisher(message,to_server)
        except Exception as e:
            error = frappe.get_traceback()   
        doc = Producer()
        doc.insert(self.__set_doctype(doctype_name=doctype,docname=doc_name,routed_to=to_server,hash=hash,payload=message,error_log=error))



    def __set_hash(self,hash,message):
        message["hash"] = hash

    def __set_doctype(self,doctype_name,docname,routed_to,hash,payload,error_log):
        return {
            "doctype_name":doctype_name,
            "docname":docname,
            "routed_to":routed_to,
            "hash":hash,
            "payload":payload,
            "error_log":error_log
        }
