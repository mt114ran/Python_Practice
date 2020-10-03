from bs4 import BeautifulSoup
import requests

url="https://weather.yahoo.co.jp/weather/jp/13/4410.html"

r = requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')

high = soup.select(".high")[0].text[0:3]

low = soup.select(".low")[0].text[0:3]

print("今日の東京の最高気温は {} 、最低気温は {} です".format(high,low))