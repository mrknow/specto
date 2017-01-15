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

import re,urllib,urlparse,json,base64

from resources.lib.libraries import cleantitle
from resources.lib.libraries import client
from resources.lib.libraries import cache
from resources.lib.libraries import control

import cookielib, os
cookie_file = os.path.join(control.dataPath , 'mycookie'+'.cookies')
cj = cookielib.LWPCookieJar()

class source:
    def __init__(self):
        self.base_link = 'http://www.pelispedia.tv'
        self.base_link = 'http://www.pelispedia.tv'
        self.movie_link = '/pelicula/%s/'
        self.tvsearch_link = '/serie/%s/'



    def get_movie(self, imdb, title, year):

        try:
            t = cleantitle.get(title)

            query = self.movie_link % cleantitle.query10(title)
            query = urlparse.urljoin(self.base_link, query)
            control.log('PELISPEDIA URL %s' % query)
            result = client.request(query).decode('gb18030').encode('utf-8')
            result = client.parseDOM(result, 'div', attrs={'id': 'player'})[0]
            r = [(re.findall('(.*?)<a', client.parseDOM(result, 'center')[0])[0].strip(),
                      re.findall('>\((.*?)\)</a>', client.parseDOM(result, 'center')[0])[0])]
            r = [i for i in r if t == cleantitle.get(i[0]) and year == (i[1])][0]
            return query
        except:
            return

    def get_show(self, imdb, tvdb, tvshowtitle, year):
        try:
            url = self.tvsearch_link % cleantitle.query10(tvshowtitle)

            r = urlparse.urljoin(self.base_link, url)
            r = client.request(r, limit='1')
            r = client.parseDOM(r, 'title')

            if not r:
                url = 'http://www.imdb.com/title/%s' % imdb
                url = client.request(url, headers={'Accept-Language':'es-ES'})
                url = client.parseDOM(url, 'title')[0]
                url = re.sub('\((?:.+?|)\d{4}.+', '', url).strip()
                url = cleantitle.normalize(url.encode("utf-8"))
                url = self.tvsearch_link % cleantitle.geturl(url)

                r = urlparse.urljoin(self.base_link, url)
                r = client.request(r, limit='1')
                r = client.parseDOM(r, 'title')

            if not year in r[0]: raise Exception()

            return url
        except:
            return

    def get_episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return

            url = '/pelicula/%s-season-%01d-episode-%01d/' % (url.strip('/').split('/')[-1], int(season), int(episode))
            return url
        except:
            return


    def get_sources(self, url, hosthdDict, hostDict, locDict):
        control.log("><><><><> PELISPEDIA SOURCE %s" % url)
        try:
            sources = []

            if url == None: return sources

            r = urlparse.urljoin(self.base_link, url)

            result = client.request(r)

            f = client.parseDOM(result, 'iframe', ret='src')
            f = [i for i in f if 'iframe' in i][0]

            result = client.request(f, headers={'Referer': r})

            r = client.parseDOM(result, 'div', attrs = {'id': 'botones'})[0]
            r = client.parseDOM(r, 'a', ret='href')
            r = [(i, urlparse.urlparse(i).netloc) for i in r]

            links = []

            for u, h in r:
                if not 'pelispedia' in h and not 'thevideos.tv' in h: continue

                result = client.request(u, headers={'Referer': f})

                try:
                    if 'pelispedia' in h: raise Exception()

                    url = re.findall('sources\s*:\s*\[(.+?)\]', result)[0]
                    url = re.findall('file\s*:\s*(?:\"|\')(.+?)(?:\"|\')\s*,\s*label\s*:\s*(?:\"|\')(.+?)(?:\"|\')', url)
                    url = [i[0] for i in url if '720' in i[1]][0]

                    links.append({'source': 'cdn', 'quality': 'HD', 'url': url, 'direct': False})
                except:
                    pass

                try:
                    url = re.findall('sources\s*:\s*\[(.+?)\]', result)[0]
                    url = re.findall('file\s*:\s*(?:\"|\')(.+?)(?:\"|\')', url)

                    for i in url:
                        try: links.append({'source': 'gvideo', 'quality': client.googletag(i)[0]['quality'], 'url': i, 'direct': True})
                        except: pass
                except:
                    pass

                try:
                    headers = {'X-Requested-With': 'XMLHttpRequest', 'Referer': u}

                    post = re.findall('gkpluginsphp.*?link\s*:\s*"([^"]+)', result)[0]
                    post = urllib.urlencode({'link': post})

                    url = urlparse.urljoin(self.base_link, '/Pe_flsh/plugins/gkpluginsphp.php')
                    url = client.request(url, post=post, headers=headers)
                    url = json.loads(url)['link']

                    links.append({'source': 'gvideo', 'quality': 'HD', 'url': url, 'direct': True})
                except:
                    pass

                try:
                    headers = {'X-Requested-With': 'XMLHttpRequest'}

                    post = re.findall('var\s+parametros\s*=\s*"([^"]+)', result)[0]


                    post = urlparse.parse_qs(urlparse.urlparse(post).query)['pic'][0]
                    post = urllib.urlencode({'sou': 'pic', 'fv': '23', 'url': post})

                    url = urlparse.urljoin(self.base_link, '/Pe_Player_Html5/pk/pk_2/plugins/protected.php')
                    url = client.request(url, post=post, headers=headers)
                    url = json.loads(url)[0]['url']

                    links.append({'source': 'cdn', 'quality': 'HD', 'url': url, 'direct': True})
                except:
                    pass

            for i in links:
                sources.append({'source': i['source'], 'quality': i['quality'], 'provider': 'Pelispedia', 'url': i['url']})

            return sources

        except Exception as e:
            control.log('ERROR PELISP %s' % e)
            return sources


    def resolve(self, url):
        control.log("##pelispedia %s " % url)

        return url


