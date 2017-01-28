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
        self.search_link = '/ajax/movie_suggest_search.html'
        self.info_link = '/ajax/movie_info/%s.html?is_login=false'
        self.server_link = '/ajax/v3_movie_get_episodes/%s/%s/%s/movie.html'
        self.series_link = '/ajax/v3_movie_get_episodes/%s/%s/%s/series.html'
        self.url_img = '/resources/images/zootopia/%s'

        self.direct_link = '/ajax/v2_load_episode/%s'
        self.embed_link = '/ajax/load_embed/%s'
        self.key = 'xwh38if39ucx'
        self.key2 = '8qhfm9oyq1ux'
        self.key3 = 'ctiw4zlrn09tau7kqvc153uo'
        self.di8j1v = "1egh436fk3k9xwh38if39ucxh9ssnlpw0x8qhfm9oyq1uxxcmrqek0mlctiw4zlrn09tau7kqvc153uoubmv6tl738x17yypy64jpk9brwfv2rora4t59ta938cz87togvc8i72t6zz8wpy3mjd1vede3g8o1ep937i2p051u7slbt9w252fopaouuskrhk7q82k5r8hub0saxb044pgtqdcy4uadrkmxpczoyu7t6sd219ikb8h0uvz7zoh6s32"
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}


    def get_movie(self, imdb, title, year):
        try:
            r = client.request(self.base_link, limit='0', output='extended')
            cookie2 = r[4] ; headers = r[3] ; r1 = r[0]

            t = cleantitle.query2(title)
            hash = hashlib.md5(title).hexdigest()
            query = urllib.urlencode({'keyword': title, 'hash':hash})
            url = urlparse.urljoin(self.base_link, self.search_link)
            headers['X-Requested-With']= 'XMLHttpRequest'
            r = client.request(url, post=query, headers=headers)
            print "res",r
            r = json.loads(r)['content']
            r = zip(client.parseDOM(r, 'a', ret='href', attrs = {'class': 'ss-title'}), client.parseDOM(r, 'a', attrs = {'class': 'ss-title'}))
            r = [i[0] for i in r if cleantitle.get(t) == cleantitle.get(i[1])][:2]
            r = [(i, re.findall('(\d+)', i)[-1]) for i in r]
            url = None
            print r

            for i in r:
                try:
                    print i[1]
                    #y, q = cache.get(self.myesmovies_info(), 9000, i[1])
                    y, q = self.myesmovies_info(i[0])
                    print("yQ",y,q,year)
                    if not y == year:
                        print "NOT",type(y),type(year)
                        raise Exception()
                    print("URL", urlparse.urlparse(i[0]).path, i[0])
                    return urlparse.urlparse(i[0]).path
                except:
                    pass

            return url


        except Exception as e:
            control.log('Error %s' % e)
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
            print('###',t,data['tvshowtitle'])
            year = re.findall('(\d{4})', date)[0]
            years = [str(year), str(int(year)+1), str(int(year)-1)]
            season = '%01d' % int(season)
            episode = '%01d' % int(episode)

            hash = hashlib.md5(data['tvshowtitle']+' ').hexdigest()
            query = urllib.urlencode({'keyword': '%s ' % (data['tvshowtitle']), 'hash':hash})
            print query
            url = urlparse.urljoin(self.base_link, self.search_link)
            r = client.request(url, post=query, headers=self.headers)
            r = json.loads(r)['content']
            print('>>>>>>>',r)

            r = zip(client.parseDOM(r, 'a', ret='href', attrs = {'class': 'ss-title'}), client.parseDOM(r, 'a', attrs = {'class': 'ss-title'}))
            print "RRRR", r
            r = [(i[0], re.findall('(.+?) - season (\d+)$', i[1].lower())) for i in r]
            print "RRRR", r
            r = [(i[0], i[1][0][0], i[1][0][1]) for i in r if len(i[1]) > 0]
            print "RRRR", r
            r = [i for i in r if t == cleantitle.get(i[1])]
            print "RRRR", r
            print "AAA", '%01d' % int(r[0][2]), season
            r = [i[0] for i in r if season == '%01d' % int(i[2])]
            print "RRRR", r

            r = [(i, re.findall('(\d+)', i)[-1]) for i in r]
            print('>>>',r)

            for i in r:
                try:
                    y, q = cache.get(self.myesmovies_info, 9000, i[0])
                    if not y in years: raise Exception()
                    return urlparse.urlparse(i[0]).path + '?episode=%01d' % int(episode)
                except:
                    pass
        except:
            return

    def myesmovies_info(self, url):
        try:
            u = client.request(url)
            #print "U",u
            r = re.findall('<p><strong>Quality:</strong>[^"]+"quality">(.*?)</s[^R]+Release:</strong>(.*?)</p>',u)[0]
            print r
            q = str(r[0])
            y = str(r[1].strip())
            return (y, q)
        except:
            return

    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []
            agent = cache.get(client.randomagent, 180)

            if url == None: return sources

            if '?episode=' in url:
                print 'Jest serial'
                try: url, episode = re.findall('(.+?)\?episode=(\d*)$', url)[0]
                except: return sources
                episode_num = 'episode %02d:' % int(episode)
                #print episode_num, url
                url = urlparse.urljoin(self.base_link, url)
                headers = {'Referer':  url, 'User-Agent':agent}
                r100= client.request(url, limit='0', output='extended' , headers=headers)
                cookie = r100[4];headers = r100[3];r = r100[0]

                u = client.parseDOM(r,'a', ret='href', attrs = {'class': 'mod-btn mod-btn-watch'})[0]
                headers['Referer']=u
                mid, episode, server= re.findall('-(\d+)/(\d+)-(\d+)/watching\.html$', u)[0]
                u = urlparse.urljoin(self.base_link, self.series_link % (mid, server, episode))
                headers['X-Requested-With']='XMLHttpRequest'
                r = client.request(u, headers=headers, cookie=cookie)
                #print r
                #print u
                r = zip(client.parseDOM(r, 'li', ret='onclick',  attrs={'class': 'episode-item '}),client.parseDOM(r, 'li', attrs={'class': 'episode-item '}))
                r = [(i[0], client.parseDOM(i[1], 'a', ret='title')[0]) for i in r]
                #            r = [(i[0], re.findall('(.+?) - season (\d+)$', i[1].lower())) for i in r]
                r = [(re.findall('load_episode\((\d+),(\d+)\)', i[0])[0], re.findall('(.+?:)', i[1].lower())[0]) for i in r]
                #print r
                #print("Episode", episode_num)
                r = [i[0] for i in r if str(i[1]) == episode_num]
                print r

            else:
                url = urlparse.urljoin(self.base_link, url)

                url2 = urlparse.urljoin(self.base_link, self.url_img % re.findall('(\d+)', url)[0])
                headers = {'Referer':  url, 'User-Agent':agent}
                r  = client.request(url2, limit='0', output='extended' , headers=headers)
                cookie2 = r[4]; headers = r[3]; result = r[0]

                r = client.request(url, headers=headers, cookie=cookie2)
                u = client.parseDOM(r,'a', ret='href', attrs = {'class': 'mod-btn mod-btn-watch'})[0]
                headers['Referer']=u
                mid, episode, server= re.findall('-(\d+)/(\d+)-(\d+)/watching\.html$', u)[0]
                u = urlparse.urljoin(self.base_link, self.server_link % (mid, server, episode))
                headers['X-Requested-With']='XMLHttpRequest'
                r = client.request(u, headers=headers, cookie=cookie2)
                r = re.findall('onclick=\"load_episode\((\d+),(\d+)\)\"', r)
            links = []

            for i in r:
                try:
                    key_gen = self.__get_token(hash_len=6)
                    episode_id = i[0]
                    hash_id = self.uncensored(episode_id + self.di8j1v[56:80], key_gen)
                    cookie = '%s%s%s=%s; %s' % (self.di8j1v[12:24], episode_id, self.di8j1v[34:46], key_gen, cookie2)
                    request_url2 = self.base_link + '/ajax/v2_get_sources/' + episode_id + '.html?hash=' + urllib.quote(hash_id)
                    headers = {'Cookie': cookie, 'Referer': headers['Referer'],
                               'X-requested-with': 'XMLHttpRequest', 'User-Agent': agent}

                    result = client.request(request_url2, headers=headers)
                    q = json.loads(result)['playlist'][0]['sources']
                    for j in q: links.append(client.googletag(j['file'])[0])
                except Exception as e:
                    pass

            for i in links:
                sources.append({'source': 'gvideo', 'quality': i['quality'].encode('utf-8'), 'provider': 'Yesmovies', 'url': i['url'].encode('utf-8')})

            return sources
        except Exception as e:
            control.log('ERROR Yesmo %s' % e)
            return sources



    def resolve(self, url):
        return url

    def random_generator(self, size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    def __get_token(self, hash_len=16):
        chars = string.digits + string.ascii_uppercase + string.ascii_lowercase
        base = hashlib.sha512(str(int(time.time()) / 60 / 60)).digest()
        return ''.join([chars[int(ord(c) % len(chars))] for c in base[:hash_len]])

    def uncensored(self, a, b):
        c = ''
        i = 0
        for i, d in enumerate(a):
            e = b[i % len(b) - 1]
            d = int(self.__jav(d) + self.__jav(e))
            c += chr(d)

        return base64.b64encode(c)

    def __jav(self, a):
        b = str(a)
        code = ord(b[0])
        if 0xD800 <= code and code <= 0xDBFF:
            c = code
            if len(b) == 1:
                return code
            d = ord(b[1])
            return ((c - 0xD800) * 0x400) + (d - 0xDC00) + 0x10000

        if 0xDC00 <= code and code <= 0xDFFF:
            return code
        return code


    """
    function uncensored(sData, sKey) {
    var sResult = "";
    var i = 0;
    for (i = 0; i < sData.length; i++) {
        var sChar = sData.substr(i, 1);
        var sKeyChar = sKey.substr(i % sKey.length - 1, 1);
        sChar = Math.floor(jav(sChar) + jav(sKeyChar));
        sChar = String.fromCharCode(sChar);
        sResult = sResult + sChar
    }
    return encode64(sResult)
    :path:/ajax/v2_get_sources/145651.html?hash=YZZsrW5kk9ag7m2tnNSlp3Knkddu4qqpk5Nsqq6i
                v2_get_sources/145651.html?hash=mp%2Bem6SUzN/S3KPd1d3XlajXyuCg0ODZzJyemOTS
                v2_get_sources/208328.html?hash=aJpxqGZumd6i7GiwotynpW2ql99w4KWsmZtuqKml
    """
