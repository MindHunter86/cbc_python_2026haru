import requests

url = 'https://cbc-gict.net/t_kazama/py/test1.html'

response = requests.get(url)
response.encoding = response.apparent_encoding

print(response.text)
print(response.url)
print(response.status_code)