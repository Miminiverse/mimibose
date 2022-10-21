import csv, smtplib, ssl
from bs4 import BeautifulSoup
import requests
import time
import creds


HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

url = "https://www.amazon.com/Bose-Cancelling-Wireless-Bluetooth-Headphones/dp/B07Q9MJKBV?th=1"

html = requests.get(url, headers=HEADERS)


soup = BeautifulSoup(html.content, "lxml")


def get_price():
    try:
        price = soup.find("span", attrs={'class': 'a-price-whole'}).text.replace('.', '')
    except AttributeError:
        price = "NA"
    return (price)


def emailnew(price):
    sender = "test140266@gmail.com"
    receiver = "test140266@gmail.com"
    password = creds.password

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:

        server.login(sender, password)
        server.sendmail(sender, receiver, f"Subject: Price Tracker - Bose Noise Cancelling Headphones 700 \n\nPrice has been updated to {price} \n\n https://www.amazon.com/Bose-Cancelling-Wireless-Bluetooth-Headphones/dp/B07Q9MJKBV?th=1 ")


emailnew(get_price())