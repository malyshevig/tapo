import multiprocessing

import pika

from multiprocessing import Process
import os

queue_from = 'words'
host="127.0.0.1"
user = "words"
passwd = "words"

multiprocessing.set_start_method("fork")

credentials = pika.PlainCredentials(user, passwd)
wordsparameters = pika.ConnectionParameters(host=host, port='5672', credentials=credentials)


def on_message_callback(channel, method, properties, body):
    binding_key = method.routing_key
    print (body)


def read():
    print ("reading")
    credentials = pika.PlainCredentials(user, passwd)
    parameters = pika.ConnectionParameters(host=host, port='5672', credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.basic_consume(queue=queue_from,
                          on_message_callback=on_message_callback, auto_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    print("Exit")

def main ():

    t=Process(target=read)
    t.start()


    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    # тут получаем количество сообщений в нашей очереди

    while True:
        l = input("str:")
        print (f"publish: {l}")
        if l == "end":
            break


        channel.basic_publish(exchange="", routing_key=queue_from, body=l)




    channel.close()
    connection.close()
    t.join()

class Publisher:

    def __init__(self):
        credentials = pika.PlainCredentials(user, passwd)
        parameters = pika.ConnectionParameters(host=host, port='5672', credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def open(self):
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def publish(self, word:str):
        if word is not None and len(word )> 0:
            self.channel.basic_publish(exchange="", routing_key=queue_from, body=word)


    def close(self):
        self.channel.close()
        self.connection.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def test():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()


if __name__ == "__main__":
    test()
