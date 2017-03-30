import sys
import time
import json
import re

sys.path.append('/home/mrknow/Dokumenty/praca/kodi/specto/plugin.video.specto/mylib/')
sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.mrknow.urlresolver/lib/')
#sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.module.youtube.dl/lib/')
#script.module.youtube.dl

r3 =  [(u'http://onwatchseries.to/episode/elementary_s5_e16.html', u'Fidelity (2)', u'2017-03-12'), (u'http://onwatchseries.to/episode/elementary_s5_e15.html', u'Wrong Side of the Road (1)', u'2017-03-05'), (u'http://onwatchseries.to/episode/elementary_s5_e14.html', u'Rekt in Real Life', u'2017-02-19'), (u'http://onwatchseries.to/episode/elementary_s5_e13.html', u'Over a Barrel', u'2017-01-29'), (u'http://onwatchseries.to/episode/elementary_s5_e12.html', u'Crowned Clown, Downtown Brown', u'2017-01-15'), (u'http://onwatchseries.to/episode/elementary_s5_e11.html', u'Be My Guest', u'2017-01-08'), (u'http://onwatchseries.to/episode/elementary_s5_e10.html', u'Pick Your Poison', u'2016-12-18'), (u'http://onwatchseries.to/episode/elementary_s5_e9.html', u'It Serves You Right to Suffer', u'2016-12-11'), (u'http://onwatchseries.to/episode/elementary_s5_e8.html', u'How the Sausage Is Made', u'2016-11-27'), (u'http://onwatchseries.to/episode/elementary_s5_e7.html', u'Bang Bang Shoot Chute', u'2016-11-20'), (u'http://onwatchseries.to/episode/elementary_s5_e6.html', u'Ill Tidings', u'2016-11-13'), (u'http://onwatchseries.to/episode/elementary_s5_e5.html', u'To Catch a Predator Predator', u'2016-11-06'), (u'http://onwatchseries.to/episode/elementary_s5_e4.html', u'Henny Penny the Sky is Falling', u'2016-10-30'), (u'http://onwatchseries.to/episode/elementary_s5_e3.html', u'Render, and Then Seize Her', u'2016-10-23'), (u'http://onwatchseries.to/episode/elementary_s5_e2.html', u'Worth Several Cities', u'2016-10-16'), (u'http://onwatchseries.to/episode/elementary_s5_e1.html', u'Folie \xe0 Deux', u'2016-10-02'), (u'http://onwatchseries.to/episode/elementary_s4_e24.html', u'A Difference in Kind', u'2016-05-08'), (u'http://onwatchseries.to/episode/elementary_s4_e23.html', u'The Invisible Hand', u'2016-05-01'), (u'http://onwatchseries.to/episode/elementary_s4_e22.html', u'Turn It Upside Down', u'2016-04-24'), (u'http://onwatchseries.to/episode/elementary_s4_e21.html', u'Ain&#039;t Nothing Like the Real Thing', u'2016-04-17'), (u'http://onwatchseries.to/episode/elementary_s4_e20.html', u'Art Imitates Art', u'2016-04-10'), (u'http://onwatchseries.to/episode/elementary_s4_e19.html', u'All In', u'2016-04-10'), (u'http://onwatchseries.to/episode/elementary_s4_e18.html', u'Ready or Not', u'2016-03-27'), (u'http://onwatchseries.to/episode/elementary_s4_e17.html', u'You&#039;ve Got Me, Who&#039;s Got You?', u'2016-03-20'), (u'http://onwatchseries.to/episode/elementary_s4_e16.html', u'Hounded', u'2016-03-10'), (u'http://onwatchseries.to/episode/elementary_s4_e15.html', u'Up to Heaven and Down to Hell', u'2016-03-03'), (u'http://onwatchseries.to/episode/elementary_s4_e14.html', u'Who Is That Masked Man?', u'2016-02-25'), (u'http://onwatchseries.to/episode/elementary_s4_e13.html', u'A Study in Charlotte', u'2016-02-18'), (u'http://onwatchseries.to/episode/elementary_s4_e12.html', u'A View With a Room', u'2016-02-11'), (u'http://onwatchseries.to/episode/elementary_s4_e11.html', u'Down Where the Dead Delight', u'2016-02-04'), (u'http://onwatchseries.to/episode/elementary_s4_e10.html', u'Alma Matters', u'2016-01-28'), (u'http://onwatchseries.to/episode/elementary_s4_e9.html', u'Murder Ex Machina', u'2016-01-21'), (u'http://onwatchseries.to/episode/elementary_s4_e8.html', u'A Burden of Blood', u'2016-01-14'), (u'http://onwatchseries.to/episode/elementary_s4_e7.html', u'Miss Taken', u'2016-01-07'), (u'http://onwatchseries.to/episode/elementary_s4_e6.html', u'The Cost of Doing Business', u'2015-12-17'), (u'http://onwatchseries.to/episode/elementary_s4_e5.html', u'The Games Underfoot', u'2015-12-10'), (u'http://onwatchseries.to/episode/elementary_s4_e4.html', u'All My Exes Live in Essex', u'2015-11-26'), (u'http://onwatchseries.to/episode/elementary_s4_e3.html', u'Tag, You&#039;re Me', u'2015-11-19'), (u'http://onwatchseries.to/episode/elementary_s4_e2.html', u'Evidence of Things Not Seen', u'2015-11-12'), (u'http://onwatchseries.to/episode/elementary_s4_e1.html', u'The Past Is Parent', u'2015-11-05'), (u'http://onwatchseries.to/episode/elementary_s4_e0.html', u'Recap S04', u'2015-09-13'), (u'http://onwatchseries.to/episode/elementary_s3_e24.html', u'A Controlled Descent', u'2015-05-14'), (u'http://onwatchseries.to/episode/elementary_s3_e23.html', u'Absconded', u'2015-05-07'), (u'http://onwatchseries.to/episode/elementary_s3_e22.html', u'The Best Way Out Is Always Through', u'2015-04-30'), (u'http://onwatchseries.to/episode/elementary_s3_e21.html', u'Under My Skin', u'2015-04-23'), (u'http://onwatchseries.to/episode/elementary_s3_e20.html', u'A Stitch in Time', u'2015-04-16'), (u'http://onwatchseries.to/episode/elementary_s3_e19.html', u'One Watson, One Holmes', u'2015-04-09'), (u'http://onwatchseries.to/episode/elementary_s3_e18.html', u'The View From Olympus', u'2015-04-02'), (u'http://onwatchseries.to/episode/elementary_s3_e17.html', u'T-Bone and the Iceman', u'2015-03-12'), (u'http://onwatchseries.to/episode/elementary_s3_e16.html', u'For All You Know', u'2015-03-05'), (u'http://onwatchseries.to/episode/elementary_s3_e15.html', u'When Your Number&#039;s Up', u'2015-02-19'), (u'http://onwatchseries.to/episode/elementary_s3_e14.html', u'The Female of the Species', u'2015-02-12'), (u'http://onwatchseries.to/episode/elementary_s3_e13.html', u'Hemlock', u'2015-02-05'), (u'http://onwatchseries.to/episode/elementary_s3_e12.html', u'The One That Got Away (2)', u'2015-01-29'), (u'http://onwatchseries.to/episode/elementary_s3_e11.html', u'The Illustrious Client (1)', u'2015-01-22'), (u'http://onwatchseries.to/episode/elementary_s3_e10.html', u'Seed Money', u'2015-01-15'), (u'http://onwatchseries.to/episode/elementary_s3_e9.html', u'The Eternity Injection', u'2015-01-08'), (u'http://onwatchseries.to/episode/elementary_s3_e8.html', u'End of Watch', u'2014-12-18'), (u'http://onwatchseries.to/episode/elementary_s3_e7.html', u'The Adventure of the Nutmeg Concoction', u'2014-12-11'), (u'http://onwatchseries.to/episode/elementary_s3_e6.html', u'Terra Pericolosa', u'2014-12-04'), (u'http://onwatchseries.to/episode/elementary_s3_e5.html', u'Rip Off', u'2014-11-27'), (u'http://onwatchseries.to/episode/elementary_s3_e4.html', u'Bella', u'2014-11-20'), (u'http://onwatchseries.to/episode/elementary_s3_e3.html', u'Just a Regular Irregular', u'2014-11-13'), (u'http://onwatchseries.to/episode/elementary_s3_e2.html', u'The Five Orange Pipz', u'2014-11-06'), (u'http://onwatchseries.to/episode/elementary_s3_e1.html', u'Enough Nemesis to Go Around', u'2014-10-30'), (u'http://onwatchseries.to/episode/elementary_s2_e24.html', u'The Grand Experiment', u'2014-05-15'), (u'http://onwatchseries.to/episode/elementary_s2_e23.html', u'Art in the Blood', u'2014-05-08'), (u'http://onwatchseries.to/episode/elementary_s2_e22.html', u'Paint It Black', u'2014-05-01'), (u'http://onwatchseries.to/episode/elementary_s2_e21.html', u'The Man With the Twisted Lip', u'2014-04-24'), (u'http://onwatchseries.to/episode/elementary_s2_e20.html', u'No Lack of Void', u'2014-04-10'), (u'http://onwatchseries.to/episode/elementary_s2_e19.html', u'The Many Mouths of Aaron Colville', u'2014-04-03'), (u'http://onwatchseries.to/episode/elementary_s2_e18.html', u'The Hound of the Cancer Cells', u'2014-03-13'), (u'http://onwatchseries.to/episode/elementary_s2_e17.html', u'Ears to You', u'2014-03-06'), (u'http://onwatchseries.to/episode/elementary_s2_e16.html', u'The One Percent Solution', u'2014-02-27'), (u'http://onwatchseries.to/episode/elementary_s2_e15.html', u'Corpse de Ballet', u'2014-02-06'), (u'http://onwatchseries.to/episode/elementary_s2_e14.html', u'Dead Clade Walking', u'2014-01-30'), (u'http://onwatchseries.to/episode/elementary_s2_e13.html', u'All in the Family', u'2014-01-09'), (u'http://onwatchseries.to/episode/elementary_s2_e12.html', u'The Diabolical Kind', u'2014-01-02'), (u'http://onwatchseries.to/episode/elementary_s2_e11.html', u'Internal Audit', u'2013-12-12'), (u'http://onwatchseries.to/episode/elementary_s2_e10.html', u'Tremors', u'2013-12-05'), (u'http://onwatchseries.to/episode/elementary_s2_e9.html', u'On the Line', u'2013-11-21'), (u'http://onwatchseries.to/episode/elementary_s2_e8.html', u'Blood Is Thicker', u'2013-11-14'), (u'http://onwatchseries.to/episode/elementary_s2_e7.html', u'The Marchioness', u'2013-11-07'), (u'http://onwatchseries.to/episode/elementary_s2_e6.html', u'An Unnatural Arrangement', u'2013-10-31'), (u'http://onwatchseries.to/episode/elementary_s2_e5.html', u'Ancient History', u'2013-10-24'), (u'http://onwatchseries.to/episode/elementary_s2_e4.html', u'Poison Pen', u'2013-10-17'), (u'http://onwatchseries.to/episode/elementary_s2_e3.html', u'We Are Everyone', u'2013-10-10'), (u'http://onwatchseries.to/episode/elementary_s2_e2.html', u'Solve for X', u'2013-10-03'), (u'http://onwatchseries.to/episode/elementary_s2_e1.html', u'Step Nine', u'2013-09-26'), (u'http://onwatchseries.to/episode/elementary_s1_e24.html', u'Heroine (2)', u'2013-05-16'), (u'http://onwatchseries.to/episode/elementary_s1_e23.html', u'The Woman (1)', u'2013-05-16'), (u'http://onwatchseries.to/episode/elementary_s1_e22.html', u'Risk Management', u'2013-05-09'), (u'http://onwatchseries.to/episode/elementary_s1_e21.html', u'A Landmark Story', u'2013-05-02'), (u'http://onwatchseries.to/episode/elementary_s1_e20.html', u'Dead Man&#039;s Switch', u'2013-04-25'), (u'http://onwatchseries.to/episode/elementary_s1_e19.html', u'Snow Angels', u'2013-04-04'), (u'http://onwatchseries.to/episode/elementary_s1_e18.html', u'Deja Vu All Over Again', u'2013-03-14'), (u'http://onwatchseries.to/episode/elementary_s1_e17.html', u'Possibility Two', u'2013-02-21'), (u'http://onwatchseries.to/episode/elementary_s1_e16.html', u'Details', u'2013-02-14'), (u'http://onwatchseries.to/episode/elementary_s1_e15.html', u'A Giant Gun, Filled with Drugs', u'2013-02-07'), (u'http://onwatchseries.to/episode/elementary_s1_e14.html', u'The Deductionist', u'2013-02-03'), (u'http://onwatchseries.to/episode/elementary_s1_e13.html', u'The Red Team', u'2013-01-31'), (u'http://onwatchseries.to/episode/elementary_s1_e12.html', u'M.', u'2013-01-10'), (u'http://onwatchseries.to/episode/elementary_s1_e11.html', u'Dirty Laundry', u'2013-01-03'), (u'http://onwatchseries.to/episode/elementary_s1_e10.html', u'The Leviathan', u'2012-12-13'), (u'http://onwatchseries.to/episode/elementary_s1_e9.html', u'You Do It to Yourself', u'2012-12-06'), (u'http://onwatchseries.to/episode/elementary_s1_e8.html', u'The Long Fuse', u'2012-11-29'), (u'http://onwatchseries.to/episode/elementary_s1_e7.html', u'One Way to Get Off', u'2012-11-15'), (u'http://onwatchseries.to/episode/elementary_s1_e6.html', u'Flight Risk', u'2012-11-08'), (u'http://onwatchseries.to/episode/elementary_s1_e5.html', u'Lesser Evils', u'2012-11-01'), (u'http://onwatchseries.to/episode/elementary_s1_e4.html', u'The Rat Race', u'2012-10-25'), (u'http://onwatchseries.to/episode/elementary_s1_e3.html', u'Child Predator', u'2012-10-18'), (u'http://onwatchseries.to/episode/elementary_s1_e2.html', u'While You Were Sleeping', u'2012-10-04'), (u'http://onwatchseries.to/episode/elementary_s1_e1.html', u'Pilot', u'2012-09-27'), (u"' + url + '", u"' + shortName + '", u'0000-00-00')]
#(u'http://onwatchseries.to/episode/elementary_s4_e3.html', u'Tag, You&#039;re Me', u'2015-11-19')

for i in r3:
    if 's4_e3' in i[0]:
        print "YES", i



exit()

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
