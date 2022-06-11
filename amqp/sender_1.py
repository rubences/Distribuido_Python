#!/usr/bin/env python

from pika import BlockingConnection
from pika.connection import URLParameters

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.queue_declare(queue='test_1')

while True:
    data = input("> ")
    if not data:
        data = "STOP"
    channel.basic_publish(exchange='', routing_key='test_1', body=data)
    print(f"Sent '{data}'")
    if data == "STOP":
        break

connection.close()

