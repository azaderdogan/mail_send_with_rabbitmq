from mail import Mail
import requests
import smtplib
import os


def send(mail):
    transcode = 'e3da6689630c9fc01fc4f809b8f7912b235fb45ee461bdc59e'
    apikey = 'bkNfnkD9P3pLdQgj85rLjQ4xAH6ZSJOUUsW7Ds6immUq30w2VQ'
    url = f'http://www.setrowsend.com/email/send.php?k={apikey}&transcode={transcode}'

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


