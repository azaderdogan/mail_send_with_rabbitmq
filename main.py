from mail import Mail
import requests
import smtplib
import os
from producer import send_message

mail = Mail(me="T3",
            to="azad56azad56@gmail.com",
            title="başlık",
            content="içerik",
            send_date_time=datetime(2023, 3, 17, 16, 40, 5),
            create_date_time=datetime.today())






if __name__ == '__main__':
    send_message()