
import frappe
from uuid import uuid4
from eda.doc_event.utility import validater
from eda.doc_event.producer_doc import Producer_log

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
        if message is None or message == "" or to_server is None or to_server == "":
            raise ValueError("Both 'message' and 'to_server' parameters are required for this function.")
        validate = validater(message,["module","function","argument","doc_uuid"])
        new_doc = Producer_log()
        record = {
            "doc_uuid":message["doc_uuid"],
            "routed_to":to_server,
            "payload":message
        }
        new_doc.insert(record)

        
       
          