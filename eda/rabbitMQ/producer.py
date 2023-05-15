import pika
from pika.exchange_type import ExchangeType
import json
from eda.rabbitMQ.utility import eda_settings
import frappe

def publisher(message,routing_key):
    try:
        settings = eda_settings()
        if settings.switch:
            exchange = settings.exchange
            message = json.dumps(message) #{"module":"eda_test_app.test","function":"test","argument":""}
            # Set credentials
            credentials = pika.PlainCredentials(settings.user, settings.get_password('passwd'))
            # Connect to RabbitMQ server
            connection = pika.BlockingConnection(pika.ConnectionParameters(settings.url, credentials=credentials))
            channel = connection.channel()
            # Declare exchange
            channel.exchange_declare(exchange=exchange, exchange_type=ExchangeType.topic)
            # Publish message with topic routing
            routing_key = routing_key
            channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
            # Close connection
            connection.close()
    except Exception as e:
        frappe.log_error(title="RabbitMQ Publisher Faild",message=frappe.get_traceback())
