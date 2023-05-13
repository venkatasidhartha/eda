from eda.rabbitMQ.producer import publisher
import frappe
from uuid import uuid4
from eda.event_handler.utility import json_validater
from eda.doc_event.producer_doc import Producer
from eda.hashing import generate_hash

class site_routing_key:
    erp = ""
    supplier = ""
    procurement = "procurement.karkhana.io"

class Publisher:
    def send(self,message:dict,to_server:str):
        """
            {
                "module":"",
                "function":"",
                "argument":{
                    
                },
                "doc_uuid":""
            }
        """
        hash = generate_hash()
        error = ""
        try:
            self.__set_hash(message=message,hash=hash)
            valid = json_validater(message)
            publisher(message,to_server)
        except Exception as e:
            error = frappe.get_traceback()
          
        doc = Producer()
        doc.insert(self.__set_log_doctype(doc_uuid=message["doc_uuid"],routed_to=to_server,hash=hash,payload=message,error_log=error))
       

    def __set_hash(self,hash,message):
        message["hash"] = hash

    def __set_log_doctype(self,doc_uuid,routed_to,hash,payload,error_log):
        return {
            "doc_uuid":doc_uuid,
            "routed_to":routed_to,
            "hash":hash,
            "payload":payload,
            "error_log":error_log
        }
