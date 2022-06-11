#!/usr/bin/env python

from random import choice
from pika import BlockingConnection, BasicProperties
from pika.connection import URLParameters

ROUTES = ("N", "W", "S", "E")

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.exchange_declare(exchange='tests_more', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(f"queue declared: {queue_name}")

channel.queue_bind(exchange='tests_more', queue=queue_name)

while True:
    data = input("> ")
    if not data:
        data = "STOP"
    route = choice(ROUTES)
    channel.basic_publish(exchange='tests_more', routing_key=route, body=data)
    print(f"publishing {data} to {route}")
    if data == "STOP":
        break

connection.close()

