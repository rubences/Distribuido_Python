#!/usr/bin/env python

import sys
from pika import BlockingConnection
from pika.connection import URLParameters

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.exchange_declare(exchange='tests_topics', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(f"queue declared: {queue_name}")

topics = sys.argv[1:]
if not topics:
    topics.append("all.end")

print(f"Topics binded {topics}")

for topic in topics:
    print(f"topic binded {topic}")
    channel.queue_bind(exchange='tests_topics', queue=queue_name, routing_key=topic)

def callback(ch, method, properties, body):
    print(f"Received {body!r} from {method.routing_key}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

