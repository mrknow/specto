# -*- coding: utf-8 -*-

import sys

sys.path.append('/home/mrknow/Dokumenty/praca/kodi/specto/plugin.video.specto/mylib/')
sys.path.append('/home/mrknow/Dokumenty/praca/kodi/filmkodi/script.mrknow.urlresolver/lib/')



from resources.lib.libraries import control

"""
url = 'http://openload.co/embed/7wlGOdWQnT4'
url = 'https://openload.co/embed/CFDSAsN4Zeo/Animal.Kingdom.US.S01E06.720p.HDTV.X264-DIMENSION.mp4'
url ='http://openload.co/embed/ExatdBfcJ38'
url = 'https://openload.co/embed/rZ04_L_uRuU'
#url = 'https://openload.co/embed/rZ04_L_uRuU'
#url = 'https://cloud.mail.ru/public/5TFB/spjSFgKSo'
#url = 'http://www.cda.pl/video/10603989f'
#url = 'http://www.cda.pl/video/1852188d/Ultimatum-Bournea---The-Bourne-Ultimatum-HD?wersja=720p'


url='http://shared.sx/8addffca7f'
url = 'http://openload.co/embed/JlSTfXTluk8'
import urlresolver9
z = False
hmf = urlresolver9.HostedMediaFile(url, include_disabled=True, include_universal=False)
print hmf
if hmf:
    print 'yay! we can resolve this one'
    z = hmf.resolve()
else:
    print 'dupa'
print("URL", z)

exit()

"""
def getmovie(myclass):
    a = myclass.get_movie('tt3799694', 'The Nice Guys', '2016')
    #a = my.get_movie('tt3110958','Mechanic: Resurrection','2016')
    #a = myclass.get_movie('tt2948356','Zootopia','2016')
    # a = my.get_movie('tt5377604','Pitbull. New Order','2016')
    control.log('############ DAYT res-1 %s' % a)

    b = myclass.get_sources(a, '', '', '')
    print('>>>>>>>>>>>>>>>>  get_sources', len(b), b)
    #print('>>>>>>>>>>>>>>>>  get_sources', len(b))
    #print('>>>>>>>>>>>>>>>>  get_sources', len(b))


def getserial(myclass):
    c=myclass.get_show(imdb,tvdb,title,year)
    control.log('############ DAYT res-1 %s' % c)
    #exit()
    #PARAMS: {'tmdb': '60948', 'episode': '6', 'name': '12 Monkeys S02E06', 'title': 'Immortal', 'tvdb': '272644', 'season': '2', 'tvshowtitle': '12 Monkeys', 'date': '2016-05-23', 'meta': '{"rating": "8.0", "code": "tt3148266", "tmdb": "60948", "imdb": "tt3148266", "year": "2015", "duration": "2700", "plot": "Cole\'s partnership with Ramse is put to the test when they travel back to the 1970s to try to prevent the Twelve from murdering a disturbed Vietnam veteran with a connection to the Witness.", "votes": "47", "thumb": "http://thetvdb.com/banners/episodes/272644/5565074.jpg", "title": "Immortal", "tvdb": "272644", "mpaa": "TV-14", "fanart": "http://thetvdb.com/banners/fanart/original/272644-20.jpg", "season": "2", "status": "Continuing", "poster": "http://thetvdb.com/banners/posters/272644-12.jpg", "tvshowtitle": "12 Monkeys", "studio": "Syfy", "genre": "Mystery / Science-Fiction", "tvrage": "36903", "banner": "http://thetvdb.com/banners/graphical/272644-g5.jpg", "episode": "6", "name": "12 Monkeys S02E06", "premiered": "2016-05-23", "cast": [["Aaron Stanford", ""], ["Amanda Schull", ""], ["Kirk Acevedo", ""], ["Barbara Sukowa", ""], ["Todd Stashwick", ""], ["Emily Hampshire", ""], ["Noah Bean", ""], ["Tom Noonan", ""]], "trailer": "plugin://plugin.video.specto/?action=trailer&name=12+Monkeys"}', 'imdb': 'tt3148266', 'year': '2015', 'action': 'sources', 'tvrage': '36903', 'alter': '0'}
    d=myclass.get_episode(c,imdb,tvdb,title2,data,sezon,epis)
    control.log('############ episode %s' % d)
    time.sleep(2)
    e=myclass.get_sources(d,'','','')
    print ("eee",e)

    for i in e:
        print ("y",i['url'])
        print i

    #f=my.resolve(e[0]['url'])
    #print("mylink",f)


from resources.lib.sources.pelispedia_mv_tv import source as pelispedia
from resources.lib.sources.putlocker_mv_tv import source as putlocker
from resources.lib.sources.muchmovies_mv_tv import source as muchmovies
from resources.lib.sources.pubfilm_mv_tv import source as pubfilm
from resources.lib.sources.yesmovies_mv_tv import source as yesmovies
from resources.lib.sources.fmovies_mv_tv import source as fmovies
from resources.lib.sources.movie25_mv_tv import source as pmovie
from resources.lib.sources.watchfree_mv_tv import source as watchfree
from resources.lib.sources.onemovies_mv_tv import source as onemovies
from resources.lib.sources.xmovies_mv_tv import source as xmovies
#from resources.lib.sources.genvideos_mv import source as genvid
from resources.lib.sources.moviexk_mv_tv import source as mxk
from resources.lib.sources.moviefree_mv_tv import source as moviefree









my1 = yesmovies()
my2 = pelispedia()
my3 = fmovies()
my4 = putlocker()
my5 = muchmovies()
my6 = pubfilm()
my7 = fmovies()

my1000 = xmovies()
my2000 = None

import time
#http://fmovies.to/ajax/episode/info?ts=1481295600&_=2338&id=902kxx&update=0
#http://fmovies.to/ajax/episode/info?ts=1481364000&_=2337&id=902kxx&update=0

#http://fmovies.to/ajax/episode/info?_=2341&id=902kxx&ts=1481367917&update=0
#ts - 1481295600
#     1481342057
print int(time.time())


#x = 0
#for i in [my1, my2, my3, my4]:
#    x = x +1
#    print "--------------- %s" % x
#    getmovie(i)

try:
    #a = my1000.get_movie('tt3799694', 'The Nice Guys', '2016')
    #a = my1000.get_movie('','Snowden','2016')
    #a = my1000.get_movie('tt2948356','Zootopia','2016')
    a  = my1000.get_movie('tt4649416','Almost Christmas','2016')
    #a = my1000.get_movie('','split','2016')

    print "------------"
    print a
    print "------------"

    b = my1000.get_sources(a, '', '', '')
    print "------------"
    print b
    print "------------"
    for i in b:
        print ("y", i['url'])
        print my1000.resolve(i['url'])
    exit()
except Exception as e:
    print 'ERRORRRR %s' % e
    pass
exit()

title2=''
imdb = 'tt5574490'
tvdb = '304262'
title = 'Ballers'
year = '2015'
data = '2016-06-28'
epis= '10'
sezon = '2'

#imdb = 'tt2364582'
#tvdb = '263365'
#title = "Brain Games"
#year = '2011'
#data = '2011-10-09'
#epis= '1'
#sezon = '1'

#imdb = 'tt2078690'
#tvdb = '263365'
#title = "Marvel's Agents of S.H.I.E.L.D."
#year = '2016'
#data = '2016-09-20'
#epis= '1'
#sezon = '4'


imdb = 'tt5574490'
tvdb = '304262'
title = 'Westworld'
year = '2016'
data = '2016-06-28'
epis= '9'
sezon = '1'

imdb = 'tt2191671'
tvdb = '262856'
title = 'Elementary'
year = '2012'
data = '2015-11-19'
epis= '3'
sezon = '4'
title2="Tag, You're Me"

getserial(my2000)
exit()


#{'name': 'Mr. Robot S02E08', 'tvdb': '289590', 'content': 'episode', 'source':
# '{"rating": "8.7", "code": "tt4158110", "tmdb": "62560", "imdb": "tt4158110", "year": "2015", "duration": "2700",
# ""season": "2", "status": "Continuing", "tvshowtitle": "Mr. Robot",
#imdb = 'tt4158110'
#tvdb = '289590'
#title = 'Mr. Robot'
#year = '2015'
#data = '2016-06-28'
#epis= '8'
#sezon = '2'
import time

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
print ("get_sources",e[0][0])
print(e)
f=my.resolve()
exit()




