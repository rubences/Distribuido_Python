#!/usr/bin/env python

from time import sleep
from pika import BlockingConnection
from pika.connection import URLParameters

connection = BlockingConnection(
    URLParameters('amqp://test:test@localhost:5672/vhost'))
channel = connection.channel()

channel.queue_declare(queue='test_2', durable=True)

def callback(ch, method, properties, body):
    print(f"Received {body!r} ... ")
    sleep(len(body))
    print(f"... {body!r} Done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test_2', on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

