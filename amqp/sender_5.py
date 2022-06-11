#!/usr/bin/env python

from pika import BlockingConnection, BasicProperties
from pika.connection import URLParameters

ROUTES = {"N", "W", "S", "E"}

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
    if not ":" in data:
        if not data:
            data = "STOP"
        routes = ROUTES
    else:
        data_parts = data.split(":")
        routes, data = set(d.upper() for d in data_parts[0]) & ROUTES, ":".join(data_parts[1:])
    print(f"Publishing to {routes}")
    for route in routes:
        print(f"publish {data} to {route}")
        channel.basic_publish(exchange='tests_more', routing_key=route, body=data)
    print(f"Sent '{data}'")
    if data == "STOP":
        break

connection.close()

