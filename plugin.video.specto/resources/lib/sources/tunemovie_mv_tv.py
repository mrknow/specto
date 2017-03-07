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


import re,urllib,urlparse,base64

from resources.lib.libraries import cleantitle
from resources.lib.libraries import pyaes
from resources.lib.libraries import control
from resources.lib.libraries import client
from resources.lib import resolvers
import json

class source:
    def __init__(self):
        self.base_link = 'http://tunemovies.to'
        self.search_link = '/search/%s.html'
        #http://tunemovie.is/search-movies/The+Hateful+Eight.html

    def get_movie(self, imdb, title, year):
        try:
            query = urlparse.urljoin(self.base_link, self.search_link)
            query = query % urllib.quote_plus(title)

            t = cleantitle.get(title)

            r = client.request(query)

            r = client.parseDOM(r, 'div', attrs = {'id': 'post-\d+'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title'), re.findall('(\d{4})', i)) for i in r]
            r = [(i[0][0], i[1][0], i[2][0]) for i in r if len(i[0]) > 0 and len(i[1]) > 0 and len(i[2]) > 0]

            r = [i[0] for i in r if t == cleantitle.get(i[1]) and year == i[2]][0]

            url = re.findall('(?://.+?|)(/.+)', r)[0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return



    def get_show(self, imdb, tvdb, tvshowtitle, year):
        try:
            url = '%s (%s)' % (tvshowtitle, year)
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return


    def get_episode(self, url, imdb, tvdb, title, date, season, episode):
        try:
            tvshowtitle, year = re.compile('(.+?) [(](\d{4})[)]$').findall(url)[0]

            query = self.search_link % (urllib.quote_plus(tvshowtitle))
            query = urlparse.urljoin(self.base_link, query)

            result = client.source(query)
            result = client.parseDOM(result, 'div', attrs = {'id': 'post-.+?'})

            tvshowtitle = cleantitle.tv(tvshowtitle)
            season = '%01d' % int(season)
            episode = '%01d' % int(episode)
            years = ['%s' % str(year), '%s' % str(int(year)+1), '%s' % str(int(year)-1)]

            result = [(client.parseDOM(i, 'a', ret='href')[0], client.parseDOM(i, 'a', ret='title')[0], client.parseDOM(i, 'div', attrs = {'class': 'status status-year'})) for i in result]
            result = [x for y,x in enumerate(result) if x not in result[:y]]
            result = [(i[0], i[1], i[2][0]) for i in result if len(i[2]) > 0]
            result = [(i[0], re.compile('(.+?) Season (\d*)$').findall(i[1]), i[2]) for i in result]
            result = [(i[0], i[1][0][0], i[1][0][1], i[2]) for i in result if len(i[1]) > 0]
            result = [i for i in result if tvshowtitle == cleantitle.tv(i[1])]
            result = [i for i in result if season == i[2]]
            result = [(i[0], i[1], str(int(i[3]) - int(i[2]) + 1)) for i in result]
            result = [i[0] for i in result if any(x in i[2] for x in years)][0]

            url = urlparse.urljoin(self.base_link, result)

            result = client.source(url)
            result = client.parseDOM(result, 'div', attrs = {'id': 'episode_show'})[0]
            result = re.compile('(<a.+?</a>)').findall(result)
            result = [(client.parseDOM(i, 'a', ret='href')[0], client.parseDOM(i, 'a')[0]) for i in result]
            result = [i[0] for i in result if episode == i[1]][0]

            try: url = re.compile('//.+?(/.+)').findall(result)[0]
            except: url = result
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return


    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []

            if url == None: return sources

            url = urlparse.urljoin(self.base_link, url)

            try: url, episode = re.findall('(.+?)\?episode=(\d*)$', url)[0]
            except: episode = None

            headers = {'X-Requested-With': 'XMLHttpRequest', 'Referer': url}

            for i in range(3):
                result = client.request(url)
                if not result == None: break

            if not episode == None:
                mid = client.parseDOM(result, 'input', ret='value', attrs = {'name': 'phimid'})[0]
                url = urlparse.urljoin(self.base_link, '/ajax.php')
                post = {'ipos_server': 1, 'phimid': mid, 'keyurl': episode}
                post = urllib.urlencode(post)

                for i in range(3):
                    result = client.request(url, post=post, headers=headers, timeout='10')
                    if not result == None: break

            r = client.parseDOM(result, 'div', attrs = {'class': '[^"]*server_line[^"]*'})

            links = []

            for u in r:
                try:
                    host = client.parseDOM(u, 'p', attrs = {'class': 'server_servername'})[0]
                    host = host.strip().lower().split(' ')[-1]

                    url = urlparse.urljoin(self.base_link, '/ip.temp/swf/plugins/ipplugins.php')

                    p1 = client.parseDOM(u, 'a', ret='data-film')[0]
                    p2 = client.parseDOM(u, 'a', ret='data-server')[0]
                    p3 = client.parseDOM(u, 'a', ret='data-name')[0]
                    post = {'ipplugins': 1, 'ip_film': p1, 'ip_server': p2, 'ip_name': p3}
                    post = urllib.urlencode(post)

                    if not host in ['google', 'putlocker', 'megashare']: raise Exception()

                    for i in range(3):
                        result = client.request(url, post=post, headers=headers, timeout='10')
                        if not result == None: break

                    result = json.loads(result)['s']

                    url = urlparse.urljoin(self.base_link, '/ip.temp/swf/ipplayer/ipplayer.php')

                    post = {'u': result, 'w': '100%', 'h': '420'}
                    post = urllib.urlencode(post)

                    for i in range(3):
                        result = client.request(url, post=post, headers=headers)
                        if not result == None: break

                    url = json.loads(result)['data']

                    if type(url) is list:
                        url = [i['files'] for i in url]
                        for i in url:
                            try: sources.append({'source': 'gvideo', 'quality': client.googletag(i)[0]['quality'], 'url': i})
                            except: pass

                    else:
                        url = client.request(url)
                        url = client.parseDOM(url, 'source', ret='src', attrs = {'type': 'video.+?'})[0]
                        url += '|%s' % urllib.urlencode({'User-agent': client.randomagent()})
                        sources.append({'source': 'cdn', 'quality': 'HD','provider': 'Tunemovie', 'url': i})

                except:
                    pass

            return sources
        except Exception as e:
            control.log('ERROR tunemovie %s' % e)
            return sources


    def __resolve(self, result):
        try:
            result = client.parseDOM(result, 'div', attrs = {'id': 'player'})[0]

            try: url = client.parseDOM(result, 'iframe', ret='src')[0]
            except: pass
            try: url = base64.b64decode(re.compile('decode\("(.+?)"').findall(result)[0])
            except: pass

            if 'proxy.link=tunemovie' in url:
                url = re.compile('proxy[.]link=tunemovie[*]([^&]+)').findall(url)[-1]

                key = base64.b64decode('Q05WTmhPSjlXM1BmeFd0UEtiOGg=')
                decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationECB(key + (24 - len(key)) * '\0'))
                url = url.decode('hex')
                url = decrypter.feed(url) + decrypter.feed()

            url = resolvers.request(url)
            return url
        except:
            return


    def resolve(self, url):
        return client.googlepass(url)

