import requests

image_url = 'https://cbc-gict.net/t_kazama/py/image/sample1.png'
imgdata = requests.get(image_url)

filename = image_url.split('/')[-1]

with open(filename, mode='wb') as f:
    f.write(imgdata.content)