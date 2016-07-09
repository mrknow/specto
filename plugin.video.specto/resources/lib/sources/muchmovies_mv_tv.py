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


import re,urllib,urlparse, json, hashlib

from resources.lib.libraries import cleantitle
from resources.lib.libraries import client
from resources.lib.libraries import cache
from resources.lib import resolvers
from resources.lib.libraries import control
import requests




class source:
    def __init__(self):
        self.base_link = 'http://123movies.ru'
        self.search_link = '/ajax/suggest_search'
        self.info_link = '/ajax/movie_load_info/%s'
        self.server_link = '/ajax/get_episodes/%s'
        self.direct_link = '/ajax/v2_load_episode/%s'
        self.embed_link = '/ajax/load_embed/%s'


    def get_movie(self, imdb, title, year):
        try:
            t = cleantitle.get(title)
            headers = {'X-Requested-With': 'XMLHttpRequest'}
            query = urllib.urlencode({'keyword': title})
            url = urlparse.urljoin(self.base_link, self.search_link)
            r = client.request(url, post=query, headers=headers)
            print("1",r)
            r = json.loads(r)['content']
            print ("2",r)
            r = zip(client.parseDOM(r, 'a', ret='href', attrs = {'class': 'ss-title'}), client.parseDOM(r, 'a', attrs = {'class': 'ss-title'}))
            r = [i[0] for i in r if cleantitle.get(t) == cleantitle.get(i[1])][:2]
            r = [(i, re.findall('(\d+)', i)[-1]) for i in r]
            print ("3",r)

            for i in r:
                try:
                    y, q = cache.get(self.muchmovies_info, 9000, i[1])
                    print("4",y,q)
                    if not y == year: raise Exception()
                    return urlparse.urlparse(i[0]).path
                except:
                    pass
        except:
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
            year = re.findall('(\d{4})', date)[0]
            years = [str(year), str(int(year)+1), str(int(year)-1)]
            season = '%01d' % int(season)
            episode = '%01d' % int(episode)

            headers = {'X-Requested-With': 'XMLHttpRequest'}
            query = urllib.urlencode({'keyword': '%s - Season %s' % (data['tvshowtitle'], season)})
            url = urlparse.urljoin(self.base_link, self.search_link)
            r = client.request(url, post=query, headers=headers)
            r = json.loads(r)['content']
            r = zip(client.parseDOM(r, 'a', ret='href', attrs = {'class': 'ss-title'}), client.parseDOM(r, 'a', attrs = {'class': 'ss-title'}))
            r = [(i[0], re.findall('(.+?) - season (\d+)$', i[1].lower())) for i in r]
            r = [(i[0], i[1][0][0], i[1][0][1]) for i in r if len(i[1]) > 0]
            r = [i for i in r if t == cleantitle.get(i[1])]
            r = [i[0] for i in r if season == '%01d' % int(i[2])][:2]
            r = [(i, re.findall('(\d+)', i)[-1]) for i in r]

            for i in r:
                try:
                    y, q = cache.get(self.muchmovies_info, 9000, i[1])
                    if not y in years: raise Exception()
                    return urlparse.urlparse(i[0]).path + '?episode=%01d' % int(episode)
                except:
                    pass
        except:
            return

    def muchmovies_info(self, url):
        try:
            u = urlparse.urljoin(self.base_link, self.info_link)
            u = client.request(u % url)
            q = client.parseDOM(u, 'div', attrs = {'class': 'jtip-quality'})[0]
            y = client.parseDOM(u, 'div', attrs = {'class': 'jt-info'})
            y = [i.strip() for i in y if i.strip().isdigit() and len(i.strip()) == 4][0]

            return (y, q)
        except:
            return

    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []

            if url == None: return sources

            url = urlparse.urljoin(self.base_link, url)
            url = referer = url.replace('/watching.html', '')

            try: url, episode = re.findall('(.+?)\?episode=(\d*)$', url)[0]
            except: episode = None

            u = re.findall('-(\d+)', url)[-1]

            headers = {'X-Requested-With': 'XMLHttpRequest', 'Referer': url}

            quality = cache.get(self.muchmovies_info, 9000, u)[1].lower()
            if quality == 'cam' or quality == 'ts': quality = 'CAM'
            elif quality == 'hd': quality = 'HD'
            else: quality = 'SD'

            u = urlparse.urljoin(self.base_link, self.server_link % u)

            r = client.request(u, headers=headers)

            r = client.parseDOM(r, 'div', attrs = {'class': 'les-content'})
            r = zip(client.parseDOM(r, 'a', ret='onclick'), client.parseDOM(r, 'a'))
            r = [(i[0], ''.join(re.findall('(\d+)', i[1])[:1])) for i in r]

            if not episode == None:
                r = [i[0] for i in r if '%01d' % int(i[1]) == episode]
            else:
                r = [i[0] for i in r]

            r = [re.findall('(\d+),(\d+)', i) for i in r]
            r = [i[0][:2] for i in r if len(i) > 0]


            head_link = '|' + urllib.urlencode(headers)


            links = []
            links += [{'source': 'gvideo', 'url': self.direct_link % i[1]} for i in r if 2 <= int(i[0]) <= 11]
            links += [{'source': 'openload.co', 'url': self.embed_link % i[1]} for i in r if i[0] == '14']
            links += [{'source': 'videomega.tv', 'url': self.embed_link % i[1]} for i in r if i[0] == '13']
            links += [{'source': 'videowood.tv', 'url': self.embed_link % i[1]} for i in r if i[0] == '12']

            for i in links: sources.append({'source': i['source'], 'quality': quality, 'provider': 'Muchmovies', 'url': i['url'] + head_link})

            return sources
        except:
            return sources



    def resolve(self, url):
        print url
        try: headers = dict(urlparse.parse_qsl(url.rsplit('|', 1)[1]))
        except: headers = None
        url = urlparse.urljoin(self.base_link, url.split('|')[0])
        if '/ajax/v2_load_episode/' in url:
            print "Direct"
            try:
                key = "0p6b28o7j87zkmpugwwdtpkxxjpdwkuw"
                key2 = "idcnt43nrc26wxpbcfkutyk2x9vuf2ye"
                key3 = "f7sg3mfrrs5qako9nhvvqlfr7wc9la63"
                video_id = headers['Referer'].split('-')[-1].replace('/','')
                print "1"

                episode_id= url.split('/')[-1]
                coookie_1 = hashlib.md5(video_id + key).hexdigest()
                coookie_2 = hashlib.md5(episode_id + key2).hexdigest()
                coookie_3 = hashlib.md5(video_id + episode_id + key3).hexdigest()
                coookie = coookie_1 + '=' + coookie_2
                print "2"

                request_url2 = self.base_link + '/ajax/v2_load_episode/' + episode_id + '/' + coookie_3
                headers = {'Accept-Encoding': 'gzip, deflate, sdch', 'Cookie': coookie, 'Referer': headers['Referer'],
                           'user-agent': headers['User-Agent'], 'x-requested-with': 'XMLHttpRequest'}
                result = requests.get(request_url2, headers=headers).text
                #link = client.request(request_url2, headers=headers)
                print "3",url

                url = re.findall('"?file"?\s*=\s*"(.+?)"', result)
                url = [client.googletag(i) for i in url]
                url = [i[0] for i in url if len(i) > 0]

                u = []
                try: u += [[i for i in url if i['quality'] == '1080p'][0]]
                except: pass
                try: u += [[i for i in url if i['quality'] == 'HD'][0]]
                except: pass
                try: u += [[i for i in url if i['quality'] == 'SD'][0]]
                except: pass
                url = client.replaceHTMLCodes(u[0]['url'])
                if 'requiressl=yes' in url: url = url.replace('http://', 'https://')
                else: url = url.replace('https://', 'http://')
                print("url1",url)
                return url
            except:
                return
        else:
            try:
                result = client.request(url, headers=headers)
                url = json.loads(result)['embed_url']
                print("url2",url)
                return resolvers.request(url)
            except:
                return

