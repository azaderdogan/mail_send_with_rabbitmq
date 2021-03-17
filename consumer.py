import json
import os
import sys
from pprint import pprint
from utils import dict_to_mail
import pika

from utils import datetime_convertor

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672)
)
channel = connection.channel()


def consumer():
    def callback(ch, method, properties, body: bytes):
        body = body.decode().__str__()
        body = json.loads(body)

        dict_to_mail(body)

    channel.basic_consume(queue='email', on_message_callback=callback, auto_ack=True, )
    channel.start_consuming()


if __name__ == '__main__':
    try:
        consumer()
    except KeyboardInterrupt:
        connection.close()
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

