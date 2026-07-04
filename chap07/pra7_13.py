import requests

response = requests.get('https://www.python.org/download/')
text = response.text
print(text)