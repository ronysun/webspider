#codeing: utf-8

"""

"""
import urllib2
import re
import sys
import chardet

typeEncode = sys.getfilesystemencoding()
print typeEncode
request = urllib2.Request('https://movie.douban.com/top250')
try:
    response = urllib2.urlopen(request)
    cache = response.read()
    html = cache.decode('utf-8','ignore').encode(typeEncode)
    regex = r'<span.*?class="title">(.*?)</span>'
    # menu = re.findall(regex, html)
    menu = re.findall(regex, html)
    for movieName in menu:
        print movieName.decode('utf-8')
        pass
except urllib2.URLError, e:
    print e.reason
