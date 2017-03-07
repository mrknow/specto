import sys
import time
import json
import re

sys.path.append('/home/mrknow/Dokumenty/praca/kodi/specto/plugin.video.specto/mylib/')
sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.mrknow.urlresolver/lib/')
#sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.module.youtube.dl/lib/')
#script.module.youtube.dl


import YoutubeDLWrapper

ytdl = YoutubeDLWrapper._getYTDL()
ytdl.clearDownloadParams()

import pprint


from resources.lib.libraries import control
from resources.lib.libraries import client

url='http://thevideo.me/b2hmj4tm6ftb'
url='https://vk.com/video-76470207_456252512'
url='http://thevideo.me/b2hmj4tm6ftb'
url='http://www.auroravid.to/video/c65060bde6c68'
url='https://vk.com/video-76470207_456252512'
url='http://www.movdivx.com/hnaxamhe7d3y'
#mylink = YDStreamExtractor._getYoutubeDLVideo(url, 0, resolve_redirects=False)
#print vars(mylink)
#print YDStreamExtractor.getVideoInfo(url)

try:
    r = ytdl.extract_info(url, download=False)
except YoutubeDLWrapper.DownloadError:
    print "Err"
    exit()

#print r
alina = YoutubeDLWrapper._selectVideoQuality(r, None)

print alina
print alina[0]['xbmc_url']

exit()


import base64

def uncensored(a, b):
    c = ''
    i = 0
    for i, d in enumerate(a):
        e = b[i % len(b) - 1]
        d = int(__jav(d) + __jav(e))
        c += chr(d)

    return base64.b64encode(c)

def __jav(a):
    b = str(a)
    code = ord(b[0])
    if 0xD800 <= code and code <= 0xDBFF:
        c = code
        if len(b) == 1:
            return code
        d = ord(b[1])
        return ((c - 0xD800) * 0x400) + (d - 0xDC00) + 0x10000

    if 0xDC00 <= code and code <= 0xDFFF:
        return code
    return code

ala = uncensored('145651'+'ctiw4zlrn09tau7kqvc153uo','oyz3b0')
print ala
print ala == 'YaOusGiTk+Pi8WfcnOHnqmzWkeSw5aTYk6CurajR'
    #}
    #return encode64(sResult)
