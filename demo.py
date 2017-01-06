#codeing: utf-8

import urllib2
import re
import sys
import chardet

typeEncode = sys.getfilesystemencoding()
request = urllib2.Request('http://www.dytt8.net/html/gndy/rihan/index.html')
try:
    response = urllib2.urlopen(request)
    cache = response.read()
    infoencode = chardet.detect(cache).get('encoding','utf-8')
    print infoencode
    html = cache.decode('gbk','ignore').encode(typeEncode)
    #phtml = '<strong>.*</strong>'
    phtml = '.*index.html">.*</a>.*'
    menu = re.findall(phtml, html)
    # menuEncode = chardet.detect(menu).get("encoding","utf-8")
    menu = menu.encode('utf-8')
    print '%s' % menu
except urllib2.URLError, e:
    print e.reason
