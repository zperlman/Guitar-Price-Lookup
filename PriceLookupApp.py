__author__ = "Zach Perlman"

import requests
from bs4 import BeautifulSoup

requests.get("https://shop.fender.com/en-US/electric-guitars/telecaster/classic-series-50s-telecaster/0131202301.html")
r = requests.get(
    "https://shop.fender.com/en-US/electric-guitars/telecaster/classic-series-50s-telecaster/0131202301.html")
content = r.content

print("This program will help you decide if it's a good time to purchase your favorite guitar.")

user_budget = int(input("What is your budget? Enter a number: "))
soup = BeautifulSoup(content, features="html.parser")
element = soup.find("span", {"class": "value", "itemprop": "price", "content": "799.99"})

price = element.text.strip()
price_no_currency = price[1:]
price_number = float(price_no_currency)

if price_number > user_budget:
    print("Don't buy this item now.")
    print("At {} this guitar is currently priced outside your budget.".format(price))
else:
    print("Now is a good time to buy this item.")
    print("At {} this guitar is currently priced within your budget.".format(price))
exit()
