import requests
from bs4 import BeautifulSoup

load_url = 'https://cbc-gict.net/t_kazama/py/test1.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content,'html.parser')

print(soup.find('title').text)
print(soup.find('h2') .text)
print(soup.find('li') .text)