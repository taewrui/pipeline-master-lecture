import urllib.request as req
from bs4 import BeautifulSoup
import datetime

url = "https://finance.naver.com/marketindex/"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
currency = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value")
print(f"Date : {now} USD : {currency.string}")