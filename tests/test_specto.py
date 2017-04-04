# -*- coding: utf-8 -*-


import sys
import os
import time

sys.path.append('../tests/lib')
sys.path.append('../../filmkodi/script.mrknow.urlresolver/lib/')
sys.path.append('../plugin.video.specto')

#print("PATHS",sys.path)
print("CURENT PATHS",os.getcwd())

imdb = 'tt1520211'
tvdb = '304262'
title = 'The Walking Dead'
year = '2010'
data = '2017-03-05'
epis= '12'
sezon = '7'
title2 = 'Say Yes'


from resources.lib.libraries import control

def getmovie(myclass, myname):
    try:
        a = myclass.get_movie('tt3799694', "Assassin's Creed", '2016')
        # a = my1000.get_movie('tt3799694', 'The Nice Guys', '2016')
        # a = my1000.get_movie('','Snowden','2016')
        # a = my1000.get_movie('tt2140479','The Accountant','2016')
        # a  = my1000.get_movie('tt4649416','The Girl on the Train','2016')
        if a == None:
            control.log('XXXXX %s | get_movie' % (myname))
        else:
            control.log('### %s | get_movie %s' % (myname,a))

        b = myclass.get_sources(a, '', '', '')

        if len(b) > 0:
            control.log('### %s | get_sources %s | %s' % (myname, len(b), b))
        else:
            control.log('XXXXX %s | get_sourcess' % (myname))
        return b

    except Exception as e:
        print("ERROR %s: %s" % (myname,e))
        pass

def getserial(myclass, myname):
    try:
        c=myclass.get_show(imdb,tvdb,title,year)
        if c == None:
            control.log('XXXXX %s | get_show' % (myname))
        else:
            control.log('### %s | get_show %s' % (myname,c))
        d=myclass.get_episode(c,imdb,tvdb,title2,data,sezon,epis)
        control.log('### %s | get_episode %s' % (myname,d))
        time.sleep(2)
        e=myclass.get_sources(d,'','','')
        if len(e) > 0:
            control.log('### %s | get_sources %s | %s' % (myname, len(e), e))
        else:
            control.log('XXXXX %s | get_sourcess' % (myname))
        return e

    except Exception as e:
        print("ERROR %s: %s" % (myname,e))
        pass

from resources.lib.sources.pelispedia_mv_tv import source as pelispedia
from resources.lib.sources.putlocker_mv_tv import source as putlocker
from resources.lib.sources.muchmovies_mv_tv import source as muchmovies
from resources.lib.sources.pubfilm_mv_tv import source as pubfilm
from resources.lib.sources.yesmovies_mv_tv import source as yesmovies
from resources.lib.sources.fmovies_mv_tv import source as fmovies
from resources.lib.sources.movie25_mv_tv import source as movie25
from resources.lib.sources.movieshd_mv_tv import source as movieshd
from resources.lib.sources.onemovies_mv_tv import source as onemovies
#from resources.lib.sources.genvideos_mv import source as genvid
from resources.lib.sources.onlinemovies_mv_tv import source as onlinemovies
from resources.lib.sources.watch5s_mv_tv import source as watch5s
from resources.lib.sources.onseries_tv import source as onseries
from resources.lib.sources.wrzcraft_mv_tv import source as wrz
from resources.lib.sources.onlinedizi_tv import source as onlinedizi

ala = getserial(onemovies(), 'onemovies')
#print ala[0]['url']
#print onlinedizi().resolve(ala[0]['url'])

exit()

getmovie(fmovies(),'fmovies')
getserial(fmovies(), 'fmovies')
getmovie(pelispedia(),'pelispedia')
getserial(pelispedia(), 'pelispedia')
getmovie(putlocker(),'putlocker')
getserial(putlocker(), 'putlocker')
#getserial(movieshd(), 'iitv')
getmovie(movie25(),'movie25')
getserial(movie25(), 'movie25')
getmovie(movieshd(),'movieshd')
getserial(movieshd(), 'movieshd')
getmovie(muchmovies(),'muchmovies')
getserial(muchmovies(), 'muchmovies')
#getmovie(segos(),'segos')
getmovie(muchmovies(),'onemovies')
getserial(muchmovies(), 'onemovies')


getserial(onlinedizi(), 'onlinedizi')
getmovie(yesmovies(),'yesmovies')
getserial(yesmovies(), 'yesmovies')



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

#imdb = 'tt3322310'
#tvdb = '263365'
#title = "Marvel's Iron Fist"
#year = '2017'
#data = '2017-09-20'
#epis= '4'
#sezon = '1'


#imdb = 'tt5574490'
#tvdb = '304262'
#title = 'Sherlock'
#year = '2010'
#data = '2016-06-28'
#epis= '3'
#sezon = '4'

#imdb = 'tt2191671'
#tvdb = '262856'
#title = 'Elementary'
#year = '2012'
#data = '2015-11-19'
#epis= '3'
#sezon = '5'
#title2="Tag, You're Me"


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
