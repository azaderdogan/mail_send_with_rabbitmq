from datetime import datetime
from mail import Mail
from producer import send_message

mail = Mail(me="T3",
            to="azad56azad56@gmail.com",
            title="başlık",
            content="içerik",
            send_date_time=datetime(2021, 3, 17, 20, 0, 0),
            create_date_time=datetime.today())

if __name__ == '__main__':
    send_message(mail)
