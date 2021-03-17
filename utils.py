from datetime import timedelta, datetime


def days_between_two_dates(created_date: datetime, send_date: datetime):
    now = created_date
    delta_date = send_date - now

    return delta_date


def date_to_millisecond(timedelta: timedelta):
    day = timedelta.days
    seconds = timedelta.seconds
    millisecond = (day * 24 * 60 * 60 * 1000) + (seconds * 1000)
    assert millisecond >= 0
    return millisecond


def calculate_millisecond(created_date: datetime, send_date: datetime):
    delta = days_between_two_dates(created_date=created_date, send_date=send_date)

    ms = date_to_millisecond(delta)
    return ms


def datetime_convertor(date: datetime):
    if isinstance(date, datetime):
        return date.__str__()


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = f'{BASE_DIR}/queues.txt'


def save_queue(queue: str):
    file = open(FILE_PATH, 'a', encoding='utf-8')
    file.write(f'{queue}\n')


from mail import Mail


def dict_to_mail(data: dict):
    mail = Mail
    mail.content = data['content']
    mail.create_date_time = data['create_date_time']
    mail.me = data['me']
    mail.send_date_time = data['send_date_time']
    mail.title = data['title']
    mail.to = data['to']
    return mail
