import pika
from pika.exchange_type import ExchangeType
import json
from eda.rabbitMQ.utility import eda_settings
import frappe
import ssl

def publisher(message,routing_key):
    try:
        settings = eda_settings()
        if settings.switch:
            exchange = settings.exchange
            message = json.dumps(message) #{"module":"eda_test_app.test","function":"test","argument":""}
            # Set credentials
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
            url = settings.url
            parameters = pika.URLParameters(url)
            parameters.ssl_options = pika.SSLOptions(context=ssl_context)
            connection = pika.BlockingConnection(parameters)
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
