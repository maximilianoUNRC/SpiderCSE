#!/usr/bin/env python
import pika
import os
import time
import serial

credentials=pika.PlainCredentials('asus','asus')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.103',5672,'/',credentials)) # Connect to CloudAMQP

channel = connection.channel()
channel.exchange_declare(exchange='command',type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='command',queue=queue_name)

channel1 = connection.channel()
channel1.exchange_declare(exchange='mensaje',type='fanout')
msg = "Escuchando Comandos presionados"
channel1.basic_publish(exchange='mensaje', routing_key='',body=msg)

ser = serial.Serial("/dev/ttyS0",57600)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    msg = str(body)
    channel1.basic_publish(exchange='mensaje', routing_key='',body=msg)

    if body == 'w':
	ser.write('w 1 1\r\n')
    if body == 's':
	ser.write('w 2 1\r\n')
    if body == 'd':
	ser.write('w 3 1\r\n')
    if body == 'a':
	ser.write('w 4 1\r\n')
    if body == 'k':
	ser.write('w 5 5\r\n')
	ser.write('w 0 0\r\n')

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

