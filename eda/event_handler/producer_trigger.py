import frappe
from eda.rabbitMQ.producer import publisher
import json
import ast


def schedule_pub(doc,event=None):
    frappe.enqueue("eda.event_handler.producer_trigger.trigger_publish",doc=doc,queue="short")
    

def trigger_publish(doc):
    pub_doc = ast.literal_eval(doc.payload) 
    pub_doc["hash"] = doc.hash
    publisher(pub_doc,doc.routed_to)


