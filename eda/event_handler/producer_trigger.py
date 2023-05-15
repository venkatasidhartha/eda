import frappe
from eda.rabbitMQ.producer import publisher
import json


def schedule_pub(doc,event=None):
    frappe.enqueue("eda.event_handler.producer_trigger.trigger_publish",doc=doc,queue="short")
    

def trigger_publish(doc):
    publisher(doc.payload,doc.routed_to)


    