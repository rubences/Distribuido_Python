#!/usr/bin/env python

from pika import BlockingConnection, BasicProperties
from pika.connection import URLParameters

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.exchange_declare(exchange='tests_topics', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(f"queue declared: {queue_name}")

channel.queue_bind(exchange='tests_topics', queue=queue_name)

while True:
    data = input("> ")
    if not ":" in data:
        topic = "all.end"
        if not data:
            data = "STOP"
    else:
        data_parts = data.split(":")
        topic, data = data_parts[0], ":".join(data_parts[1:])
    print(f"publish {data} to {topic}")
    channel.basic_publish(exchange='tests_topics', routing_key=topic, body=data)
    if data == "STOP":
        break

connection.close()

