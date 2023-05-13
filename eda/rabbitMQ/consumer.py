import pika
from pika.exchange_type import ExchangeType
from eda.rabbitMQ.utility import eda_settings
import frappe
import time
from eda.event_handler.dynamic_import import executer
import json

def start_consuming():
    settings = eda_settings()
    if settings.switch:
        frappe.log_error(f"consumer program started", 'wait for execute')
        queue_name = settings.queue_name
        exchange = settings.exchange
        routing_key = settings.routing_key
        credentials = pika.PlainCredentials(settings.user, settings.get_password('passwd'))
        connection = pika.BlockingConnection(pika.ConnectionParameters(settings.url, credentials=credentials))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type=ExchangeType.topic)
        channel.queue_declare(queue_name, exclusive=False)
        channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        constumer_used = 0
        while True:
            if constumer_used == 10:
                connection.close()
                break
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
            if method_frame:
                executer(json.loads(body.decode()))
            else:
                time.sleep(10)
                constumer_used+=1