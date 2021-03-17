from mail import Mail
import requests
import smtplib
import os


url = 'http://www.setrowsend.com/email/send.php?k=bkNfnkD9P3pLdQgj85rLjQ4xAH6ZSJOUUsW7Ds6immUq30w2VQ&transcode=9a2034618ce854b1ff686231cf1269b1581e2ebb7984382bbc'

content = 'Email içeriği'
# gmaili mail serverlarına bağlıyoruz
mail = smtplib.SMTP(host='smtp.gmail.com', port=587)

data = [{
    "gonderen_adi": "Şablon gönderen adı (from name) bilgisi",
    "musterigonderimid": "ID123Q",
    "adres": "email@domain.com",
    "alanlar": {"content": "icerik_content", "subject": "icerik_subject"},
    "dosya_ek": []
}]

if __name__ == '__main__':
    pass
