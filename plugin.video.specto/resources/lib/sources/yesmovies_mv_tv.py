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
import requests




class source:
    def __init__(self):
        self.base_link = 'https://yesmovies.to'
        self.info_link = '/ajax/movie_info/%s.html'
        self.episode_link = '/ajax/v4_movie_episodes/%s'
        self.playlist_link = '/ajax/v2_get_sources/%s.html?hash=%s'
        #https://yesmovies.to/ajax/v4_movie_episodes/13115


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
                    if not y == year: raise Exception()
                    return urlparse.urlparse(i[0]).path + '?episode=%01d' % int(episode)
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
        #                sources.append({'source': 'gvideo', 'quality': i['quality'].encode('utf-8'), 'provider': 'Yesmovies', 'url': i['url'].encode('utf-8')})
        try:
            sources = []

            if url == None: return sources

            try: url, episode = re.findall('(.+?)\?episode=(\d*)$', url)[0]
            except: episode = None

            url = urlparse.urljoin(self.base_link, url)

            vid_id = re.findall('-(\d+)', url)[-1]
            print("VID",vid_id)

            '''
            quality = cache.get(self.ymovies_info, 9000, vid_id)[1].lower()
            if quality == 'cam' or quality == 'ts': quality = 'CAM'
            elif quality == 'hd': quality = 'HD'
            else: quality = 'SD'
            '''

            for i in range(3):
                r = client.request(url)
                if not r == None: break

            ref = client.parseDOM(r, 'a', ret='href', attrs = {'class': 'mod-btn mod-btn-watch'})[0]
            ref = urlparse.urljoin(self.base_link, ref)
            #print("VID-ref", ref)

            for i in range(3):
                r = client.request(ref, referer=url)
                if not r == None: break
            print("VID-r", r)

            c = client.parseDOM(r, 'img', ret='src', attrs = {'class': 'hidden'})

            if c: cookie = client.request(c[0], referer=ref, output='cookie')
            else: cookie = ''
            print("VID-c", cookie)


            #server = re.findall('server\s*:\s*"(.+?)"', r)[0]
            #print("VID-s", server)

            #type = re.findall('type\s*:\s*"(.+?)"', r)[0]
            #print("VID-t", type)

            #episode_id = re.findall('episode_id\s*:\s*"(.+?)"', r)[0]

            r = self.episode_link % (vid_id)
            u = urlparse.urljoin(self.base_link, r)

            for i in range(13):
                r = client.request(u, referer=ref)
                if not r == None: break
            print("VID-r", r)
            print json.loads(r)['html']


            r = client.parseDOM(json.loads(r)['html'], 'div', attrs={'class':'pas-list'})[0]
            r = re.compile('(<li.+?/li>)', re.DOTALL).findall(r)
            print("VID-r1", r)

            r = [(client.parseDOM(i, 'li', ret='data-id'),client.parseDOM(i, 'li', ret='data-server'), client.parseDOM(i, 'a', ret='title')) for i in r]
            print("VID-r2", r)

            if not episode == None:
                r = [(i[0][0], i[1][0], i[2][0]) for i in r if i[0] and i[1]]
                r = [(i[0],i[1], ''.join(re.findall('(\d+)', i[2])[:1])) for i in r]
                r = [(i[0],i[1]) for i in r if '%01d' % int(i[2]) == episode]
            else:
                r = [(i[0][0],i[1][0])  for i in r if i[0]]
            print("VID-r3", r)

            #r = [re.findall('(\d+)', i) for i in r]
            #r = [i[:2] for i in r if len(i) > 1]
            r = [i[0] for i in r if 1 <= int(i[1]) <= 11][:3]
            print("VID-r4", r)

            for u in r:
                try:
                    key = 'xwh38if39ucx' ; key2 = '8qhfm9oyq1ux' ; key3 = 'ctiw4zlrn09tau7kqvc153uo'

                    k = u + key3
                    v = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))

                    c = key + u + key2 + '=%s' % v
                    c = '%s; %s' % (cookie, c)

                    url = urllib.quote(uncensored(k, v))
                    url = '/ajax/v2_get_sources/%s?hash=%s' % (u, url)
                    url = urlparse.urljoin(self.base_link, url)

                    for i in range(3):
                        u = client.request(url, referer=ref, cookie=c, timeout='10')
                        if not u == None: break

                    u = json.loads(u)['playlist'][0]['sources']
                    u = [i['file'] for i in u if 'file' in i]

                    for i in u:
                        try: sources.append({'source': 'gvideo', 'quality': client.googletag(i)[0]['quality'], 'provider': 'Yesmovies','url': i})
                        except: pass
                except:
                    pass

            return sources
        except Exception as e:
            print("Error %s" % e)
            return sources

    def resolve(self, url):
        return client.googlepass(url)


def uncensored(a,b):
    x = '' ; i = 0
    for i, y in enumerate(a):
        z = b[i % len(b) - 1]
        y = int(ord(str(y)[0])) + int(ord(str(z)[0]))
        x += chr(y)
    x = base64.b64encode(x)
    return x