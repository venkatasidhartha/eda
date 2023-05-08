import pika
from eda.rabbitMQ.utility import eda_settings
import frappe

class RabbitMQConsumer:
    def __init__(self, callback):
        self.settings = eda_settings()
        self.callback = callback
        self.queue_name = self.settings.queue_name
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
    frappe.log_error(f"{body} <--->", 'Consumer error')
    


def start_consuming():
    print("consumer started")

    consumer = RabbitMQConsumer(my_callback)
    consumer.start_consuming()
    return True
    


def cheking_hook_scheduler():
    print("running in cron scheduler_events")
    frappe.log_error(f"scheduler_events <--->", 'Consumer error')