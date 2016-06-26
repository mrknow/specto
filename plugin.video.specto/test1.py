# -*- coding: utf-8 -*-

import random, string, sys
import json,re
sys.path.append('/home/mrknow/Dokumenty/praca/kodi/specto/plugin.video.specto/mylib/')

print ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(25))

from resources.lib.sources import sezonlukdizi_tv

from resources.lib.libraries import client
from resources.lib.libraries import cleantitle
from resources.lib.libraries import control
from resources.lib import resolvers

from resources.lib.resolvers import openload
from resources.lib.sources.watchfree_mv_tv import source
#from resources.lib.sources.animeultima_tv import source

from resources.lib.indexers import movies

#openloadlink = 'https://openload.co/embed/7xKm9d-wcT4'
my = source()
#a = my.get_movie('tt2379713','Spectre','2015')
#control.log('############ DAYT res-1 %s' % a)

#b = my.get_sources(a,'','','')
#control.log('############ DAYT res-2 %s' % b)

#{'tmdb': '60948', 'tvdb': '272644', 'tvshowtitle': '12 Monkeys', 'imdb': 'tt3148266', 'year': '2015', 'action': 'seasons', 'tvrage': '36903'}
#PARAMS: {'tmdb': '1424', 'tvdb': '264586', 'tvshowtitle': 'Orange Is the New Black', 'imdb': 'tt2372162', 'year': '2013', 'action': 'seasons', 'tvrage': '32950'}

imdb = 'tt2372162'
tvdb = '264586'
title = 'Orange Is the New Black'
year = '2015'
data = '2016-05-23'



c=my.get_show('tt3148266',tvdb,'12 Monkeys','2015')
control.log('############ DAYT res-1 %s' % c)
#PARAMS: {'tmdb': '60948', 'episode': '6', 'name': '12 Monkeys S02E06', 'title': 'Immortal', 'tvdb': '272644', 'season': '2', 'tvshowtitle': '12 Monkeys', 'date': '2016-05-23', 'meta': '{"rating": "8.0", "code": "tt3148266", "tmdb": "60948", "imdb": "tt3148266", "year": "2015", "duration": "2700", "plot": "Cole\'s partnership with Ramse is put to the test when they travel back to the 1970s to try to prevent the Twelve from murdering a disturbed Vietnam veteran with a connection to the Witness.", "votes": "47", "thumb": "http://thetvdb.com/banners/episodes/272644/5565074.jpg", "title": "Immortal", "tvdb": "272644", "mpaa": "TV-14", "fanart": "http://thetvdb.com/banners/fanart/original/272644-20.jpg", "season": "2", "status": "Continuing", "poster": "http://thetvdb.com/banners/posters/272644-12.jpg", "tvshowtitle": "12 Monkeys", "studio": "Syfy", "genre": "Mystery / Science-Fiction", "tvrage": "36903", "banner": "http://thetvdb.com/banners/graphical/272644-g5.jpg", "episode": "6", "name": "12 Monkeys S02E06", "premiered": "2016-05-23", "cast": [["Aaron Stanford", ""], ["Amanda Schull", ""], ["Kirk Acevedo", ""], ["Barbara Sukowa", ""], ["Todd Stashwick", ""], ["Emily Hampshire", ""], ["Noah Bean", ""], ["Tom Noonan", ""]], "trailer": "plugin://plugin.video.specto/?action=trailer&name=12+Monkeys"}', 'imdb': 'tt3148266', 'year': '2015', 'action': 'sources', 'tvrage': '36903', 'alter': '0'}
d=my.get_episode(c,imdb,tvdb,title,data,'2','6')
control.log('############ DAYT res-1 %s' % d)
e=my.get_sources(d,'','','')
print ("eee",e)
exit()

#PARAMS: {'tmdb': '62715', 'episode': '7', 'name': 'Dragon Ball Super S04E07', 'title': 'A Message From the Future - Goku Black Invades!',
# 'tvdb': '295068', 'season': '4', 'tvshowtitle': 'Dragon Ball Super', 'date': '2016-06-26',
# 'meta': '{"rating": "7.5", "code": "tt4644488", "tmdb": "62715", "imdb": "tt4644488", "year": "2015", "duration": "1500",
#  "plot": "T  are they? ", "votes": "332", "thumb": "https://walter.trakt.us/images/episodes/002/265/650/screenshots/thumb/4923bc211d.jpg",
# "title": "A Message From the Future - Goku Black Invades!", "tvdb": "295068", "mpaa": "TV-14",
#  "season": "4", "status": "Continuing", "poster": "https://walter.trakt.us/images/shows/000/098/580/posters/medium/32569f3caa.jpg",
# "tvshowtitle": "Dragon Ball Super", "studio": "Fuji TV", "genre": "Animation / Action / Adventure / Mystery",
# "tvrage": "48862", "banner": "https://walter.trakt.us/images/shows/000/098/580/banners/original/dc596601d3.jpg",
# "episode": "7", "name": "Dragon Ball Super S04E07", "premiered": "2016-06-26",
# "fanart": "https://walter.trakt.us/images/shows/000/098/580/fanarts/original/fab7afcb95.jpg",
# "trailer": "plugin://plugin.video.specto/?action=trailer&name=Dragon+Ball+Super"}', 'imdb': 'tt4644488',
# 'year': '2015', 'action': 'sources', 'tvrage': '48862', 'alter': '0'}

tvdb='295068'
title = 'Dragon Ball Super'
imdb='tt4644488'

c=my.get_show(imdb,tvdb,title,'2015')
control.log('############ get_show  res-1 %s' % c)
d=my.get_episode(c,imdb,tvdb,title,data,'4','7')
control.log('############ get_episode res-1 %s' % d)
e=my.get_sources(d,'','','')
print ("get_sources",e)
exit()

#url = 'http://ok.ru/video/86215559923'
#print resolvers.request(url)



"""
src='http://dayt.se/forum/search.php?do=process'

post={'titleonly':1,'securitytoken':'guest','do':'process','q':'London + Has Fallen','B1':''}
result = client.source(src, post=post)
result = client.parseDOM(result, 'h3', attrs={'class': 'searchtitle'})
result = [(client.parseDOM(i, 'a', attrs={'class': 'title'}, ret='href')[0],client.parseDOM(i, 'a', attrs={'class': 'title'})[0]) for i in result]
control.log('############ DAYT res-1 %s' % result)
result = [i for i in result if title in cleantitle.movie(i[1])]
result = [i[0] for i in result if any(x in i[1] for x in years)][0]
result = re.compile('(.+?)(?:&amp)').findall(result)[0]

control.log('############ DAYT res-1 %s' % result)



exit()
result = client.parseDOM(result, 'iframe', ret='src')
result = [i for i in result if 'pasep' in i][0]

control.log('############ DAYT res-1 %s' % result)
result = client.source(result)
result = client.parseDOM(result, 'iframe', ret='src')[0]
result = client.source(result)
result = client.parseDOM(result, 'iframe', ret='src')[0]
control.log('############ DAYT res-2 %s' % result)
#control.log('############ DAYT res-2 %s' % resolvers.request(result))


result10 = client.parseDOM(result2, 'div', attrs = {'id': '5throw'})[0]
result10 = client.parseDOM(result10, 'a', attrs = {'rel': 'nofollow'}, ret='href')
for i in result10:
    print resolvers.request(i)


control.log('############ DAYT res-2 %s' % result10)
https://cloclo9.cldmail.ru/2dfVwUu76bo9TkKgZDPE/G/GT9F/FoCczQknq?key=9170c586eac96c6fbe53d3b77bf5d59b1ac4538a


src='https://cloud.mail.ru/public/GT9F/FoCczQknq'
src='https://cloud.mail.ru/public/6i3K/8aL4QRjZU'
#print resolvers.request(src)

result20 = client.source(src)
title= client.parseDOM(result20, 'title')
print title

vid = src.split('public')[-1]
token  = re.compile('"tokens":{"download":"([^"]+)"}').findall(result20)[0]
weblink = re.compile('"weblink_get":\[{"count":\d+,"url":"([^"]+)"}\]').findall(result20)[0]
print("Dane",token,weblink,vid)


if len(token)>0 and len(weblink)>0:
    url = weblink + vid + '?key='+token

    #result20 = json.loads(result20)
    control.log('############ DAYT res-2 %s' % url)
    #https://cloclo9.cldmail.ru/2dfVwUu76bo9TkKgZDPE/G/GT9F/FoCczQknq?key=9170c586eac96c6fbe53d3b77bf5d59b1ac4538a






src=' http://dayt.se/forum/forumdisplay.php?356-The-Flash'
mytitile = cleantitle.tv('S%02dE%02d' % (2,19)).lower()
control.log('############ DAYT mytitle %s' % mytitile)


result = client.source(src)
result = client.parseDOM(result, 'h3', attrs={'class': 'threadtitle'})
result = [(client.parseDOM(i, 'a', attrs={'class': 'title'}, ret='href')[0],client.parseDOM(i, 'a', attrs={'class': 'title'})[0]) for i in result]
result = [i for i in result if mytitile in i[1].lower()]
result = [(re.compile('(.+?)(?:&amp)').findall(i[0]), i[1]) for i in result][0][0]
control.log('############ DAYT res-2 %s' % result[0])

    #a = client.parseDOM(i, 'a', attrs={'class': 'title'})[0]
    #a1 = client.parseDOM(i, 'a', attrs={'class': 'title'},ret='href')[0]

    #control.log('############ DAYT res-20 %s' % a)
    #control.log('############ DAYT res-21 %s' % a1)
"""