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


import re,urllib,urlparse,json,time

from resources.lib.libraries import cleantitle
from resources.lib.libraries import client
from resources.lib.libraries import control

from resources.lib import resolvers



class source:
    def __init__(self):
        self.domains = ['xmovies8.tv']
        self.base_link = 'http://xmovies8.tv'
        self.moviesearch_link = '/movie/%s-%s/'


    def get_movie(self, imdb, title, year):
        try:
            url = self.moviesearch_link % (cleantitle.geturl(title), year)
            r = urlparse.urljoin(self.base_link, url)
            r = client.request(r)
            try:
                r1 = client.parseDOM(r, 'title')[0]
                if not '(%s)' % year in r1: raise Exception()
                return url
            except:
                pass

            title = cleantitle.movie(title)
            years = ['(%s)' % str(year), '(%s)' % str(int(year)+1), '(%s)' % str(int(year)-1)]
            print("Y",url, "X ",title, r)

            r = client.parseDOM(r, 'div', attrs={'class': 'item_movie'})
            r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'img', ret='alt')[0]) for i in r]
            r = [(i[0][0], i[1], re.findall('(\d{4})', i[1])[0]) for i in r if len(i[0]) > 0 and len(i[1]) > 0]
            r = [i for i in r if title == cleantitle.movie(i[1])]
            r = [i[0] for i in r if any(x in i[1] for x in years)]
            url = re.findall('(//.+?|)(/.+)', r[0])[0][1]
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

            season, episode = '%01d' % int(season), '%01d' % int(episode)

            query = '%s season %s' % (tvshowtitle, season)
            query = self.search_link % (urllib.quote_plus(query))
            print("R",query)
            result = client.request(query)
            result = json.loads(result)
            result = result['results']

            tvshowtitle = cleantitle.tv(tvshowtitle)
            years = ['%s' % str(year), '%s' % str(int(year)+1), '%s' % str(int(year)-1)]

            result = [(i['url'], i['titleNoFormatting']) for i in result]
            result = [(i[0], re.compile('(^Watch Full "|^Watch |)(.+?[(]\d{4}[)])').findall(i[1])) for i in result]
            result = [(i[0], i[1][0][-1].lower()) for i in result if len(i[1]) > 0]
            result = [(i[0], re.compile('(.+) season (\d+)\s*[(](\d{4})[)]').findall(i[1])) for i in result]
            result = [(i[0], cleantitle.tv(i[1][0][0]), i[1][0][1], i[1][0][2]) for i in result if len(i[1]) > 0]
            result = [i for i in result if tvshowtitle == cleantitle.tv(i[1])]
            result = [i for i in result if season == i[2]]
            result = [(i[0], i[1], str(int(i[3]) - int(i[2]) + 1)) for i in result]
            result = [i[0] for i in result if any(x in i[2] for x in years)][0]

            result += '?S%02dE%02d' % (int(season), int(episode))

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
            url = path = re.sub('/watching.html$', '', url.strip('/'))
            url = referer = url + '/watching.html'
            p = client.request(url)
            p = re.findall("data\s*:\s*{\s*id:\s*(\d+),\s*episode_id:\s*(\d+),\s*link_id:\s*(\d+)", p)[0]
            p = urllib.urlencode({'id': p[0], 'episode_id': p[1], 'link_id': p[2], '_': int(time.time() * 1000)})

            headers = {
                'Accept-Formating': 'application/json, text/javascript',
                'X-Requested-With': 'XMLHttpRequest',
                'Server': 'cloudflare-nginx',
                'Referer': referer}

            r = urlparse.urljoin(self.base_link, '/ajax/movie/load_episodes')
            r = client.request(r, post=p, headers=headers)
            r = re.findall("load_player\(\s*'([^']+)'\s*,\s*'?(\d+)\s*'?", r)
            #r = [i for i in r if int(i[1]) >= 720]
            for u in r:
                try:
                    p = urllib.urlencode({'id': u[0], 'quality': u[1], '_': int(time.time() * 1000)})
                    u = urlparse.urljoin(self.base_link, '/ajax/movie/load_player_v2')

                    u = client.request(u, post=p, headers=headers)
                    u = json.loads(u)['playlist']
                    u = client.request(u, headers=headers)
                    u = json.loads(u)['playlist'][0]['sources']
                    u = [i['file'] for i in u if 'file' in i]

                    for i in u:
                        try:
                            sources.append({'source': 'gvideo', 'quality': client.googletag(i)[0]['quality'],'provider': 'Xmovies','url': i})
                        except:
                            pass
                except:
                    pass

            return sources
        except Exception as e:
            control.log('ERROR XMOVIES %s' % e)
            return sources




    def resolve(self, url):
        try:
            if url.startswith('stack://'): return url
            if 'openload' in url: return resolvers.request(url)

            url = client.request(url, output='geturl')
            if 'requiressl=yes' in url: url = url.replace('http://', 'https://')
            else: url = url.replace('https://', 'http://')
            return url
        except:
            return


