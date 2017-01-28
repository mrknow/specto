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


import re,urllib,urlparse,random
import hashlib, string, json
from resources.lib.libraries import cleantitle
from resources.lib.libraries import client
from resources.lib.libraries import control


class source:
    def __init__(self):
        self.base_link = 'http://moviexk.com'
        self.search_link = 'aHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vY3VzdG9tc2VhcmNoL3YxZWxlbWVudD9rZXk9QUl6YVN5Q1ZBWGlVelJZc01MMVB2NlJ3U0cxZ3VubU1pa1R6UXFZJnJzej1maWx0ZXJlZF9jc2UmbnVtPTEwJmhsPWVuJmN4PTAxMzQ0NjM1MTYzMDQ5MzU5NTE5Nzprc2NlY2tjdXZxcyZnb29nbGVob3N0PXd3dy5nb29nbGUuY29tJnE9JXM='

    def get_movie(self, imdb, title, year):
        try:
            url = '%s/%s-%s/' % (self.base_link, cleantitle.geturl(title), year)

            url = client.request(url, output='geturl')

            if url == None: raise Exception()

            url = re.findall('(?://.+?|)(/.+)', url)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            pass

        try:
            t = cleantitle.get(title)

            q = '%s %s' % (title, year)
            q = self.search_link.decode('base64') % urllib.quote_plus(q)

            r = client.request(q, error=True)

            r = json.loads(r)['results']
            r = [(i['url'], i['titleNoFormatting']) for i in r]
            r = [(i[0], re.findall('(?:^Watch Movie |^Watch |)(.+?)\((\d{4})', i[1])) for i in r]
            r = [(i[0], i[1][0][0], i[1][0][1]) for i in r if i[1]]
            r = [(urllib.unquote_plus(i[0]), i[1], i[2]) for i in r]
            r = [(urlparse.urlparse(i[0]).path, i[1], i[2]) for i in r]
            r = [i for i in r if t == cleantitle.get(i[1]) and year == i[2]]
            r = re.sub('/watch-movie-|-\d+$', '/', r[0][0].strip())

            url = re.findall('(?://.+?|)(/.+)', r)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            pass

    def get_show(self, imdb, tvdb, tvshowtitle, year):
        try:
            t = cleantitle.get(tvshowtitle)

            q = '%s %s' % (tvshowtitle, year)
            q = self.search_link.decode('base64') % urllib.quote_plus(q)

            r = client.request(q)

            r = json.loads(r)['results']
            r = [(i['url'], i['titleNoFormatting']) for i in r]

            r = [(i[0], re.findall('(?:^Watch Movie |^Watch |)(.+?)$', i[1])) for i in r]
            r = [(i[0], i[1][0].rsplit('TV Series')[0].strip('(')) for i in r if i[1]]
            r = [(urllib.unquote_plus(i[0]), i[1]) for i in r]
            r = [(urlparse.urlparse(i[0]).path, i[1]) for i in r]
            r = [i for i in r if t == cleantitle.get(i[1])]

            r = urlparse.urljoin(self.base_link, r[0][0].strip())

            if '/watch-movie-' in r: r = re.sub('/watch-movie-|-\d+$', '/', r)

            y = re.findall('(\d{4})', r)

            if y:
                y = y[0]
            else:
                y = client.request(r)
                y = re.findall('(?:D|d)ate\s*:\s*(\d{4})', y)[0]

            if not year == y: raise Exception()

            url = re.findall('(?://.+?|)(/.+)', r)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return

    def get_episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return

            url = '%s?season=%01d&episode=%01d' % (url, int(season), int(episode))
            return url
        except:
            return

    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []

            if url == None: return sources

            f = urlparse.urljoin(self.base_link, url)

            url = f.rsplit('?', 1)[0]

            r = client.request(url, mobile=True)

            r = client.parseDOM(r, 'div', attrs = {'id': 'servers'})
            r = client.parseDOM(r, 'li')
            r = zip(client.parseDOM(r, 'a', ret='href'), client.parseDOM(r, 'a', ret='title'))

            try:
                s = urlparse.parse_qs(urlparse.urlparse(f).query)['season'][0]
                e = urlparse.parse_qs(urlparse.urlparse(f).query)['episode'][0]
                r = [(i[0], re.findall('(\d+)', i[1])) for i in r]
                r = [(i[0], '%01d' % int(i[1][0]), '%01d' % int(i[1][1])) for i in r if len(i[1]) > 1]
                r = [i[0] for i in r if s == i[1] and e == i[2]]
            except:
                r = [i[0] for i in r]

            for u in r:
                try:
                    url = client.request(u, mobile=True)
                    url = client.parseDOM(url, 'source', ret='src')
                    url = [i.strip().split()[0] for i in url]

                    for i in url:
                        try: sources.append({'source': 'gvideo', 'quality': client.googletag(i)[0]['quality'], 'provider': 'Moviexk','url': i})
                        except: pass
                except:
                    pass

            return sources

        except Exception as e:
            control.log('ERROR moviexk %s' % e)
            return sources



    def resolve(self, url):
        return client.googlepass(url)


