#!/usr/bin/env python

from pika import BlockingConnection, BasicProperties
from pika.connection import URLParameters

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.exchange_declare(exchange='tests', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(f"queue declared: {queue_name}")

channel.queue_bind(exchange='tests', queue=queue_name)

while True:
    data = input("> ")
    if not data:
        data = "STOP"
    channel.basic_publish(exchange='tests', routing_key='', body=data)
    print(f"Sent '{data}'")
    if data == "STOP":
        break

connection.close()

