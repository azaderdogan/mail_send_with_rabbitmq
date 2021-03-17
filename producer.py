import json

from datetime import date, datetime
from pprint import pprint

from utils import calculate_millisecond, datetime_convertor
from mail import Mail
import pika
import os

url = os.environ.get("CLOUDAMQP_URL", "amqp://guest:guest@localhost:5672/")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

consumer_queue = 'email'


def create_producer_queue(connection: pika.BlockingConnection):
    channel = connection.channel()

    channel.confirm_delivery()
    channel.queue_declare(queue=consumer_queue, durable=True)
    channel.queue_bind(exchange='amq.direct', queue=consumer_queue)
    return channel


def create_delay_queue(queue_name, ttl):
    delay_channel = connection.channel()
    delay_channel.confirm_delivery()

    delay_channel.queue_declare(queue=f'{queue_name}',
                                auto_delete=True,
                                durable=True,
                                arguments={
                                    'x-message-ttl': ttl,
                                    'x-dead-letter-exchange': 'amq.direct',
                                    'x-dead-letter-routing-key': consumer_queue,
                                    'x-expires': ttl + 600000
                                })
    return delay_channel


mail = Mail(me="azad",
            to="sema",
            title="başlık",
            content="içerik",
            send_date_time=datetime(2023, 3, 17, 16, 40, 5),
            create_date_time=datetime.today())


def send_message(mail: Mail):
    create_producer_queue(connection)
    queue_name = f'{mail.send_date_time.today()}'
    send_date_time = mail.send_date_time
    created_date_time = mail.create_date_time
    ttl = calculate_millisecond(created_date_time, send_date_time)
    email = json.dumps(mail.__dict__, default=datetime_convertor)
    delay_channel = create_delay_queue(queue_name, ttl)
    email = email.encode(encoding='utf-8').decode(encoding='utf-8')
    delay_channel.basic_publish(exchange='',
                                routing_key=f'{queue_name}',
                                body=email,
                                properties=pika.BasicProperties(
                                    delivery_mode=1,
                                    content_encoding='utf-8',
                                    content_type='application/json'
                                ), )


def fake_send_message(mail: Mail):
    delay_channel = create_producer_queue(connection)
    queue_name = f'{mail.send_date_time.today()}'
    send_date_time = mail.send_date_time
    created_date_time = mail.create_date_time
    ttl = calculate_millisecond(created_date_time, send_date_time)

    email = json.dumps(mail.__dict__, default=datetime_convertor,ensure_ascii=False).encode('utf8').decode()
    pprint(email)
    delay_channel.basic_publish(exchange='',
                                routing_key=f'{consumer_queue}',
                                body=email,
                                properties=pika.BasicProperties(
                                    content_encoding='utf-8',
                                    content_type='application/json',
                                    delivery_mode=2
                                )
                                )


fake_send_message(mail)
