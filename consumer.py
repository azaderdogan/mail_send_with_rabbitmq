import json
import os
import sys

import requests

from utils import dict_to_mail,TRANSCODE,APIKEY
import pika

from utils import datetime_convertor

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672)
)
channel = connection.channel()
def send(mail):

    url = f'http://www.setrowsend.com/email/send.php?k={APIKEY}&transcode={TRANSCODE}'

    data = [{
        "gonderen_adi": "Türkiye Teknoloji Takımı",
        "musterigonderimid": "ID123Q",
        "adres": f"{mail.to}",
        "alanlar": {"content": f"{mail.content}", "subject": f"{mail.title}"},
        "dosya_ek": []
    }]

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('başarılı')
        print(response.json())
    else:
        print(response.status_code)
        print(response.json())

def consumer():
    def callback(ch, method, properties, body: bytes):
        body = body.decode().__str__()
        body = json.loads(body)
        mail = dict_to_mail(body)
        send(mail)

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
