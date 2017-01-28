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

import re,urlparse,datetime,os,base64,urllib
import zipfile, StringIO

from resources.lib.libraries import cleantitle
from resources.lib import resolvers
from resources.lib.libraries import client
from resources.lib.libraries import control
try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database


class source:
    def __init__(self):
        self.base_link = 'http://cyro.se'
        self.search_link = '/forum/search.php?do=process'
        self.forum_link = '/forum/forum.php'
        self.forum_prefix = '/forum'
        self.data_link = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL21ya25vdy9kYXRhYmFzZS9tYXN0ZXIvZGF5dHNlMS56aXA='
        self.watch_link = '/watch/%s'
        self.headers = {}

    def get_movie(self,imdb, title, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return



    def get_show(self, imdb, tvdb, tvshowtitle, year):
        return


    def dayt_tvcache(self):
        #try:
        #    url = urlparse.urljoin(self.base_link, self.forum_link)
        #    result =  client.source(url)
        #    result = re.compile('<span class="sectiontitle"><a href="([^"]+)">([^<]+)</a></span> <span class="rightrss">').findall(result)
        #    result = [(re.compile('(.+?)(?:&amp)').findall(i[0]), re.sub('&#\d*;', '', i[1])) for i in result]
        #    result = [( i[0][0], cleantitle.get(i[1])) for i in result if len(i[0]) > 0]

        #    return result
        #except:
        #    return
        return


    def get_episode(self, url, imdb, tvdb, title, premiered, season, episode):
        return


    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []

            if url == None: return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            url = (data['title'].translate(None, '\/:*?"\'<>|!,')).replace(' ', '-').replace('--', '-').lower()
            url = urlparse.urljoin(self.base_link, self.watch_link % url)

            r = client.request(url, output='geturl')

            if r == None: raise Exception()

            r = result= client.request(url)
            r = re.sub(r'[^\x00-\x7F]+',' ', r)


            y = re.findall('Date\s*:\s*.+?>.+?(\d{4})', r)
            y = y[0] if len(y) > 0 else None

            if not (data['imdb'] in r or data['year'] == y): raise Exception()


            q = client.parseDOM(r, 'title')
            q = q[0] if len(q) > 0 else None

            quality = '1080p' if ' 1080' in q else 'HD'


            r = client.parseDOM(r, 'div', attrs = {'id': '5throw'})[0]
            r = client.parseDOM(r, 'a', ret='href', attrs = {'rel': 'nofollow'})

            links = []

            for url in r:
                try:
                    if 'yadi.sk' in url:
                        url = resolvers.request(url)
                    elif 'mail.ru' in url:
                        url = resolvers.request(url)
                    else:
                        raise Exception()

                    if url == None: raise Exception()
                    links += [{'source': 'cdn', 'url': url, 'quality': quality}]
                except:
                    pass


            try:
                r = client.parseDOM(result, 'iframe', ret='src')
                r = [i for i in r if 'pasep' in i][0]

                for i in range(0, 4):
                    try:
                        r = client.request(r)
                        r = re.sub(r'[^\x00-\x7F]+',' ', r)
                        r = client.parseDOM(r, 'iframe', ret='src')[0]
                        if 'google' in r: break
                    except:
                        break

                if not 'google' in r: raise Exception()
                #url = directstream.google(r)
                url = r

                for i in url:
                    try: links += [{'source': 'gvideo', 'url': i['url'], 'quality': i['quality']}]
                    except: pass
            except:
                pass

            for i in links: sources.append({'source': i['source'], 'quality': i['quality'], 'provider': 'Dayt', 'url': i['url']})

            return sources
        except Exception as e:
            control.log('ERROR dayyt %s' % e)
            return sources


    def resolve(self, url):
        try:
            return url
        except:
            return


