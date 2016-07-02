# -*- coding: utf-8 -*-

'''
    Specto Add-on
    Copyright (C) 2015 lambda

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import re,urlparse,json,os,base64,urllib

from resources.lib.libraries import cleantitle
from resources.lib import resolvers
from resources.lib.libraries import client

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database


class source:
    def __init__(self):
        self.base_link = 'http://genvideos.org'
        self.search_link = '/results?q=%s'
        self.post = 'http://genvideos.org/video_info/iframe'
        self.headers = {}

    def get_movie(self,imdb, title, year):
        try:
            query = self.search_link % (title)
            url = urlparse.urljoin(self.base_link, client.replaceHTMLCodes(query))
            result = client.request(url, headers=self.headers)
            result = client.parseDOM(result, 'div', attrs = {'class': 'cell'})
            print ("r1",result)
            title = cleantitle.movie(title)
            years = ['(%s)' % str(year), '(%s)' % str(int(year)+1), '(%s)' % str(int(year)-1)]
            result = [(client.parseDOM(i, 'a', ret='href')[-1], client.parseDOM(i, 'a',ret='title')[-1]) for i in result]
            print ("r2", result)
            result = [i for i in result if title in cleantitle.movie(i[1])]
            print ("r3", result)
            result = [i[0] for i in result if any(x in i[1] for x in years)][0]
            print ("r4", result)
            url = result.encode('utf-8')
            return url
        except:
            return



    def get_show(self, imdb, tvdb, tvshowtitle, year):
        return

    def get_episode(self, url, imdb, tvdb, title, premiered, season, episode):
        return


    def get_sources(self, url, hosthdDict, hostDict, locDict):
        sources = []
        try:
            if url == None: return sources
            post = urlparse.parse_qs(urlparse.urlparse(url).query)['v'][0]
            post = urllib.urlencode({'v':post})
            result = client.request(self.post, post=post)
            result = json.loads(result)
            print("r102", result)
            for i in result:
                print("i",i,result[i])
                mq = 'SD'
                if '1080' in i: mq = '1080p'
                if '72' in i: mq = 'HD'
                sources.append({'source': 'gvideo', 'quality': mq, 'provider': 'Genvideos', 'url': result[i]})
            return sources
        except:
            return sources


    def resolve(self, url):
        try:
            url1 = url.replace('//html5player.org/embed?url=','')
            url1 = urllib.unquote(url1)
            #result = client.request(url)
            return url1
        except:
            return


