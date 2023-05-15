import pika
from pika.exchange_type import ExchangeType
from eda.rabbitMQ.utility import eda_settings
import frappe
import time
import json
from eda.doc_event.consumer_doc import Consumer_log
import ssl

def start_consuming():
    try:
        settings = eda_settings()
        if settings.switch:
            frappe.log_error(f"consumer program started", 'wait for execute')
            queue_name = settings.queue_name
            exchange = settings.exchange
            routing_key = settings.routing_key
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
            url = settings.url
            parameters = pika.URLParameters(url)
            parameters.ssl_options = pika.SSLOptions(context=ssl_context)
            connection = pika.BlockingConnection(parameters)
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
                    frappe.enqueue("eda.rabbitMQ.consumer.background_insert",body=body,queue="short")
                else:
                    time.sleep(10)
                    constumer_used+=1
    except Exception as error:
        frappe.log_error(title="RabbitMQ Consumer Faild",message=frappe.get_traceback())

def background_insert(body):
    doc = Consumer_log()
    doc.insert(json.loads(body.decode()))

    