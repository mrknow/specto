# -*- coding: utf-8 -*-

import random
import string
import sys

sys.path.append('/home/mrknow/Dokumenty/praca/kodi/specto/plugin.video.specto/mylib/')
sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.mrknow.urlresolver2/lib/')

from resources.lib.libraries import client
from resources.lib.libraries import cleantitle

import urllib
import sys, json

sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/plugin.video.mrknow/mylib/')
sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.mrknow.urlresolver/lib/')



import re
import urllib

query = 'The Nice Guys'

print cleantitle.query10(query)
exit()


result = client.request('http://www.pelispedia.tv/pelicula/the-nice-guys/').decode('gb18030').encode('utf-8')
result = client.parseDOM(result,'div',attrs={'id':'player'})[0]
#print result
result = [re.findall('(.*?)<a',client.parseDOM(result,'center')[0])[0].strip(),re.findall('>\((.*?)\)</a>',client.parseDOM(result,'center')[0])[0]]
print result
#result = client.parseDOM(result,'a')

exit()
