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


import re,urllib,urlparse
import json, time, random, string
import base64, hashlib

from resources.lib.libraries import cleantitle
from resources.lib.libraries import cache
from resources.lib.libraries import client
from resources.lib.libraries import control
from resources.lib import resolvers


class source:
    def __init__(self):
        self.base_link = 'http://cartoonhd.online'
        #http://api.cartoonh0A6ru35yevokjaqbb8
        self.social_lock = '0A6ru35yevokjaqbb8'
        #http://api.cartoonhd.online/api/v1/0A6ru35yevokjaqbb8
        self.search_link = 'http://api.cartoonhd.online/api/v1/' + self.social_lock


    def get_movie(self, imdb, title, year):
        try:
            tk = cache.get(self.movieshd_token, 8)
            set = self.movieshd_set()
            rt = self.movieshd_rt(tk + set)
            sl = self.movieshd_sl()
            tm = int(time.time() * 1000)

            headers = {'X-Requested-With': 'XMLHttpRequest'}

            #url = urlparse.urljoin(self.base_link, self.search_link)
            url = self.search_link

            post = {'q': title.lower(), 'limit': '100', 'timestamp': tm, 'verifiedCheck': tk, 'set': set, 'rt': rt, 'sl': sl}
            post = urllib.urlencode(post)

            r = client.request(url, post=post, headers=headers)
            r = json.loads(r)

            t = cleantitle.get(title)

            r = [i for i in r if 'year' in i and 'meta' in i]
            r = [(i['permalink'], i['title'], str(i['year']), i['meta'].lower()) for i in r]
            r = [i for i in r if 'movie' in i[3]]
            r = [i[0] for i in r if t == cleantitle.get(i[1]) and year == i[2]][0]

            url = re.findall('(?://.+?|)(/.+)', r)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return

    def get_show(self, imdb, tvdb, tvshowtitle, year):
        try:
            tk = cache.get(self.movieshd_token, 8)

            set = self.movieshd_set()
            rt = self.movieshd_rt(tk + set)
            sl = self.movieshd_sl()

            tm = int(time.time() * 1000)

            headers = {'X-Requested-With': 'XMLHttpRequest'}


            url =  self.search_link

            post = {'q': tvshowtitle.lower(), 'limit': '20', 'timestamp': tm, 'verifiedCheck': tk, 'set': set, 'rt': rt, 'sl': sl}
            post = urllib.urlencode(post)

            r = client.request(url, post=post, headers=headers)
            r = json.loads(r)

            t = cleantitle.get(tvshowtitle)

            r = [i for i in r if 'year' in i and 'meta' in i]
            r = [(i['permalink'], i['title'], str(i['year']), i['meta'].lower()) for i in r]
            r = [i for i in r if 'tv' in i[3]]
            r = [i[0] for i in r if t == cleantitle.get(i[1]) and year == i[2]][0]

            url = re.findall('(?://.+?|)(/.+)', r)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return

    def get_episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return

            r = '%s/season/%01d/episode/%01d' % (url, int(season), int(episode))

            url = re.findall('(?://.+?|)(/.+)', r)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return

    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []

            if url == None: return sources

            url1 = urlparse.urljoin(self.base_link, url)

            r100 = client.request(url1, output='extended')
            cookie = r100[4] ; headers = r100[3] ; result = r100[0]


            try:
                auth = re.findall('__utmx=(.+)', cookie)[0].split(';')[0]
                auth = 'Bearer %s' % urllib.unquote_plus(auth)
            except:
                auth = 'Bearer false'

            headers['Authorization'] = auth
            headers['X-Requested-With'] = 'XMLHttpRequest'
            #headers['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
            #headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
            headers['Cookie'] = cookie

            u = '/ajax/nembeds.php'
            u = urlparse.urljoin(self.base_link, u)

            #action = 'getEpisodeEmb' if '/episode/' in url else 'getMovieEmb'
            if '/episode/' in url:
                url = urlparse.urljoin(self.base_link,  '/tv-series'+ url)
                action = 'getEpisodeEmb'
            else:
                action = 'getMovieEmb'
                url = urlparse.urljoin(self.base_link, '/tv-series' + url)

            headers['Referer'] = url
            control.sleep(200)

            elid = urllib.quote(base64.encodestring(str(int(time.time()))).strip())

            token = re.findall("var\s+tok\s*=\s*'([^']+)", result)[0]

            idEl = re.findall('elid\s*=\s*"([^"]+)', result)[0]

            post = {'action': action, 'idEl': idEl, 'token': token, 'elid': elid}
            post = urllib.urlencode(post)
            print post
            print headers


            r = client.request(u, post=post, headers=headers, output='')
            print("####",r)
            r = str(json.loads(r))
            r = client.parseDOM(r, 'iframe', ret='.+?') + client.parseDOM(r, 'IFRAME', ret='.+?')

            links = []

            for i in r:
                try: links += [{'source': 'gvideo', 'quality': client.googletag(i)[0]['quality'], 'url': i}]
                except: pass

            links += [{'source': 'openload', 'quality': 'SD', 'url': i} for i in r if 'openload.co' in i]
            links += [{'source': 'videomega', 'quality': 'SD', 'url': i} for i in r if 'thevideo.me' in i]
            for i in links: sources.append({'source': i['source'], 'quality': i['quality'], 'provider': 'MoviesHD', 'url': i['url']})

            return sources
        except Exception as e:
            control.log('ERROR moviesHD %s' % e)
            return sources


    def resolve(self, url):
        try:
            if 'openload.co' in url or 'thevideo.me' in url or 'vidto.me' in url:
                url = resolvers.request(url)
            else:
                return client.googlepass(url)
        except:
            return

    def movieshd_token(self):
        try:
            token = client.request(self.base_link)
            token = re.findall("var\s+tok\s*=\s*'([^']+)", token)[0]
            return token
        except:
            return


    def movieshd_set(self):
        return ''.join([random.choice(string.ascii_letters) for _ in xrange(25)])

    def movieshd_sl(self):
        return hashlib.md5(base64.encodestring('0A6ru35yyi5yn4THYpJqy0X82tE95btV')+self.social_lock).hexdigest()


    def movieshd_rt(self, s, shift=13):
        s2 = ''
        for c in s:
            limit = 122 if c in string.ascii_lowercase else 90
            new_code = ord(c) + shift
            if new_code > limit:
                new_code -= 26
            s2 += chr(new_code)
        return s2

