
import frappe
from eda.doc_event.utility import validater
from eda.doc_event.producer_doc import Producer_log
from eda.rabbitMQ.utility import eda_settings 
import ast

class site_routing_key:
    def __init__(self):
        kwargs = self.json_data()
        for key, value in kwargs.items():
            setattr(self, key, value)
    def json_data(self):
        data = eda_settings().servers
        return ast.literal_eval(data)
    
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

        
       
          