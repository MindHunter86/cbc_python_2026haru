import requests
from bs4 import BeautifulSoup

load_url = 'https://cbc-gict.net/t_kazama/py/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content,'html.parser')

for element in soup.find_all('a') :
    print(element.text)
    url = element.get('href')
    print(url)