import frappe
from eda.rabbitMQ.producer import publisher
import json
import ast


def schedule_pub(doc,event=None):
    frappe.enqueue("eda.event_handler.producer_trigger.trigger_publish",doc=doc,queue="short")
    

def trigger_publish(doc):
    pub_doc = {
        "doc_uuid":doc.doc_uuid,
        "hash":doc.hash,
        "payload":ast.literal_eval(doc.payload)
    }
    publisher(pub_doc,doc.routed_to)


