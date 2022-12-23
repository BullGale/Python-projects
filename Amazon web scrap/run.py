import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/Vills-Laurrens-VL-1114-Stunning-Black/dp/B07GL4RYMC/ref=sr_1_35?crid=1XHE2ITXHIAVL&keywords=watches&qid=1656996334&sprefix=watche%2Caps%2C324&sr=8-35"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
# 1775399773563191&amp
price = soup.find(class_="a-color-price").get_text()
# print(price)
# price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
# print(price_without_currency)
title = soup.find(id="productTitle").get_text().strip()
# print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    # with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
    #     connection.starttls()
        # result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        # connection.sendmail(
        #     from_addr=YOUR_EMAIL,
        #     to_addrs=YOUR_EMAIL,
        #     msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        # )