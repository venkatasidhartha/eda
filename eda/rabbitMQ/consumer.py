import pika
from eda.rabbitMQ.utility import eda_settings
import frappe

class RabbitMQConsumer:
    def __init__(self, callback):
        self.settings = eda_settings()
        
        self.callback = callback
        self.queue_name = self.settings.queue_name
        print("^"*100)
        print("self.settings.user",self.settings.user)
        # Set RabbitMQ credentials
        credentials = pika.PlainCredentials(self.settings.user, self.settings.get_password('passwd'))

        # Connect to RabbitMQ server
        parameters = pika.ConnectionParameters(self.settings.url, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        # Declare queue
        self.channel.queue_declare(queue=self.queue_name)

        # Start consuming messages from queue
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

    def start_consuming(self):
        self.channel.start_consuming()

    def stop_consuming(self):
        self.channel.stop_consuming()

    def close_connection(self):
        self.connection.close()


def my_callback(ch, method, properties, body):
    print("*"*100)
    print(f"Received message: {body}")
    frappe.log_error(f"Received message: {body}", 'Consumer error')
    # import time
    # time.sleep(5)

my_callback("","","","")