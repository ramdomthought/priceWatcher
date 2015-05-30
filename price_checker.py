# -*- coding: utf8 -*-
import urllib2	##https://docs.python.org/2/library/urllib2.html
import sys		##https://docs.python.org/2/library/sys.html
import re		##https://docs.python.org/2/library/re.html
import urlparse	##https://docs.python.org/2/library/urlparse.html

#take in url
print("Enter a URL:")
urlInput = raw_input()

#request and 'handle' data from url

req = urllib2.Request(urlInput)
handler = urllib2.urlopen(req)

#parse url to determine domain (url.netloc)
url = urlparse.urlparse(urlInput)



#for urls that match "¥"

##rakuten global
if (url.netloc == 'global.rakuten.com') or (url.netloc == 'global.rakuten.com:443') or (url.netloc == 'global.rakuten.com:80'):
	for line in handler:
		if (line.rstrip().find("¥")) != -1: #.find returns the offset, or -1 for not found
			untaggedPrice = re.sub("<[^>]*>","",line.rstrip())
			untaggedPrice = re.sub("                  \(¥ ","",untaggedPrice)
			untaggedPrice = re.sub(",","",untaggedPrice)
			untaggedPrice = re.sub("\)","",untaggedPrice)
			print untaggedPrice
			
#rakuten japan
elif (url.netloc == 'item.rakuten.co.jp') or (url.netloc == 'item.rakuten.co.jp:80') or (url.netloc == 'item.rakuten.co.jp:443'):
	for line in handler:
		if (line.rstrip().find("apprakuten:price")) != -1: #.find returns the offset, or -1 for not found
			untaggedPrice = re.sub('<meta property="apprakuten:price" content="',"",line.rstrip())
			untaggedPrice = re.sub('">',"",untaggedPrice)
			print untaggedPrice
	
 
#print handler.getcode()
#print handler.headers.getheader('content-type')

