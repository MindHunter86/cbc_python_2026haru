import urllib.parse
import requests , urllib , time
from bs4 import BeautifulSoup
from pathlib import Path
import sys, time

target_url = 'https://www.irasutoya.com/'

resp = requests.get(target_url)
if resp.status_code != 200:
    print('some troubles with loading url')
    sys.exit(1)

sp = BeautifulSoup(resp.content, 'html.parser')

fd = Path('download')
fd.mkdir(exist_ok=True)

imgcnt = 0

for div1 in sp.find('div', id='homedesign').find_all('div', id='section_banner'):
    for img in div1.find_all('img'):
        imgsrc = img.get('src')
        if not imgsrc:
            print('could not load image ' + img.get('alt'))
            continue

        imgpath = urllib.parse.urljoin(target_url, imgsrc)
        print(f'downloading {imgpath} ...')
        imgdata = requests.get(imgpath)

        if imgdata.status_code != 200:
            print('could not download picture from target, status not OK')

        fdname = imgpath.split('/')[-1]
        fdext = fdname.split('.')[-1]
        fdout = fd.joinpath('{}.{}'.format(str(imgcnt).zfill(3), fdext))

        with open(fdout, mode='wb') as f:
            f.write(imgdata.content)

        imgcnt+=1
        time.sleep(0.5)