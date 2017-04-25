import urllib2
import urllib
import re
response=urllib2.urlopen('http://www.naver.com')
print 'Response: ', response
print 'URL: ', response.geturl()

headers=response.info()
print 'Date: ', headers['date']
print 'Headers: '
print '-'*50
print headers

dat=response.read()
print 'Length: ', len(dat)
print 'Data: '
print '-'*50
r=re.search('noscript', dat)
s=r.start()
r=re.search('/noscript', dat)
e=r.end()
dat= dat[s:e + 1].split('\n')
for i in range(4, 14):
    s=re.search('">', dat[i]).end()
    e=re.search('</', dat[i]).start()
    print dat[i][s:e]
