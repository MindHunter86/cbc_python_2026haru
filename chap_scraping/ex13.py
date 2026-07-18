import requests
from bs4 import BeautifulSoup
import urllib

load_url = 'https://news.yahoo.co.jp/'
html = requests.get(load_url)
soup = BeautifulSoup(html.content,'html.parser')

topic = soup.find(class_='topics')

filename = 'linklist2.txt'
with open(filename , 'w') as f:
    for li in topic.find_all('li'):
        for element in li.find_all('a') :
            url = element.get('href')
            link_url = urllib.parse.urljoin(load_url , url)
            f.write(element.text + '\n')
            f.write(link_url + '\n')
            f.write('\n')