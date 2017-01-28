# -*- coding: utf-8 -*-

import sys

sys.path.append('/home/mrknow/Dokumenty/praca/kodi/specto/plugin.video.specto/mylib/')
sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.mrknow.urlresolver2/lib/')

mytab = ['oboom', 'rapidgator', 'uploaded', '180upload', 'allvid', 'clicknupload', 'ipithos', 'ishared', 'mightyupload', 'mrfile', 'openload', 'primeshare', 'promptfile', 'skyvids', 'turbovideos', 'tusfiles', 'uptobox', 'v-vids', 'vidlockers', 'zettahost', 'watch1080p', 'allmyvideos', 'nosvideo', 'divxstage', 'noslocker', 'cloudtime', 'cloudzilla', 'divxpress', 'letwatch', 'putstream', 'streamcloud', 'streamin', 'up2stream', 'uploadc', 'zalaa', 'vidspot', 'vidto', 'xvidstage', 'youtube', 'zstream', 'youwatch', 'flashx', 'thevideobee', 'auroravid', 'vshare', 'shared', 'bestreams', 'daclips', 'exashare', 'fastvideo', 'faststream', 'filehoot', 'filenuke', 'sharesix', 'gorillavid', 'movdivx', 'movpod', 'movshare', 'novamov', 'nowvideo', 'realvid', 'sharerepo', 'stagevu', 'thefile', 'thevideo', 'vidbull', 'videoweed', 'vidzi', 'watchers.to', 'videosky.to', 'vidup.org', 'mp4stream.com', 'openload.io', 'openload.co', 'video.tt', 'vidcrazy.net', 'uploadcrazy.net', 'fastplay.sx', 'fastplay.cc', 'cda.pl', 'www.cda.pl', 'ebd.cda.pl', 'exashare.com', 'uame8aij4f.com', 'yahmaib3ai.com', 'daclips.in', 'daclips.com', 'videohut.to', 'kingfiles.net', 'bestreams.net', 'zettahost.tv', 'videoboxer.co', 'rapidvideo.com', 'byzoo.org', 'playpanda.net', 'videozoo.me', 'videowing.me', 'easyvideo.me', 'play44.net', 'playbb.me', 'video44.net', 'promptfile.com', 'bitvid.sx', 'videoweed.es', 'videoweed.com', 'allvid.ch', 'watchvideo.us', 'watchvideo2.us', 'watchvideo3.us', 'watchvideo4.us', 'watchvideo5.us', 'watchvideo6.us', 'watchvideo7.us', 'watchvideo8.us', 'watchvideo9.us', 'watchvideo10.us', 'uploadx.org', 'vshare.eu', 'googlevideo.com', 'googleusercontent.com', 'get.google.com', 'plus.google.com', 'googledrive.com', 'drive.google.com', 'docs.google.com', 'vid.me', 'divxstage.eu', 'divxstage.net', 'divxstage.to', 'cloudtime.to', 'idowatch.net', 'uploadc.com', 'uploadc.ch', 'zalaa.com', 'upload.af', 'xvidstage.com', 'vidbull.com', 'speedvideo.net', 'novamov.com', 'auroravid.to', 'playwire.com', 'www.playhd.video', 'www.playhd.fo', 'rapidvideo.ws', 'youwatch.org', 'chouhaa.info', 'flashx.tv', 'ok.ru', 'odnoklassniki.ru', 'thevideo.me', 'auengine.com', 'thevideobee.to', 'vidspot.net', 'cloud.mail.ru', 'vidzi.tv', 'shared2.me', 'vid.ag', 'mersalaayitten.com', 'mersalaayitten.co', 'mersalaayitten.us', 'stagevu.com', 'shared.sx', 'vidgg.to', 'www.vid.gg', 'streamin.to', 'gorillavid.in', 'gorillavid.com', 'sharesix.com', 'playu.net', 'playu.me', 'vidio.sx', 'vodlocker.com', 'weshare.me', 'ishared.eu', 'allmyvideos.net', 'letwatch.us', 'letwatch.to', 'vidshare.us', 'anyfiles.pl', 'videomega.tv', 'filehoot.com', 'facebook.com', 'thevideos.tv', 'zstream.to', 'jetload.tv', 'sharerepo.com', 'cloudzilla.to', 'neodrive.co', 'hugefiles.net', 'nosvideo.com', 'noslocker.com', 'movdivx.com', 'usersfiles.com', 'movshare.net', 'wholecloud.net', 'mightyupload.com', 'uptobox.com', 'uptostream.com', 'dailymotion.com', 'videoraj.ec', 'videoraj.eu', 'videoraj.sx', 'videoraj.ch', 'videoraj.com', 'videoraj.to', 'videoraj.co', 'videorev.cc', 'mp4upload.com', 'cloudy.ec', 'cloudy.eu', 'cloudy.sx', 'cloudy.ch', 'cloudy.com', 'yourupload.com', 'yucache.net', 'ecostream.tv', 'clicknupload.com', 'clicknupload.me', 'clicknupload.link', 'castamp.com', 'myvidstream.net', 'vidup.me', 'streamcloud.eu', 'youtube.com', 'youtu.be', 'tusfiles.net', 'videowood.tv', 'filenuke.com', 'grifthost.com', 'veoh.com', 'trollvid.net', 'mp4edge.com', 'movpod.net', 'movpod.in', 'vidto.me', 'crunchyroll.com', 'teramixer.com', 'speedplay.xyz', 'speedplay.us', 'speedplay1.site', 'speedplay.pw', 'speedplay3.pw', 'speedplayy.site', 'up2stream.com', 'mail.ru', 'my.mail.ru', 'videoapi.my.mail.ru', 'api.video.mail.ru', 'vimeo.com', 'userscloud.com', 'tune.pk', 'rutube.ru', 'megamp4.net', 'vivo.sx', 'nowvideo.eu', 'nowvideo.ch', 'nowvideo.sx', 'nowvideo.co', 'nowvideo.li', 'nowvideo.fo', 'nowvideo.at', 'nowvideo.ec', 'vkpass.com', 'www.filmshowonline.net', 'filepup.net', 'vshare.io', 'vk.com']

host = 'streamin.to'
if not host in mytab:
    print 'NIE MA'
else:
    print 'Jest'


"""
def __get_token(data):
    result = 0
    for key in data:
        i = list(range(0, 256))
        if not key.startswith('_'):
            n = 0
            o = 0
            #            n += ord(c) * t + len(data[key]) + i
            for l in range(0, 256):
                #print l
                n = (n + i[l] + ord(key[l % len(key)]))% 256
                r = i[l]
                i[l] = i[n]
                i[n] = r
            n=0
            for u in range(0, len(data[key])):
                l = u+1
                n = (n + i[l]) % (256)
                r = i[l]
                i[l] = i[n]
                i[n] = r
                o += ord(data[key][u]) ^ (i[(i[l]+ i[n]) % 256]) + u

            print ">>>>>>>>>", o
            result += o
    print "RES", result
"""

def __get_token(data):
    index1 = 0
    for index10 in data:
        lista = list(range(0, 256))
        if not index10.startswith('_'):
            print "index10",index10
            zmienna_o = 0
            zmienna_u = 0
            for j in range(0, 256):
                zmienna_o = (zmienna_o + lista[j] + ord(index10[j % len(index10)])) % 256
                index6 = lista[j]
                lista[j] = lista[zmienna_o]
                lista[zmienna_o] = index6
            print lista
            zmienna_o = 0
            for k in range(0, len(data[index10])):
                j = k + 1  # line:15
                zmienna_o = (zmienna_o + lista[j]) % (256)
                index6 = lista[j]
                lista[j] = lista[zmienna_o]
                lista[zmienna_o] = index6
                zmienna_u += ord(data[index10][k]) ^ (lista[(lista[j] + lista[zmienna_o]) % 256]) + k
            index1 += zmienna_u
    return {'_': str(index1)}
#UN.O(e[n](d), a[UN.l(a[c], a[o]) % (1 * r)] + d);

# e9015584e6a44b14988f13e2298bcbf9

#http://fmovies.to/grabber-api/?ts=1481364000&_=38636&id=902kxx&token=IFmEgNFcXOoGvJbTmZ6BOB6E0M54yvgN5keGw7RT0xtD7ZkduiLxDugB8oXM6%2FmmmFmkAWWk%2FNik%40C54vgoBDhnrIEqtaKUUG19AspVhTpePHxPNnulmTcZKk9w%3D&options=LhyCgccIA7AF%409rJhcmTKFDS2t4zyugor1OVyKgG%2FU4QltZJgwjbWMpb4qHf1bvXxwfEWgXnn5%2Ftm2JN&mobile=0

#1481385600

import time

mydata = {'id':'oyly', 'aa':'1'}
mydata = {"id": "902kxx", "update": "0", "film": "oyly"}
mydata= {"ts": "1481385600"}
print   str(int(time.time()))
print   str(((int(time.time())/3600)*3600))
print "1481385600"

print "ALA"
print __get_token(mydata)


exit()

# encrypted with www.stringencrypt.com (v1.0.0) [Python]
# myString = "Encryption in Python"
myString = [0xBB7A, 0xBBD0, 0xBB5E, 0xBBCE, 0xBBC2, 0xBBCA, 0xBB57, 0xBB51,
            0xBB58, 0xBB58, 0xBC17, 0xBB6D, 0xBB6B, 0xBC12, 0xBB63, 0xBB59,
            0xBB59, 0xBB66, 0xBB62, 0xBB62]

for uVqes in range(20):
    JzEXf = myString[uVqes]
    JzEXf -= 0xF251
    JzEXf ^= uVqes
    JzEXf ^= 0xE0BE
    JzEXf += uVqes
    JzEXf -= 0x2952
    JzEXf ^= uVqes
    myString[uVqes] = JzEXf

myString = ''.join(chr(JzEXf & 0xFFFF) for JzEXf in myString)

del uVqes, JzEXf

print(myString)
exit()
#print ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(25))

from resources.lib.libraries import control


def testing(my):
    a = my.get_movie('tt3799694', 'The Nice Guys', '2016')
    # a = my.get_movie('tt3110958','Now You See Me 2','2016')
    # a = my.get_movie('tt2948356','Zootopia','2016')
    # a = my.get_movie('tt5377604','Pitbull. New Order','2016')
    # control.log('############ DAYT res-1 %s' % a)

    b = my.get_sources(a, '', '', '')
    print('############ DAYT get_sources', b)
    for i in b:
        try:
            c = my.resolve(i['url'])
            control.log('############ DAYT res-3 %s' % c)
        except:
            pass


from resources.lib.sources.fmovies_mv_tv import source
my = source()
print "FMOVIES"
testing(my)

from resources.lib.sources.rainierland_mv import source
my = source()
print "RAINERLAND"
testing(my)

from resources.lib.sources.pelispedia_mv_tv import source
my = source()
print "PELISPEDIZ"

testing(my)





