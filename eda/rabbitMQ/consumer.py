import pika
from pika.exchange_type import ExchangeType
from eda.rabbitMQ.utility import eda_settings
import frappe
import time
from eda.event_handler.dynamic_import import executer
import json

def start_consuming():
    settings = eda_settings()
    frappe.log_error(f" consumer program started", 'wait for execute')
    queue_name = settings.queue_name
    exchange = settings.exchange
    routing_key = settings.routing_key
    # Set credentials
    credentials = pika.PlainCredentials(settings.user, settings.get_password('passwd'))
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(settings.url, credentials=credentials))
    channel = connection.channel()
    # Declare the topic exchange
    channel.exchange_declare(exchange=exchange, exchange_type=ExchangeType.topic)
    # Declare a queue for this consumer
    channel.queue_declare(queue_name, exclusive=False)
    # Bind the queue to the exchange with the routing key
    # binding_key = 'important.events.error'
    channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
    # Poll the queue for new messages
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
        if method_frame:
            # A message is available, process it
            print("Received message:", body.decode())
            frappe.log_error(f"{body.decode()}", 'Consumer error new data from cron job')
            executer(json.loads(body.decode()))
            # connection.close()
            # break
        else:
            # No message available, sleep for some time before polling again
            time.sleep(1)
