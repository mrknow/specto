# -*- coding: utf-8 -*-

'''
    Exodus Add-on
    Copyright (C) 2016 Exodus

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


import re,urllib,urlparse,json

from resources.lib.libraries import cleantitle
from resources.lib.libraries import client
from resources.lib.libraries import cache
from resources.lib.libraries import trakt
from resources.lib.libraries import tvmaze


class source:
    def __init__(self):
        self.base_link = 'http://kissanime.io'
        self.search_link = 'http://kissanime.io/Search/?s=%s'
        self.showlist_link = '/AnimeList?c=%s&page=%s'
        self.anime_link = '/Anime/%s'


    def get_show(self, imdb, tvdb, tvshowtitle, year):
        try:
            r = 'search/tvdb/%s?type=show&extended=full' % tvdb
            r = json.loads(trakt.getTrakt(r))
            print "r1",r
            if not r: return '0'

            d = r[0]['show']['genres']
            if not ('anime' in d or 'animation' in d): return '0'

            tv_maze = tvmaze.tvMaze()
            t = tv_maze.showLookup('thetvdb', tvdb)
            t = tv_maze.showID()
            print "r2",t, tvshowtitle
            if not t: return '0'

            url = self.searchTitle(tvshowtitle)
            print "r3",url
            url = {'tvMazeID': t, 'title': tvshowtitle, 'items': url}
            url = json.dumps(url).encode('base64')
            print "URL",url

            return url
        except:
            return

    def get_episode(self, url, imdb, tvdb, title, date, season, episode):
        try:
            if url == None or url == '0': return

            info = json.loads(url.decode('base64'))

            title = info['title'] ; items = info['items']

            tv_maze = tvmaze.tvMaze(info['tvMazeID'])

            season_no = int(season)

            episode_no = tv_maze.episodeAbsoluteNumber(tvdb, int(season), int(episode))

            episode_no_base = int(episode)

            try: season_title = tv_maze.showSeasons()[season_no-1]['name']
            except: season_title = None

            try: year = int(date.split('-')[0])
            except: year = ''

            url = self.getEpisodeURL(items, season_no, episode_no, episode_no_base, title, season_title, year)

            url = re.findall('(?://.+?|)(/.+)', url)[0]
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

            r = self.getEpisodeSources(url)

            for i in r:
                try: sources.append({'source': 'gvideo', 'quality': client.googletag(i)[0]['quality'], 'provider': 'KissAnime', 'url': i, 'direct': True, 'debridonly': False})
                except: pass

            return sources
        except:
            return sources


    def resolve(self, url):
        try:
            url = client.request(url, output='geturl')
            if 'requiressl=yes' in url: url = url.replace('http://', 'https://')
            else: url = url.replace('https://', 'http://')
            return url
        except:
            return



    def searchTitle(self, title):
        try:
            result = []

            q = urlparse.urljoin(self.base_link, self.search_link % title)

            data = {
                's': title
            }
            post = urllib.urlencode(data)

            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            print "r4",q, post
            r = client.request(q, post=post, headers=headers)
            print "r5",r

            # Sometimes the search result returns nothing or the only searched item,
            # This changes the content of show instead of search results
            if (not 'Find anime' in r) or ('Not found' in r):
                try:
                    # this tries to catch the anime tv show directly if available...
                    if ('Not found' in r):
                        # makes a query url for the show
                        url_title = cleantitle.normalize(title)
                        url_title = re.sub(r'[^\w\d]', '-', url_title)
                        url_title = re.sub(r'\-+', '-', url_title)

                        q = urlparse.urljoin(self.base_link, self.anime_link % url_title)
                        
                        # requests the url
                        r = client.request(q)

                    x = client.parseDOM(r, 'div', attrs={'class': 'barContent'})[0]

                    t = client.parseDOM(x, 'a', attrs={'Class': 'bigChar'})[0]

                    if (cleantitle.get(title) == cleantitle.get(t)):
                        s = client.parseDOM(r, 'table', attrs={'class': 'listing'})[0]
                        s = self.getTableRows(s)

                        status = 0
                        for e in s:
                            match = re.search('episode\s(\d+)', e, flags=re.I)
                            if (match):
                                try:
                                    status = int( match.group(1) )
                                    break
                                except:
                                    pass

                        item = {
                            'status': status,
                            'title': title,
                            'url': str( client.parseDOM(x, 'a', ret='href', attrs={'Class': 'bigChar'})[0] )
                        }

                        try:
                            result.index( item )
                        except:
                            result.append( item )

                    return result
                except:
                    return

            r = client.parseDOM(r, 'table', attrs={'class': 'listing'})[0]
            r = re.compile("(\stitle=\'[^\']+\')", flags=re.I).sub('', r)

            # Goes through search results
            for x in self.getTableRows(r):
                try:
                    tdList = client.parseDOM(x, 'td')
                    
                    url = client.parseDOM(tdList[0], 'a', ret='href')[0]
                    ititle = client.parseDOM(tdList[0], 'a')[0].replace(' (TV)', '')
                    status = tdList[1]

                    try:
                        ititle = ititle.encode('utf-8')
                    except:
                        pass

                    try: status = int( re.sub('[^\d]', '', client.parseDOM(status, 'a')[0] ))
                    except: pass

                    if (not isinstance(status, int)):
                        status = str( cleantitle.get( status ) )

                    item = {
                        'status': status,
                        'title': ititle,
                        'url': str( url )
                    }

                    if item['status'] == 'notyetaired':
                        continue

                    try:
                        result.index( item )
                    except:
                        result.append( item )
                        pass

                except:
                    continue

            return result
        except:
            pass

        return []


    def getEpisodeURL(self, items, season_no, episode_no, episode_no_base, title, season_title, year):
        try:
            # Finds the right tv show among all the items, if available
            item = None
            if len(items) > 1:

                # Finding the tv show by its season title
                # This happens only when a show has diffrent season title than its original title
                if season_title:
                    item = self.getAbsoluteItem(items, season_title, year, season_no, episode_no)

                # Finding the tv show by its title
                if (not item):
                    item = self.getAbsoluteItem(items, title, year, season_no, episode_no)

                # Finding the tv show by its url
                if (not item):
                    item = self.getAbsoluteItem(items, title, year, season_no, episode_no, 'url')

            # Item not found, let's grab the first item in the list
            if (not item):
                item = items[0]

            # Gets the list of episodes for this show
            # Cache expires in 24 hours
            episodes = cache.get( self.getEpisodeList, 24, item )

            # Requested episode is not available
            if len(episodes) < episode_no_base:
                raise Exception()

            # Getting the episode url
            try:
                episode_url = [x['url'] for x in episodes if x['episode'] == episode_no][0]
            except:
                episode_url = [x['url'] for x in episodes if x['episode'] == episode_no_base][0]

            # Patching up the full episode URL
            return urlparse.urljoin(self.base_link, episode_url)
        except:
            pass

        return


    def getAbsoluteItem(self, titleList, title, year, season, episode, item_key = 'title'):

        romanNumbers = {
            1: 'i',         2: 'ii',        3: 'iii',
            4: 'iv',        5: 'v',         6: 'vi',
            7: 'vii',       8: 'viii',      9: 'ix',
            10: 'x',        11: 'xi',       12: 'xii',
            13: 'xiii',     14: 'xiv',      15: 'xv',
            16: 'xvi',      17: 'xvii',     18: 'xviii',
            19: 'xix',      20: 'xx'
        }

        # Cases
        cases = [
            # Season title
            # Title + 'season' + Season No + Year
            '^%sseason%s%s' % ('%s', season, year),

            # Title + 'season' + Season No
            '^%sseason%s' % ('%s', season),

            # Season with roman numbers
            # Title + Season Roman No + Year
            '^%s%s%s' % ('%s', romanNumbers.get( season , ''), year),

            # Title + Season Roman No
            '^%s%s$' % ('%s', romanNumbers.get( season , '')),

            # Season numbers
            # Title + Season No + Year
            '^%s%s%s' % ('%s', season, year),

            # Title + Season No
            '^%s%s$' % ('%s', season),

            # Title + Year
            '^%s%s' % ('%s', year),

            # Title
            '^%s$'
        ]

        # Sort the items based on priority of sub, dub
        # Later we reverse the list and dub will become the higher priority
        def sorting(item):
            title = re.sub('[^\w]', '', item[ item_key ])
            result = len(title)

            if (re.search('dub$', title, flags=re.I)):
                result -= 2

            elif (re.search('sub$', title, flags=re.I)):
                result -= 3

            return result

        titleList = sorted(titleList, key=sorting)

        # removes all space chars
        t = re.sub('\s', '', title)

        # Checks each item of titleList
        # Reverse helps to check the long title
        for x in reversed( titleList ):

            # if this item doesn't include the episode, then continue
            if (x['status'] != 'completed' and x['status'] < episode):
                continue

            # removes spaces and parantheses from title
            xx = re.sub('\s|\t|\-|\(|\)', '', x[ item_key ])
            if (item_key == 'url'):
                xx = xx.split('/').pop()

            # checks for some seasons such as 'Show Season 2', or 'Show 2' or a new season title
            for y in cases:
                # creates pattern of regular expression to search the season title
                pattern = y % t

                # trys to find dubbed titles first
                for yy in ['dub', 'sub', '']:

                    # adds 'dub' and 'sub' at the end of pattern
                    # if the pattern ends with '$' sign, moves it to the end
                    try:
                        idx = pattern.index('$')
                        if idx == len(pattern) -1:
                            yy = pattern[0:idx] + yy + '$'
                    except:
                        # add the dub, sub at the end
                        yy = pattern + yy

                    # finds the right title, if matches
                    if (re.search(yy, xx, flags=re.IGNORECASE)):
                        return x

        return


    def getEpisodeList(self, show):
        try:
            q = urlparse.urljoin(self.base_link, show['url'])

            r = client.request(q)
            r = client.parseDOM(r, 'table', attrs={'class': 'listing'})[0]

            result = []

            episode_re = re.compile(r'[^\d]+(\d+(\.\d+)?)')

            for x in self.getTableRows(r):
                try: x.index('<a ')
                except ValueError: continue
                try:
                    url = str( client.parseDOM(x, 'a', ret='href')[0] )
                    episode = client.parseDOM(x, 'a')[0]
                    try: episode = episode.encode('ascii')
                    except: pass
                    episode = episode.replace(show['title'], '')
                    episode = float(episode_re.search(episode).group(1))

                    result.append({
                        'episode': episode,
                        'url': url
                    })
                except:
                    continue

            if len(result):
                return sorted(result, key=lambda k: k['episode'])

        except:
            pass

        return


    def getEpisodeSources(self, url):
        try:
            # Video url list
            videos = []

            # Getting the page content
            r = client.request(url)

            # Grabs the direct links
            try:
                direct = client.parseDOM(r, 'select', attrs={'id': 'selectQuality'})[0]

                direct_links = client.parseDOM(direct, 'option', ret='value')
                for idx, x in enumerate( direct_links ):
                    videos.append(str(x).decode('base64'))
            except:
                pass
        except:
            pass

        return videos


    def getTableRows(self, html):
        html = re.sub('[\n\r\t]+', '', html)
        html = re.sub('>[\n\r\s]+<', '><', html)
        html = re.sub('>[\n\r\s]+', '>', html)
        html = re.sub('[\n\r\s]+<', '<', html)
        html = re.sub('\<\/tr\>', '</tr>\n', html)

        return re.findall('\<tr[^\>]*\>(.*)\<\/tr\>', html, flags=re.I)


