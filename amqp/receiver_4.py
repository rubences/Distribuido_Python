#!/usr/bin/env python

import sys
from pika import BlockingConnection
from pika.connection import URLParameters

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.exchange_declare(exchange='tests_more', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(f"queue declared: {queue_name}")

if len(sys.argv) < 2:
    routes = ("N", "W", "S", "E")
else:
    routes = tuple(sys.argv[1])

print(f"Routes binded {routes}")

for route in routes:
    print(f"Route binded {route}")
    channel.queue_bind(exchange='tests_more', queue=queue_name, routing_key=route)

def callback(ch, method, properties, body):
    print(f"Received {body!r} from {method.routing_key}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

