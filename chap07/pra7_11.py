from http.client import HTTPSConnection

conn = HTTPSConnection('www.cbc.ac.jp')

conn.request('GET', '/')
res = conn.getresponse()
conn.close()

print(res.getheaders())