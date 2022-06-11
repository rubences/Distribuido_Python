#!/usr/bin/env python

from pika import BlockingConnection
from pika.connection import URLParameters

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.queue_declare(queue='test_1')


def callback(ch, method, properties, body):
    print(f"Received {body!r}")

channel.basic_consume(
    queue='test_1', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

