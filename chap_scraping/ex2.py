import requests

filename = 'download.txt'

url = 'https://cbc-gict.net/t_kazama/py/test1.html'
response = requests.get(url)
response.encoding = response.apparent_encoding

with open(filename , mode='w') as f:
    f.write(response.text)