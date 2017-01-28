# -*- coding: utf-8 -*-

import random
import re
import string
import sys

sys.path.append('/home/mrknow/Dokumenty/praca/kodi/specto/plugin.video.specto/mylib/')

#print ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(25))


import time, datetime
from resources.lib.libraries import client2
from resources.lib.libraries import client
from resources.lib.libraries import ntptime

#mynow = int(str(int(time.mktime(datetime.datetime.now().timetuple()))))
#print "Exp_Now", mynow

print 'ExpWhen', ntptime.checkDate()

s= '__cfduid=d4a8b611c1d4b33abacf8d245ec3892d61485465542; PHPSESSID=249b8gc4bfrrbcp754uaaqvh66; history_watch=a%3A1%3A%7Bi%3A0%3Bs%3A109%3A%22%3Ca+href%3D%22http%3A%2F%2Falltube.tv%2Ffilm%2Fvaiana-skarb-oceanu-moana-2016%2F37136%22%3EVaiana%3A+Skarb+oceanu+%2F+Moana+%282016%29%3C%2Fa%3E%22%3B%7D'
import re,urllib
print  urllib.unquote(s).decode('utf8')
#print s.split(';')
a =  re.findall('(.*?)=(.*?);', urllib.unquote(s))

#exit()

q = {k.strip():v for k,v in re.findall(r'(.*?)=(.*?);', urllib.unquote(s))}
print q


exit()


#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)



def daytse_tvshows(con):
    a=1



def daytse_movies(dbname):
    con = lite.connect(dbname)
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS movies")
    #cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
    #cur.execute("CREATE TABLE movies (title TEXT, link TEXT, quality TEXT, UNIQUE (link))")

    for j in range(1,2):
        print'------- %s ' % j
        src = 'http://dayt.se/movies/index.php?&page=%s' % j
        result = ''
        result = client2.http_get(src).decode('windows-1256').encode('utf8')
        result = client.parseDOM(result, 'table', attrs={'class': 'topic_table'})
        for i in result:
            print '-------------------------'
            #print i
            print client.parseDOM(i, 'img', attrs={'class': 'image'}, ret='alt')[0]
            print  client.parseDOM(i, 'a', attrs={'target': '_self'},  ret='href')[1]

        #result = [(client.parseDOM(i, 'img', attrs={'class': 'image'}, ret='alt')[0],
        #       client.parseDOM(i, 'a', attrs={'target': '_self'},  ret='href')[0],
        #       re.findall('Quality: (\d+).*</pre>', i)[0]) for i in result]
        #cur.executemany("INSERT INTO movies VALUES(?, ?, ?)", result)
    con.commit()
    con.close()


def daytse_get_movies(dbname, title):
    con = lite.connect(dbname)
    cur = con.cursor()
    cur.execute("SELECT * FROM movies WHERE title like '%"+title.lower()+"%'")
    #result = cur.fetchone()
    result = cur.fetchone()
    #result = eval(result[0].encode('utf-8'))

    print result
    con.close()

daytse_movies('/home/mrknow/Dokumenty/praca/kodi/MyScripts/Specto/daytse1.db')
#https://raw.githubusercontent.com/mrknow/database/master/daytse1.db
#aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL21ya25vdy9kYXRhYmFzZS9tYXN0ZXIvZGF5dHNlMS5kYg==
#daytse_get_movies('/home/mrknow/Dokumenty/praca/kodi/MyScripts/Specto/daytse1.db','Eye in the Sky')