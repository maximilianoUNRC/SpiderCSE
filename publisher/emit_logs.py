#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import sys
import time
import getch

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

print("---------------------------------------------------")
print("| Mover la araña con las teclas         __        |")
print("|                  W: Avanza         | /  \ |     |")
print("|    W             A: Izquierda     \\_\\\\  //_/    |")
print("|  A S D           S: Retrocede      -'/()\\'-     |")
print("|                  D: Derecha         \\\  //      |")
print("|    K             K: Kill them all               |")
print("---------------------------------------------------")

while 1:
    char = getch.getch()
    message  = str(char)
    
    if message == 'w' or message == 'W':
       channel.basic_publish(exchange='logs',routing_key='',body=message)
       print("Avanza")
    if message == 'a' or message == 'A':
       channel.basic_publish(exchange='logs',routing_key='',body=message)
       print("Mover a la izquierda")
    if message == 's' or message == 'S':
       channel.basic_publish(exchange='logs',routing_key='',body=message)
       print("Retroceder")
    if message == 'd' or message == 'D':
       channel.basic_publish(exchange='logs',routing_key='',body=message)
       print("Mover a la derecha")
    if message == 'k' or message == 'K':
       channel.basic_publish(exchange='logs',routing_key='',body=message)
       print("ta ta ta ta ta ta")
connection.close()





	
