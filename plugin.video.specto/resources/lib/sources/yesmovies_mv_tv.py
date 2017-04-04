# -*- coding: utf-8 -*-

'''
    Specto Add-on
    Copyright (C) 2016 mrknow

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

# TODO: Check gvideo resolving

import re,urllib,urlparse, json, hashlib
import base64
import random, string
import time


from resources.lib.libraries import cleantitle
from resources.lib.libraries import client
from resources.lib.libraries import cache
from resources.lib import resolvers
from resources.lib.libraries import control
from resources.lib.libraries import jsunfuck
import requests


CODE = '''def retA():
    class Infix:
        def __init__(self, function):
            self.function = function
        def __ror__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __or__(self, other):
            return self.function(other)
        def __rlshift__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __rshift__(self, other):
            return self.function(other)
        def __call__(self, value1, value2):
            return self.function(value1, value2)
    def my_add(x, y):
        try: return x + y
        except Exception: return str(x) + str(y)
    x = Infix(my_add)
    return %s
param = retA()'''

class source:
    def __init__(self):
        self.base_link = 'https://yesmovies.to'
        self.info_link = '/ajax/movie_info/%s.html'
        self.episode_link = '/ajax/v4_movie_episodes/%s'
        self.playlist_link = '/ajax/v2_get_sources/%s.html?hash=%s'
        self.server_link = '/ajax/v4_movie_episodes/%s'
        self.embed_link = '/ajax/movie_embed/%s'
        self.token_link = '/ajax/movie_token?eid=%s&mid=%s'
        self.sourcelink = '/ajax/movie_sources/%s?x=%s&y=%s'


    def get_movie(self, imdb, title, year):
        try:
            t = cleantitle.get(title)

            q = '/search/%s.html' % (urllib.quote_plus(cleantitle.query(title)))
            q = urlparse.urljoin(self.base_link, q)

            for i in range(3):
                r = client.request(q)
                if not r == None: break

            r = client.parseDOM(r, 'div', attrs = {'class': 'ml-item'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in r]
            r = [(i[0][0], i[1][0]) for i in r if i[0] and i[1]]
            r = [i[0] for i in r if t == cleantitle.get(i[1])][:2]
            r = [(i, re.findall('(\d+)', i)[-1]) for i in r]

            for i in r:
                try:
                    y, q = cache.get(self.ymovies_info, 9000, i[1])
                    if not y == year: raise Exception()
                    return urlparse.urlparse(i[0]).path
                except:
                    pass

        except Exception as e:
            control.log('Error yesmovies %s' % e)
            return


    def get_show(self, imdb, tvdb, tvshowtitle, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return


    def get_episode(self, url, imdb, tvdb, title, date, season, episode):
        try:
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            t = cleantitle.get(data['tvshowtitle'])
            title = data['tvshowtitle']
            season = '%01d' % int(season) ; episode = '%01d' % int(episode)
            year = re.findall('(\d{4})', date)[0]
            years = [str(year), str(int(year)+1), str(int(year)-1)]

            r = cache.get(self.ymovies_info_season, 720, title, season)
            r = [(i[0], re.findall('(.+?)\s+(?:-|)\s+season\s+(\d+)$', i[1].lower())) for i in r]
            r = [(i[0], i[1][0][0], i[1][0][1]) for i in r if i[1]]
            r = [i[0] for i in r if t == cleantitle.get(i[1]) and season == '%01d' % int(i[2])][:2]
            r = [(i, re.findall('(\d+)', i)[-1]) for i in r]

            for i in r:
                try:
                    y, q = cache.get(self.ymovies_info, 9000, i[1])
                    mychk = False
                    years = [str(year),str(int(year) + 1),str(int(year) - 1)]
                    for x in years:
                        if str(y) == x: mychk = True
                    if mychk == False: raise Exception()
                    return urlparse.urlparse(i[0]).path, (episode)
                except:
                    pass
        except Exception as e:
            control.log('Error yesmovies %s' % e)
            return

    def ymovies_info_season(self, title, season):
        try:
            q = '%s Season %s' % (cleantitle.query(title), season)
            q = '/search/%s.html' % (urllib.quote_plus(q))
            q = urlparse.urljoin(self.base_link, q)

            for i in range(3):
                r = client.request(q)
                if not r == None: break

            r = client.parseDOM(r, 'div', attrs = {'class': 'ml-item'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in r]
            r = [(i[0][0], i[1][0]) for i in r if i[0] and i[1]]

            return r
        except:
            return

    def ymovies_info(self, url):
        try:
            u = urlparse.urljoin(self.base_link, self.info_link)

            for i in range(3):
                r = client.request(u % url)
                if not r == None: break

            q = client.parseDOM(r, 'div', attrs = {'class': 'jtip-quality'})[0]

            y = client.parseDOM(r, 'div', attrs = {'class': 'jt-info'})
            y = [i.strip() for i in y if i.strip().isdigit() and len(i.strip()) == 4][0]

            return (y, q)
        except:
            return

    def get_sources(self, url, hosthdDict, hostDict, locDict):
        #try:
        try:
            sources = []

            if url is None: return sources

            if url[0].startswith('http'):
                self.base_link = url[0]

            try:
                if url[1] > 0:
                    episode = url[1]
                else:
                    episode = None
            except:
                episode = None

            mid = re.findall('-(\d+)', url[0])[-1]

            try:
                headers = {'Referer': url}
                u = urlparse.urljoin(self.base_link, self.server_link % mid)
                r = client.request(u, headers=headers, XHR=True)
                r = json.loads(r)['html']
                r = client.parseDOM(r, 'div', attrs = {'class': 'pas-list'})
                ids = client.parseDOM(r, 'li', ret='data-id')
                servers = client.parseDOM(r, 'li', ret='data-server')
                labels = client.parseDOM(r, 'a', ret='title')
                r = zip(ids, servers, labels)
                for eid in r:
                    try:
                        try:
                            ep = re.findall('episode.*?(\d+):.*?',eid[2].lower())[0]
                        except:
                            ep = 0
                        if (episode is None) or (int(ep) == int(episode)):
                            url = urlparse.urljoin(self.base_link, self.token_link % (eid[0], mid))
                            script = client.request(url)
                            if '$_$' in script:
                                params = self.uncensored1(script)
                            elif script.startswith('[]') and script.endswith('()'):
                                params = self.uncensored2(script)
                            else:
                                raise Exception()
                            u = urlparse.urljoin(self.base_link, self.sourcelink % (eid[0], params['x'], params['y']))
                            r = client.request(u)
                            url = json.loads(r)['playlist'][0]['sources']
                            url = [i['file'] for i in url if 'file' in i]
                            url = [client.googletag(i) for i in url]
                            url = [i[0] for i in url if i]
                            for s in url:
                                sources.append({'source': 'gvideo', 'quality': client.googletag(s['url'])[0]['quality'],
                                                'provider': 'Yesmovies', 'url': s['url']})

                    except:
                        pass
            except:
                pass

            return sources
        except Exception as e:
            return sources

    def resolve(self, url):
        return client.googlepass(url)


    def uncensored1(self, script):
        try:
            script = '(' + script.split("(_$$)) ('_');")[0].split("/* `$$` */")[-1].strip()
            script = script.replace('(__$)[$$$]', '\'"\'')
            script = script.replace('(__$)[_$]', '"\\\\"')
            script = script.replace('(o^_^o)', '3')
            script = script.replace('(c^_^o)', '0')
            script = script.replace('(_$$)', '1')
            script = script.replace('($$_)', '4')

            vGlobals = {"__builtins__": None, '__name__': __name__, 'str': str, 'Exception': Exception}
            vLocals = {'param': None}
            exec (CODE % script.replace('+', '|x|'), vGlobals, vLocals)
            data = vLocals['param'].decode('string_escape')
            x = re.search('''_x=['"]([^"']+)''', data).group(1)
            y = re.search('''_y=['"]([^"']+)''', data).group(1)
            return {'x': x, 'y': y}
        except:
            pass

    def uncensored2(self, script):
        try:
            js = jsunfuck.JSUnfuck(script).decode()
            x = re.search('''_x=['"]([^"']+)''', js).group(1)
            y = re.search('''_y=['"]([^"']+)''', js).group(1)
            return {'x': x, 'y': y}
        except:
            pass