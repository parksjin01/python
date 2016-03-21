import urllib2
import webbrowser
site= "https://search.naver.com/search.naver?where=nexearch&query=zz&sm=top_hty&fbm=0&ie=utf8"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
response = urllib2.urlopen(req)
print 'Response: ', response
print 'URL: ', response.geturl()

"""headers=response.info()
print 'Date: ', headers['date']
print 'Headers: '
print '-'*50
print headers

dat=response.read(100000)
print 'Length: ', len(dat)
print 'Data: '
print '-'*50
print dat"""

# Open URL in new browser window

# Opens in safari browser

# Open URL in a new tab
webbrowser.open_new_tab(response.geturl()) # opens in default browser

# Opens in safari browser
