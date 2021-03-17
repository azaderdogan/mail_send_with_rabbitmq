from datetime import date, datetime

import requests


class Mail:
    def __init__(self, me, to, title, content, send_date_time: datetime, create_date_time: datetime):
        self.me = me
        self.to = to
        self.title = title
        self.content = content
        self.send_date_time = send_date_time
        self.create_date_time = create_date_time

