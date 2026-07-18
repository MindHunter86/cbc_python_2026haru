import requests
from bs4 import BeautifulSoup

load_url = 'https://cbc-gict.net/t_kazama/py/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content,'html.parser')

chap2 = soup.find(id = 'chap2')
print(chap2)