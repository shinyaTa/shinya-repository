import requests
from bs4 import BeautifulSoup

r = requests.get('https://news.yahoo.co.jp')

soup = BeautifulSoup(r.content,"html.parser")

newslist = soup.find("ul","topicsList_main")

for news in newslist:
    print(news.text)
