#!/usr/bin/env python
import pika
import os


credentials=pika.PlainCredentials('asus','asus')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.103',5672,'/',credentials)) # Connect to CloudAMQP
channel = connection.channel()

channel.exchange_declare(exchange='mensaje',
                         type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='mensaje',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
