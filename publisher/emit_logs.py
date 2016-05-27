#!/usr/bin/env python
import pika
import sys
import time

credentials = pika.PlainCredentials('fer', 'caffaro')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.10.134',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

#cant_mensajes = join(sys.argv[1]) or 1
#duracion_mensaje = join(sys.argv[3]) or 1
#print(" cant: %s", cant_mensajes )
#print(" dur: %s", cant_mensajes )

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
while 1:
    channel.basic_publish(exchange='logs',routing_key='',body=message)
    print(" [x] Sent %r" % message)
    time.sleep(1)
connection.close()
