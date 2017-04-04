# -*- coding: utf-8 -*-

import sys
import pprint
import re
import os

# content of test_some_are_slow.py
print("CURENT PATHS",os.getcwd())

import time

def test_funcfast():
    pass

def test_funcslow1():
    time.sleep(0.1)

def test_funcslow2():
    time.sleep(0.2)

sys.path.append('../plugin.video.specto')
sys.path.append('../tests/lib')

from resources.lib.libraries import control
from resources.lib.libraries import client


result = '{"_101910349":{"type":"googlevideo.com - 720p","net":"all","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=bb8bacd315ecabfd&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6n7e&ms=nxu&mv=u&pl=24&ei=8z3iWLeWGJDUqwXe9avACw&mime=video\/mp4&lmt=1488785118826530&mt=1491221740&ip=185.66.141.239&ipbits=0&expire=1491236403&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,ei,mime,lmt&signature=A7F8434BFC3D384BF449BAE9F5629810F9F1C21B.4126CEF438DB06D23D3205A9ACFFF1ECA17BDEA8&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"16"},"_101910356":{"type":"googlevideo.com - 720p","net":"ipv4","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=12b7c40f4b089faf&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6nee&ms=nxu&mv=u&pl=32&sc=yes&ei=9zfiWIj_GpDUqwXe9avACw&mime=video\/mp4&lmt=1488799127622262&mt=1491220296&ip=2a02:5060:c170:517::3&ipbits=0&expire=1491234871&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,sc,ei,mime,lmt&signature=4429B89210833DDA4CD4B4EB335F13516CB53E1E.1DF61ABE0A43E20495397B4C77B1EDECBDF58330&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"16"},"_101910353":{"type":"googlevideo.com - 720p","net":"ipv4","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=addba3f0a50cb0ac&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6ned&ms=nxu&mv=u&pl=32&ei=xUviWMOaCdb3qQWCzKyoBA&mime=video\/mp4&lmt=1488782583944760&mt=1491225427&ip=2a02:5060:c170:517::3&ipbits=128&expire=1491239941&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,ei,mime,lmt&signature=133D5CE3E25F97A8558A17B7F69E38B43A204141.5FDA447F034F758832A101E19B4AC876377AF2AB&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"16"},"_101910350":{"type":"googlevideo.com - 480p","net":"all","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=bb8bacd315ecabfd&itag=59&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6n7e&ms=nxu&mv=u&pl=24&ei=8z3iWLeWGJDUqwXe9avACw&mime=video\/mp4&lmt=1488784603280822&mt=1491221740&ip=185.66.141.239&ipbits=0&expire=1491236403&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,ei,mime,lmt&signature=85650285AE5ED531F1AB101061A3AD2BB049BD9F.7CDEE1323A01DF55C752591632FAE7A2C04B31DE&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"13"},"_101910354":{"type":"googlevideo.com - 480p","net":"ipv4","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=addba3f0a50cb0ac&itag=59&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6ned&ms=nxu&mv=u&pl=32&ei=xUviWMOaCdb3qQWCzKyoBA&mime=video\/mp4&lmt=1488782636958624&mt=1491225427&ip=2a02:5060:c170:517::3&ipbits=128&expire=1491239941&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,ei,mime,lmt&signature=A39E41F55158D2E4DDF6894470C830A5F0B767B5.2D97AC9EE55CC68D8E5E215620B230E15D607E81&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"13"},"_101910357":{"type":"googlevideo.com - 480p","net":"ipv4","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=12b7c40f4b089faf&itag=59&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6nee&ms=nxu&mv=u&pl=32&sc=yes&ei=9zfiWIj_GpDUqwXe9avACw&mime=video\/mp4&lmt=1488799311615131&mt=1491220296&ip=2a02:5060:c170:517::3&ipbits=0&expire=1491234871&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,sc,ei,mime,lmt&signature=1886D2E3424F3432983DF8A55C327794C966F357.634C4CB06F7D639CC98BB23AD431D8F5B18A4CAF&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"13"},"_101910351":{"type":"googlevideo.com - 360p","net":"all","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=bb8bacd315ecabfd&itag=18&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6n7e&ms=nxu&mv=u&pl=24&ei=8z3iWLeWGJDUqwXe9avACw&mime=video\/mp4&lmt=1488782325271395&mt=1491221740&ip=185.66.141.239&ipbits=0&expire=1491236403&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,ei,mime,lmt&signature=AA5C31EF1E950E00189D3BFB94D63D21ED11E026.2EDC405A9EF5199ABCDC72FDD57C67E571561E0C&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"12"},"_101910352":{"type":"googlevideo.com - 360p","net":"ipv4","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=addba3f0a50cb0ac&itag=18&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6ned&ms=nxu&mv=u&pl=32&ei=xUviWMOaCdb3qQWCzKyoBA&mime=video\/mp4&lmt=1488779964761977&mt=1491225427&ip=2a02:5060:c170:517::3&ipbits=128&expire=1491239941&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,ei,mime,lmt&signature=6D26440D8F5569928C95A1835C20E6ED23AEC38C.681370C92BAF51BE41673F73542A9ACE38BC8A7A&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"12"},"_101910355":{"type":"googlevideo.com - 360p","net":"ipv4","embed":"<iframe src=\"https:\/\/redirector.googlevideo.com\/videoplayback?id=12b7c40f4b089faf&itag=18&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-5hne6nee&ms=nxu&mv=u&pl=32&sc=yes&ei=9zfiWIj_GpDUqwXe9avACw&mime=video\/mp4&lmt=1488794997513285&mt=1491220296&ip=2a02:5060:c170:517::3&ipbits=0&expire=1491234871&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,sc,ei,mime,lmt&signature=8EF8A6208F47BA1441549636ABD6CED3E53D8D5E.2EC37A6231CD93D0ABC3380B4D5711D9D9F461B7&key=ck2&app=explorer\" width=\"870\" height=\"505\" frameborder=\"0\" allowfullscreen><\/iframe>","weight":"12"},"_94498277":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/nsP1R0Xp6CU\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_87759602":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/dK63z5RxUIk\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_87750122":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/msrEBxYyS4U\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_93769960":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/vSOYdsq_ugA\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_87752017":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/Qouq-7YqzaA\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_93904860":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/XBKBPQIHBRA\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_94325437":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/D3_pWz7Pa9c\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_87749029":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/HAo7hDnQf2I\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_91171693":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/LoTUwrTp8dU\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_91755337":{"type":"openload.co","net":"all","embed":"<IFRAME SRC=\"https:\/\/openload.co\/embed\/rZdIHUtkDU8\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"11"},"_96411987":{"type":"streamango.com","net":"all","embed":"<IFRAME SRC=\"https:\/\/streamango.com\/embed\/nppnldkrnmrdeckd\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"0"},"_95225781":{"type":"streamango.com","net":"all","embed":"<IFRAME SRC=\"https:\/\/streamango.com\/embed\/kbkkqkqefafofebk\/\" allowfullscreen=\"true\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO WIDTH=870 HEIGHT=505>  <\/IFRAME>","weight":"0"}}'
import json
#print "u'https://streamango.com/embed/nppnldkrnmrdeckd/'"

#result = result.replace('\\','')
#result = result.replace('"','\'')
result = """
<!DOCTYPE html>
<!--[if IE 9]> <html lang="en" class="ie9"> <![endif]-->
<!--[if !IE]><!-->
<html lang="en">
    <!--<![endif]-->
    <!-- BEGIN HEAD -->
    <head>
        <meta charset="utf-8" />
                <title>Watch The Walking Dead - Season 7 (2016) free online | watch free movies - tv series online</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1"/>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8">
        <meta name="description" content="Watch The Walking Dead - Season 7 (2016) - Sheriff Deputy Rick Grimes leads a group of survivors in a world overrun by the walking dead. Fighting the dead, fearing the living."/>
        <meta name="keywords" content="the-walking-dead-2016,andrew lincoln,chandler riggs,norman reedus,melissa mcbride"/>
        <meta property="fb:app_id" content="1776704499243260" />
        <meta property="og:type" content="website"/>
        <meta property="article:publisher" content="https://www.facebook.com/1movies.tv"/>
                    <meta property="og:url" content="http://1movies.tv/film/the-walking-dead-2016.50318/"/>
                <meta property="og:image" content="http://img.1movies.tv/crop/215/310/media/images/160815_044247/images.jpg"/>
        <meta property="og:title" content="Watch The Walking Dead - Season 7 (2016) free online | watch free movies - tv series online"/>
        <meta property="og:description" content="Watch The Walking Dead - Season 7 (2016) - Sheriff Deputy Rick Grimes leads a group of survivors in a world overrun by the walking dead. Fighting the dead, fearing the living."/>
        <meta property="og:site_name" content="1movies.tv"/>
        <meta name="revisit-after" content="1 days">
                            <link href="http://1movies.tv/film/the-walking-dead-2016.50318/" rel="canonical" />
                <link rel="shortcut icon" type="image/x-icon" href="//1movies.tv/themes/v2/images/favicon.png"/>
        <link href="//1movies.tv/themes/v2/css/bootstrap.min.css" rel="stylesheet">
        <link href="//1movies.tv/themes/v2/css/style.min.css?v=1.2.1" rel="stylesheet">
        <script src="//1movies.tv/themes/v2/js/jquery.min.js?v=1.1.1"></script>
        <script>
            var rootDomain = '//1movies.tv';
        </script>
    </head>
    <body class="home">
        <div id="fb-root"></div>
        <div id="wrapper" class="full">
            <div id="header" class="full">
                <div class="container">
                    <div class="row">
                        <div class="visible-sm visible-md visible-lg header_desk">
                            <div class="col-xs-12 col-sm-2 col-md-2">
                                <a class="logo" href="//1movies.tv" title="1Movies - Free Movies Online"><img src="//1movies.tv/themes/v2/images/1movies-logo-50.png" alt="1Movies - Free Movies Online"></a>
                            </div>
                            <div class="col-menu col-xs-12 col-sm-9 col-md-7">
                                <ul id="main_menu">
    <li class="normal_menu_item has_child">
        <a href="/genre/" title="Genre">Genre</a>
        <ul class="sub_menu col4">
            <li> <a title="Action movies" href="/genre/action"><i class="fa fa-angle-right" aria-hidden="true"></i> Action</a> </li>
            <li> <a title="Adventure movies" href="/genre/adventure"><i class="fa fa-angle-right" aria-hidden="true"></i> Adventure</a> </li>
            <li> <a title="Animation movies" href="/genre/animation"><i class="fa fa-angle-right" aria-hidden="true"></i> Animation</a> </li>
            <li> <a title="Biography movies" href="/genre/biography"><i class="fa fa-angle-right" aria-hidden="true"></i> Biography</a> </li>
            <li> <a title="Comedy movies" href="/genre/comedy"><i class="fa fa-angle-right" aria-hidden="true"></i> Comedy</a> </li>
            <li> <a title="Crime movies" href="/genre/crime"><i class="fa fa-angle-right" aria-hidden="true"></i> Crime</a> </li>
            <li> <a title="Documentary movies" href="/genre/documentary"><i class="fa fa-angle-right" aria-hidden="true"></i> Documentary</a> </li>
            <li> <a title="Drama movies" href="/genre/drama"><i class="fa fa-angle-right" aria-hidden="true"></i> Drama</a> </li>
            <li> <a title="Family movies" href="/genre/family"><i class="fa fa-angle-right" aria-hidden="true"></i> Family</a> </li>
            <li> <a title="Fantasy movies" href="/genre/fantasy"><i class="fa fa-angle-right" aria-hidden="true"></i> Fantasy</a> </li>
            <li> <a title="Game-show movies" href="/genre/game-show"><i class="fa fa-angle-right" aria-hidden="true"></i> Game show</a> </li>
            <li> <a title="History movies" href="/genre/history"><i class="fa fa-angle-right" aria-hidden="true"></i> History</a> </li>
            <li> <a title="Horror movies" href="/genre/horror"><i class="fa fa-angle-right" aria-hidden="true"></i> Horror</a> </li>
            <li> <a title="Movie-horror movies" href="/genre/movie-horror"><i class="fa fa-angle-right" aria-hidden="true"></i> Movie horror</a> </li>
            <li> <a title="Music movies" href="/genre/music"><i class="fa fa-angle-right" aria-hidden="true"></i> Music</a> </li>
            <li> <a title="Musical movies" href="/genre/musical"><i class="fa fa-angle-right" aria-hidden="true"></i> Musical</a> </li>
            <li> <a title="Mystery movies" href="/genre/mystery"><i class="fa fa-angle-right" aria-hidden="true"></i> Mystery</a> </li>
            <li> <a title="News movies" href="/genre/news"><i class="fa fa-angle-right" aria-hidden="true"></i> News</a> </li>
            <li> <a title="Reality-tv movies" href="/genre/reality-tv"><i class="fa fa-angle-right" aria-hidden="true"></i> Reality TV</a> </li>
            <li> <a title="Romance movies" href="/genre/romance"><i class="fa fa-angle-right" aria-hidden="true"></i> Romance</a> </li>
            <li> <a title="Sci-fi movies" href="/genre/sci-fi"><i class="fa fa-angle-right" aria-hidden="true"></i> Sci-fi</a> </li>
            <li> <a title="Short movies" href="/genre/short"><i class="fa fa-angle-right" aria-hidden="true"></i> Short</a> </li>
            <li> <a title="Sport movies" href="/genre/sport"><i class="fa fa-angle-right" aria-hidden="true"></i> Sport</a> </li>
            <li> <a title="Talk-show movies" href="/genre/talk-show"><i class="fa fa-angle-right" aria-hidden="true"></i> Talk show</a> </li>
            <li> <a title="Thriller movies" href="/genre/thriller"><i class="fa fa-angle-right" aria-hidden="true"></i> Thriller</a> </li>
            <li> <a title="Tv series movies" href="/genre/tv-series"><i class="fa fa-angle-right" aria-hidden="true"></i> TV Series</a> </li>
            <li> <a title="War movies" href="/genre/war"><i class="fa fa-angle-right" aria-hidden="true"></i> War</a> </li>
            <li> <a title="Western movies" href="/genre/western"><i class="fa fa-angle-right" aria-hidden="true"></i> Western</a> </li>
        </ul>
    </li>
    <li class="normal_menu_item has_child">
        <a href="/country/" title="Country">Country</a>
        <ul class="sub_menu col3">
            <li><a href="/country/usa" title="Usa"><i class="fa fa-angle-right" aria-hidden="true"></i> Usa</a></li>
            <li><a href="/country/india" title="India"><i class="fa fa-angle-right" aria-hidden="true"></i> India</a></li>
            <li><a href="/country/uk" title="Uk"><i class="fa fa-angle-right" aria-hidden="true"></i> Uk</a></li>
            <li><a href="/country/france" title="France"><i class="fa fa-angle-right" aria-hidden="true"></i> France</a></li>
            <li><a href="/country/japan" title="Japan"><i class="fa fa-angle-right" aria-hidden="true"></i> Japan</a></li>
            <li><a href="/country/china" title="China"><i class="fa fa-angle-right" aria-hidden="true"></i> China</a></li>
            <li><a href="/country/south-korea" title="South Korea"><i class="fa fa-angle-right" aria-hidden="true"></i> South korea</a></li>
            <li><a href="/country/hong-kong" title="Hong Kong"><i class="fa fa-angle-right" aria-hidden="true"></i> Hong Kong</a></li>
            <li><a href="/country/australia" title="Australia"><i class="fa fa-angle-right" aria-hidden="true"></i> Australia</a></li>
            <li><a href="/country/canada" title="Canada"><i class="fa fa-angle-right" aria-hidden="true"></i> Canada</a></li>
            <li><a href="/country/germany" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> Germany</a></li>
            <li><a href="/country/italy" title="Italy"><i class="fa fa-angle-right" aria-hidden="true"></i> Italy</a></li>
            <li><a href="/country/south-africa" title="South Africa"><i class="fa fa-angle-right" aria-hidden="true"></i> South Africa</a></li>
            <li><a href="/country/spain" title="Spain"><i class="fa fa-angle-right" aria-hidden="true"></i> Spain</a></li>
            <li><a href="/country/mexico" title="Mexico"><i class="fa fa-angle-right" aria-hidden="true"></i> Mexico</a></li>
            <li><a href="/country/new-zealand" title="New Zealand"><i class="fa fa-angle-right" aria-hidden="true"></i> New Zealand</a></li>
            <li><a href="/country/russia" title="Russia"><i class="fa fa-angle-right" aria-hidden="true"></i> Russia</a></li>
            <li><a href="/country/philippines" title="Philippines"><i class="fa fa-angle-right" aria-hidden="true"></i> Philippines</a></li>
            <li><a href="/country/denmark" title="Denmark"><i class="fa fa-angle-right" aria-hidden="true"></i> Denmark</a></li>
            <li><a href="/country/netherlands" title="Netherlands"><i class="fa fa-angle-right" aria-hidden="true"></i> Netherlands</a></li>
            <li><a href="/country/sweden" title="Sweden"><i class="fa fa-angle-right" aria-hidden="true"></i> Sweden</a></li>
            <li><a href="/country/thailand" title="Thailand"><i class="fa fa-angle-right" aria-hidden="true"></i> Thailand</a></li>
            <li><a href="/country/ireland" title="Ireland"><i class="fa fa-angle-right" aria-hidden="true"></i> Ireland</a></li>
            <li><a href="/country/belgium" title="Belgium"><i class="fa fa-angle-right" aria-hidden="true"></i> Belgium</a></li>
        </ul>
    </li>
    <li class="normal_menu_item"><a href="/movies/hot" title="Free hot movies">HOT Movies</a></li>
    <li class="normal_menu_item"><a href="/movies/series" title="Free TV Series">TV Series</a></li>
    <li class="normal_menu_item"><a href="/movies/mostviewed" title="Most Viewed">Most Watched</a></li>
    <li class="normal_menu_item"><a href="/movies/latest" title="Latest">Latest</a></li>
    <li class="normal_menu_item"><a href="/request" title="Request">Request</a></li>
</ul>                            </div>
                            <div id="search_user_top" class="col-xs-12 col-sm-1 col-md-3">
                                <div class="row">
                                    <div class="hidden-sm hidden-xs col-xs-12 col-md-9">
                                        <div class="full search_top">
                                            <form action="/movies/search" method="GET" accept-charset="utf-8">
                                                <input class="form-control" type="text" name="s" value="" placeholder="Start typing & press &#34;Enter&#34;">
                                                <button><i class="fa fa-search"></i></button>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="visible-xs visible-sm header_mobile">
                            <div class="col-xs-12 col-sm-12">
                                <div class="mobile-menu"><i class="fa fa-reorder"></i></div>
                                <div class="mobile-search"><i class="fa fa-search"></i></div>
                                <a class="logo" href="//1movies.tv" title="1Movies - Free Movies Online"><img src="//1movies.tv/themes/v2/images/1movies-logo-50.png" alt="1Movies - Free Movies Online"></a>
                                <div class="login_info">
                                    <a class="btn btn-default login_btn_header" href="javascript:void(0)" title="Checking ...">...</a>
                                </div>
                            </div>
                            <div class="col-menu col-xs-12 col-sm-12">
                                <div id="mobile_menu">
                                    <ul id="main_menu">
    <li class="normal_menu_item has_child">
        <a href="/genre/" title="Genre">Genre</a>
        <ul class="sub_menu col4">
            <li> <a title="Action movies" href="/genre/action"><i class="fa fa-angle-right" aria-hidden="true"></i> Action</a> </li>
            <li> <a title="Adventure movies" href="/genre/adventure"><i class="fa fa-angle-right" aria-hidden="true"></i> Adventure</a> </li>
            <li> <a title="Animation movies" href="/genre/animation"><i class="fa fa-angle-right" aria-hidden="true"></i> Animation</a> </li>
            <li> <a title="Biography movies" href="/genre/biography"><i class="fa fa-angle-right" aria-hidden="true"></i> Biography</a> </li>
            <li> <a title="Comedy movies" href="/genre/comedy"><i class="fa fa-angle-right" aria-hidden="true"></i> Comedy</a> </li>
            <li> <a title="Crime movies" href="/genre/crime"><i class="fa fa-angle-right" aria-hidden="true"></i> Crime</a> </li>
            <li> <a title="Documentary movies" href="/genre/documentary"><i class="fa fa-angle-right" aria-hidden="true"></i> Documentary</a> </li>
            <li> <a title="Drama movies" href="/genre/drama"><i class="fa fa-angle-right" aria-hidden="true"></i> Drama</a> </li>
            <li> <a title="Family movies" href="/genre/family"><i class="fa fa-angle-right" aria-hidden="true"></i> Family</a> </li>
            <li> <a title="Fantasy movies" href="/genre/fantasy"><i class="fa fa-angle-right" aria-hidden="true"></i> Fantasy</a> </li>
            <li> <a title="Game-show movies" href="/genre/game-show"><i class="fa fa-angle-right" aria-hidden="true"></i> Game show</a> </li>
            <li> <a title="History movies" href="/genre/history"><i class="fa fa-angle-right" aria-hidden="true"></i> History</a> </li>
            <li> <a title="Horror movies" href="/genre/horror"><i class="fa fa-angle-right" aria-hidden="true"></i> Horror</a> </li>
            <li> <a title="Movie-horror movies" href="/genre/movie-horror"><i class="fa fa-angle-right" aria-hidden="true"></i> Movie horror</a> </li>
            <li> <a title="Music movies" href="/genre/music"><i class="fa fa-angle-right" aria-hidden="true"></i> Music</a> </li>
            <li> <a title="Musical movies" href="/genre/musical"><i class="fa fa-angle-right" aria-hidden="true"></i> Musical</a> </li>
            <li> <a title="Mystery movies" href="/genre/mystery"><i class="fa fa-angle-right" aria-hidden="true"></i> Mystery</a> </li>
            <li> <a title="News movies" href="/genre/news"><i class="fa fa-angle-right" aria-hidden="true"></i> News</a> </li>
            <li> <a title="Reality-tv movies" href="/genre/reality-tv"><i class="fa fa-angle-right" aria-hidden="true"></i> Reality TV</a> </li>
            <li> <a title="Romance movies" href="/genre/romance"><i class="fa fa-angle-right" aria-hidden="true"></i> Romance</a> </li>
            <li> <a title="Sci-fi movies" href="/genre/sci-fi"><i class="fa fa-angle-right" aria-hidden="true"></i> Sci-fi</a> </li>
            <li> <a title="Short movies" href="/genre/short"><i class="fa fa-angle-right" aria-hidden="true"></i> Short</a> </li>
            <li> <a title="Sport movies" href="/genre/sport"><i class="fa fa-angle-right" aria-hidden="true"></i> Sport</a> </li>
            <li> <a title="Talk-show movies" href="/genre/talk-show"><i class="fa fa-angle-right" aria-hidden="true"></i> Talk show</a> </li>
            <li> <a title="Thriller movies" href="/genre/thriller"><i class="fa fa-angle-right" aria-hidden="true"></i> Thriller</a> </li>
            <li> <a title="Tv series movies" href="/genre/tv-series"><i class="fa fa-angle-right" aria-hidden="true"></i> TV Series</a> </li>
            <li> <a title="War movies" href="/genre/war"><i class="fa fa-angle-right" aria-hidden="true"></i> War</a> </li>
            <li> <a title="Western movies" href="/genre/western"><i class="fa fa-angle-right" aria-hidden="true"></i> Western</a> </li>
        </ul>
    </li>
    <li class="normal_menu_item has_child">
        <a href="/country/" title="Country">Country</a>
        <ul class="sub_menu col3">
            <li><a href="/country/usa" title="Usa"><i class="fa fa-angle-right" aria-hidden="true"></i> Usa</a></li>
            <li><a href="/country/india" title="India"><i class="fa fa-angle-right" aria-hidden="true"></i> India</a></li>
            <li><a href="/country/uk" title="Uk"><i class="fa fa-angle-right" aria-hidden="true"></i> Uk</a></li>
            <li><a href="/country/france" title="France"><i class="fa fa-angle-right" aria-hidden="true"></i> France</a></li>
            <li><a href="/country/japan" title="Japan"><i class="fa fa-angle-right" aria-hidden="true"></i> Japan</a></li>
            <li><a href="/country/china" title="China"><i class="fa fa-angle-right" aria-hidden="true"></i> China</a></li>
            <li><a href="/country/south-korea" title="South Korea"><i class="fa fa-angle-right" aria-hidden="true"></i> South korea</a></li>
            <li><a href="/country/hong-kong" title="Hong Kong"><i class="fa fa-angle-right" aria-hidden="true"></i> Hong Kong</a></li>
            <li><a href="/country/australia" title="Australia"><i class="fa fa-angle-right" aria-hidden="true"></i> Australia</a></li>
            <li><a href="/country/canada" title="Canada"><i class="fa fa-angle-right" aria-hidden="true"></i> Canada</a></li>
            <li><a href="/country/germany" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> Germany</a></li>
            <li><a href="/country/italy" title="Italy"><i class="fa fa-angle-right" aria-hidden="true"></i> Italy</a></li>
            <li><a href="/country/south-africa" title="South Africa"><i class="fa fa-angle-right" aria-hidden="true"></i> South Africa</a></li>
            <li><a href="/country/spain" title="Spain"><i class="fa fa-angle-right" aria-hidden="true"></i> Spain</a></li>
            <li><a href="/country/mexico" title="Mexico"><i class="fa fa-angle-right" aria-hidden="true"></i> Mexico</a></li>
            <li><a href="/country/new-zealand" title="New Zealand"><i class="fa fa-angle-right" aria-hidden="true"></i> New Zealand</a></li>
            <li><a href="/country/russia" title="Russia"><i class="fa fa-angle-right" aria-hidden="true"></i> Russia</a></li>
            <li><a href="/country/philippines" title="Philippines"><i class="fa fa-angle-right" aria-hidden="true"></i> Philippines</a></li>
            <li><a href="/country/denmark" title="Denmark"><i class="fa fa-angle-right" aria-hidden="true"></i> Denmark</a></li>
            <li><a href="/country/netherlands" title="Netherlands"><i class="fa fa-angle-right" aria-hidden="true"></i> Netherlands</a></li>
            <li><a href="/country/sweden" title="Sweden"><i class="fa fa-angle-right" aria-hidden="true"></i> Sweden</a></li>
            <li><a href="/country/thailand" title="Thailand"><i class="fa fa-angle-right" aria-hidden="true"></i> Thailand</a></li>
            <li><a href="/country/ireland" title="Ireland"><i class="fa fa-angle-right" aria-hidden="true"></i> Ireland</a></li>
            <li><a href="/country/belgium" title="Belgium"><i class="fa fa-angle-right" aria-hidden="true"></i> Belgium</a></li>
        </ul>
    </li>
    <li class="normal_menu_item"><a href="/movies/hot" title="Free hot movies">HOT Movies</a></li>
    <li class="normal_menu_item"><a href="/movies/series" title="Free TV Series">TV Series</a></li>
    <li class="normal_menu_item"><a href="/movies/mostviewed" title="Most Viewed">Most Watched</a></li>
    <li class="normal_menu_item"><a href="/movies/latest" title="Latest">Latest</a></li>
    <li class="normal_menu_item"><a href="/request" title="Request">Request</a></li>
</ul>                                </div>
                            </div>
                            <div class="col-xs-12 col-sm-12">
                                <div id="search_top_mobile" class="full search_top">
                                    <form action="/movies/search" method="GET" accept-charset="utf-8">
                                        <input class="form-control" type="text" name="s" value="" placeholder="Start typing & press &#34;Enter&#34;">
                                        <button><i class="fa fa-search"></i></button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
<script src="//1movies.tv/themes/v2/js/jwplayer/jwplayer.js"></script>
<script>jwplayer.key = "KRFX25WxJEUkqgxrEq4D7PSF4qjJzUhWXWqAOg==";</script>
<script src="//content.jwplatform.com/libraries/j5gvXQ3A.js"></script>
<script type="text/javascript" src="//1movies.tv/themes/v2/js/player.js?v=1.1.3"></script>
<script type="text/javascript">
    var movie = {
        id: 12382,
        name: "The Walking Dead - Season 7 (2016)",
        slug: "the-walking-dead-2016.50318",
        episode_slug: "12",
    };
    $(document).ready(function () {
        $.ajax("/ajax/movie/update_view", {
            cache: false,
            type: 'GET',
            data: {
                id: 12382            },
            success: function (result) {

            }
        });
        $("#movie-player a").attr('href', 'javascript:void(0)').attr('onclick', 'startPlayVideo();');
        $("#movie-player a").html('<span class="play-icon"><i class="themeum-moviewplay"></i></span>');
    });
    function startPlayVideo() {
        load_player(72195);
    }
    function showError(message) {
        $("#movie-player").html('<div style="top: 25%; z-index: 15; position: relative; width: 50%; left: 25%;" class="alert alert-danger notice" role="alert"> <i class="fa fa-exclamation-circle"></i> ' + message + '</div>');
    }
</script>
<style>
    .detail_content .cover {
        height: 100%;
        background-position: 50% 25%;
        background-size: cover;
        position: relative
    }
    .detail_content .cover:after {
        content: "";
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background: rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease 0s;
        -webkit-transition: all 0.3s ease 0s
    }
    .detail_content .cover:hover:after {
        background: rgba(0, 0, 0, 0.1);
        box-shadow: 0 0 150px rgba(0, 0, 0, 0.4) inset
    }
    .detail_content .cover .play-icon {
        position: absolute;
        left: 50%;
        top: 50%;
        font-size: 110px;
        color: #e62117;
        line-height: 0;
        width: 110px;
        text-align: center;
        z-index: 999;
        -webkit-transform: translate(-50%, -50%) scale(0.8);
        transform: translate(-50%, -50%) scale(0.8);
        transition: 300ms;
        -webkit-transition: 300ms
    }
    .detail_content .cover:hover .play-icon {
        -webkit-transform: translate(-50%, -50%) scale(1);
        transform: translate(-50%, -50%) scale(1)
    }
    .detail_content .cover .play-icon:hover {
        color: #4bb8df
    }
</style>
<div id="main" class="full">
        <div id="bread" class="full">
        <div class="container">
            <ul class="breadcrumb">
                                    <li itemtype="http://data-vocabulary.org/Breadcrumb" itemscope="" >
                                                    <a title="Home" itemprop="url" href="//1movies.tv">
                                <span itemprop="title">Home</span>
                            </a>
                                            </li>
                                    <li itemtype="http://data-vocabulary.org/Breadcrumb" itemscope="" >
                                                    <a title="drama" itemprop="url" href="//1movies.tv/genre/drama">
                                <span itemprop="title">Drama</span>
                            </a>
                                            </li>
                                    <li itemtype="http://data-vocabulary.org/Breadcrumb" itemscope="" class="active">
                                                    <span itemprop="title">The Walking Dead - Season 7 (2016)</span>
                                            </li>
                            </ul>
        </div>
    </div>
<script src="//ad.1movies.tv/1m/script.php?id=ADS_ATF&mob=true&v=725928619" type="text/javascript"></script>    <div id="single_block" class="full block_movies watch_movie">
        <div class="container">
            <div class="main-detail">
                <div class="full detail_content">
                    <link itemprop="url" href="//1movies.tv/film/the-walking-dead-2016.50318" />
                    <meta itemprop="name" content="The Walking Dead - Season 7 (2016)" />
                    <meta itemprop="description" content="Sheriff Deputy Rick Grimes leads a group of survivors in a world overrun by the walking dead. Fighting the dead, fearing the living." />
                    <meta itemprop="duration" content="PT3H2M33S" />
                    <link itemprop="thumbnailUrl" href="//img.1movies.tv/crop/215/310/media/images/160815_044247/images.jpg" />
                    <span itemprop="thumbnail" itemscope itemtype="http://schema.org/ImageObject">
                        <link itemprop="url" href="//img.1movies.tv/crop/215/310/media/images/160815_044247/images.jpg" />
                        <meta itemprop="width" content="215" />
                        <meta itemprop="height" content="310" />
                    </span>
                    <div class="alert alert-success notice" role="alert"> <i class="fa fa-exclamation-circle"></i> Scroll down and click to choose episode/server you want to watch.<br> If you don't hear the sounds, please try another server or use Desktop browsers to watch.<br> If you got error message, please press Ctrl + F5 or clear your browser cache and try again.</div>
                    <div class="ovf_watch"></div>
                    <div id="player-embed" class="full" style="background: #000;">
                        <div id="movie-player">
                            <a title="The Walking Dead - Season 7 (2016)" href="#" style="background-image:url(//img.1movies.tv/media/images/161128_024014/the-walking-dead-season-7.jpg)" class="cover full">
                                <div id="movie-loading"><div class="pacman"><div></div><div></div><div></div><div></div><div></div></div></div>
                            </a>
                        </div>
                        <div id="bar-player" class="full">
                            <a id="offlight" href="javascript:void(0)" title="Turn off light"><i class="fa fa-lightbulb-o" aria-hidden="true"></i> <span>Turn off light</span></a>
                            <a id="m-dl-button" class="btn-download" href="javascript:void(0)" data-toggle="modal" data-target="#DownloadModal" rel="1"><i class="fa fa-download"></i> <span>Download</span></a>
                            <a id="cmt" href="#commentfb" title="comment facebook"><i class="fa fa-comments-o"></i> <span>Comment (<span id="comment-count"><span class="fb-comments-count" data-href="http://1movies.tv/movie/the-walking-dead-2016/watching.html"></span></span>)</span></a>
                            <p><i class="fa fa-eye" aria-hidden="true"></i> <span>3,403,292 views</span></p>
                        </div>
                    </div>
                    <!-- download popup -->
                    <div class="modal fade" id="DownloadModal" tabindex="-1" role="dialog" aria-labelledby="DownloadModal">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header" style="background:#eee;border-radius: 6px 6px 0 0;"><span style="font-size:20px;">Download</span>
                                    <a style="color:red;" href="#" class="close" data-dismiss="modal" aria-label="Close"><i class="fa fa-times"></i></a>
                                </div>
                                <div style="padding:20px;">
                                    <h2 style="font-size:14px;"><strong>The Walking Dead - Season 7 (2016)</strong></h2>
                                    <br>
                                    <div id="download_links"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- download popup -->
                    <div class="full watch_info">
                                                                                                                <div class="full watch_info">
                                    <div class="full list_ep">
                                        <div class="col-xs-12 col-sm-12 col-md-12 nopadding">
                                            <div class="ep_link full">
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=63326" class="">Episode 1</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=63674" class="">Episode 2</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=64184" class="">Episode 3</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=65006" class="">Episode 4</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=66783" class="">Episode 5</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=67150" class="">Episode 6</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=67610" class="">Episode 7</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=68023" class="">Episode 8</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=71329" class="">Episode 9</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=71608" class="">Episode 10</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=71890" class="">Episode 11</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72195" class="active">Episode 12</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72436" class="">Episode 13</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72746" class="">Episode 14</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72978" class="">Episode 15</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=73231" class="">Episode 16</a>
                                                                                            </div>
                                        </div>
                                    </div>
                                </div>
                                                        <div class="full list_server"></div>
                                            </div>
                    <div class="info_movie full">
                        <div class="col-xs-12 col-sm-7 col-md-10">
                            <div class="full desc">
                                <div class="row">
                                    <div class="col-s-12 col-sm-12 col-md-6 col-lg-7">
                                        <div class="tit full">
                                            <h1>The Walking Dead - Season 7 (2016)</h1>
                                            <a href="#trailer" data-toggle="modal" data-target="#pop-trailer" class="btn btn-default"><i class="fa fa-film" aria-hidden="true"></i> Trailer</a>
                                            <div class="modal fade modal-cuz" id="pop-trailer" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                                                <div class="modal-dialog">
                                                    <div class="modal-content">
                                                        <div class="modal-header">
                                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><i class="fa fa-close"></i>
                                                            </button>
                                                            <h4 class="modal-title" id="myModalLabel">Trailer: The Walking Dead - Season 7 (2016)</h4>
                                                        </div>
                                                        <div class="modal-body">
                                                            <iframe width="800" height="400" src="https://www.youtube.com/embed/pSEauoJtLF0" frameborder="0" allowfullscreen></iframe>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-s-12 col-sm-12 col-md-6 col-lg-5">
                                        <div class="full share">
                                            <script type="text/javascript">
                                                var addthis_share = {
                                                    url: "http://1movies.tv/film/the-walking-dead-2016/",
                                                }
                                            </script>
                                            <div class="addthis_native_toolbox"></div>
                                        </div>
                                    </div>
                                </div>
                                <div class="full excerpt">
                                    <p>Sheriff Deputy Rick Grimes leads a group of survivors in a world overrun by the walking dead. Fighting the dead, fearing the living.</p>
                                </div>
                                <div class="full specs">
                                    <div class="row">
                                        <div class="col-xs-12 col-sm-6">
                                            <div class="specs_left full">
                                                <p><strong>Genre: </strong><a href="/genre/drama" title="Drama">Drama</a>, <a href="/genre/horror" title="Horror">Horror</a>, <a href="/genre/sci-fi" title="Sci-fi">Sci-fi</a></p>
                                                <p><strong>Actor: </strong><a href="/actor/andrew-lincoln" title="Andrew Lincoln">Andrew Lincoln</a>, <a href="/actor/chandler-riggs" title="Chandler Riggs">Chandler Riggs</a>, <a href="/actor/norman-reedus" title="Norman Reedus">Norman Reedus</a>, <a href="/actor/melissa-mcbride" title="Melissa Mcbride">Melissa Mcbride</a></p>
                                                <p><strong>Director: </strong><a href="/director/n-a" title="N/a">N/a</a></p>
                                                <p><strong>Writer: </strong><a href="/writer/frank-darabont" title="Frank Darabont">Frank Darabont</a></p>
                                                <p><strong>Country: </strong><a href="/country/usa" title="Usa">Usa</a></p>
                                            </div>
                                        </div>
                                        <div class="col-xs-12 col-sm-6">
                                            <div class="specs_right full">
                                                <p><strong>Runtime:</strong> 44 min</p>
                                                <p><strong>Quality:</strong> <span class="quality">HD</span></p>
                                                <p><strong>Release:</strong> 31 Oct 2010</p>
                                                <p><strong>IMDb:</strong> 8.6/10</p>
                                                <p><strong>Language: </strong><a href="/language/english" title="English">English</a></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-xs-12 col-sm-5 col-md-2 hidden-xs">
                            <img src="//img.1movies.tv/resize/500/250/media/images/160815_044247/images.jpg" alt="The Walking Dead - Season 7 (2016)">
                        </div>
                    </div>
                    <div class="full footer_detail">
                        <strong><i class="fa fa-hashtag"></i> Tags:</strong>
                        <a href="/tags/the-walking-dead-2016" title="The-walking-dead-2016">The-walking-dead-2016</a> <a href="/tags/andrew-lincoln" title="Andrew Lincoln">Andrew Lincoln</a> <a href="/tags/chandler-riggs" title="Chandler Riggs">Chandler Riggs</a> <a href="/tags/norman-reedus" title="Norman Reedus">Norman Reedus</a> <a href="/tags/melissa-mcbride" title="Melissa Mcbride">Melissa Mcbride</a>                    </div>
                </div>
                <div id="block_cmt" class="full">
                    <div class="col-xs-12 col-sm-12 col-md-12">
                        <div id="disqus_thread"></div>
                        <script>
                            var disqus_config = function () {
                                this.page.url = "http://1movies.tv/film/the-walking-dead-2016/";  // Replace PAGE_URL with your page's canonical URL variable
                                this.page.identifier = "http://1movies.tv/film/the-walking-dead-2016/"; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
                            };

                            (function () { // DON'T EDIT BELOW THIS LINE
                                var d = document, s = d.createElement('script');
                                s.src = '//motmovies.disqus.com/embed.js';
                                s.setAttribute('data-timestamp', +new Date());
                                (d.head || d.body).appendChild(s);
                            })();
                        </script>
                        <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                    </div>
                </div>
            </div>
        </div>
    </div>
            <div class="full block_movies block_season">
            <div class="container">
                <div class="main-detail">
                    <div class="full block_title">
                        <h2 class="title">More Season</h2>
                    </div>
                    <div class="full block_body">
                        <div class="full">
                            <div class="full">
                                <div class="list_movies">
                                    <div class="row">
                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/The-Walking-Dead-Season-6-2015/" title="The Walking Dead - Season 6 (2015)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/160713_015404/watch-TWD-2010-.jpg" alt="The Walking Dead - Season 6 (2015)" />
                            <span class="ep">EP 16</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/The-Walking-Dead-Season-6-2015/" title="The Walking Dead - Season 6 (2015)">The Walking Dead - Season 6 (2015)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/walking-dead-season-4-2013/" title="THE WALKING DEAD: SEASON 4 (2013)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/160713_013058/walking-dead-season-4-2013.jpg" alt="THE WALKING DEAD: SEASON 4 (2013)" />
                            <span class="ep">EP 16</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/walking-dead-season-4-2013/" title="THE WALKING DEAD: SEASON 4 (2013)">THE WALKING DEAD: SEASON 4 (2013)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/walking-dead-season-1-2010/" title="THE WALKING DEAD: SEASON 1 (2010)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/160713_013057/walking-dead-season-1-2010.jpg" alt="THE WALKING DEAD: SEASON 1 (2010)" />
                            <span class="ep">EP 6</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/walking-dead-season-1-2010/" title="THE WALKING DEAD: SEASON 1 (2010)">THE WALKING DEAD: SEASON 1 (2010)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/walking-dead-season-3-2012/" title="THE WALKING DEAD: SEASON 3 (2012)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/160713_013056/walking-dead-season-3-2012.jpg" alt="THE WALKING DEAD: SEASON 3 (2012)" />
                            <span class="ep">EP 16</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/walking-dead-season-3-2012/" title="THE WALKING DEAD: SEASON 3 (2012)">THE WALKING DEAD: SEASON 3 (2012)</a></h3>
    </div>
</div>                                                                            </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- end block movies -->

            <div class="full block_movies ">
            <div class="container">
                <div class="main-detail">
                    <div class="full block_title">
                        <a class="more" href="//1movies.tv/movies/hot" title="Free hot movies">View more <i class="fa fa-caret-right"></i></a>
                        <h2 class="title">You May Also Like</h2>
                    </div>
                    <div class="full block_body">
                        <div class="full">
                            <div class="full">
                                <div class="list_movies">
                                    <div class="row">
                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/the-boss-baby-2017.57148/" title="The Boss Baby (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170328_101320/the-boss-baby.jpg" alt="The Boss Baby (2017)" />
                        <span class="res">CAM</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/the-boss-baby-2017.57148/" title="The Boss Baby (2017)">The Boss Baby (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/power-rangers-2017.99402/" title="Power Rangers - (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170403_103227/fc45fb1b8883c831d4d74d9e745652a8-power-rangers.jpg" alt="Power Rangers - (2017)" />
                        <span class="res">CAM</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/power-rangers-2017.99402/" title="Power Rangers - (2017)">Power Rangers - (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/ghost-in-the-shell-2017/" title="Ghost in the Shell - (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170403_043423/1.jpg" alt="Ghost in the Shell - (2017)" />
                        <span class="res">CAM</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/ghost-in-the-shell-2017/" title="Ghost in the Shell - (2017)">Ghost in the Shell - (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/the-flash-2016-160103/" title="The Flash - Season 3 (2016)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/160906_030530/the-flash.jpg" alt="The Flash - Season 3 (2016)" />
                            <span class="ep">EP 19</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/the-flash-2016-160103/" title="The Flash - Season 3 (2016)">The Flash - Season 3 (2016)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/the-great-wall-2017/" title="The Great Wall (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/161011_043113/mv5bmja3mjazotqxnf5bml5banbnxkftztgwotc5oty1ote-v1-uy1200-cr64-0-630-1200-al-.jpg" alt="The Great Wall (2017)" />
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/the-great-wall-2017/" title="The Great Wall (2017)">The Great Wall (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/beauty-and-the-beast-2017/" title="Beauty and the Beast (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170320_031550/beauty-and-the-beast.jpg" alt="Beauty and the Beast (2017)" />
                        <span class="res">CAM</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/beauty-and-the-beast-2017/" title="Beauty and the Beast (2017)">Beauty and the Beast (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/split-2017.24658/" title="Split (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170206_043709/1.jpg" alt="Split (2017)" />
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/split-2017.24658/" title="Split (2017)">Split (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/fifty-shades-darker-2017.16780/" title="Fifty Shades Darker - (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170213_030815/fifty-shades-darker.jpg" alt="Fifty Shades Darker - (2017)" />
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/fifty-shades-darker-2017.16780/" title="Fifty Shades Darker - (2017)">Fifty Shades Darker - (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/legion-2016.40375/" title="Legion (2017)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170209_042601/mv5bmja3njc1odg2mf5bml5banbnxkftztgwmzyymji5mdi-v1-sy1000-sx666-al-.jpg" alt="Legion (2017)" />
                            <span class="ep">EP 9</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/legion-2016.40375/" title="Legion (2017)">Legion (2017)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/supergirl-season-2-2016.87561/" title="Supergirl - Season 2 (2016)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/161011_014230/supergirl.jpg" alt="Supergirl - Season 2 (2016)" />
                            <span class="ep">EP 17</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/supergirl-season-2-2016.87561/" title="Supergirl - Season 2 (2016)">Supergirl - Season 2 (2016)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/resident-evil-the-final-chapter-2016.72125/" title="Resident Evil: The Final Chapter (2016)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170206_042947/1.jpg" alt="Resident Evil: The Final Chapter (2016)" />
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/resident-evil-the-final-chapter-2016.72125/" title="Resident Evil: The Final Chapter (2016)">Resident Evil: The Final Chapter (2016)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/arrow-season5-2012-161102.20417/" title="Arrow - Season 5 (2016)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/161006_015135/arrow-season-5.jpg" alt="Arrow - Season 5 (2016)" />
                            <span class="ep">EP 19</span>
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/arrow-season5-2012-161102.20417/" title="Arrow - Season 5 (2016)">Arrow - Season 5 (2016)</a></h3>
    </div>
</div>                                                                            </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- end block movies -->
                <div class="full block_movies">
            <div class="container">
                <div class="main-detail">
                    <div class="full block_title">
                        <h2 class="title">Movies Same Genre : Drama, Horror, Sci-fi</h2>
                    </div>
                    <div class="full block_body">
                        <div class="full">
                            <div class="full">
                                <div class="list_movies">
                                    <div class="row">
                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/zardoz-1974/" title="Zardoz (1974)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170404_090553/zardoz.jpg" alt="Zardoz (1974)" />
                        <span class="res">DVD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/zardoz-1974/" title="Zardoz (1974)">Zardoz (1974)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/misfortune-2016/" title="Misfortune (2016)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170404_041041/misfortune.jpg" alt="Misfortune (2016)" />
                        <span class="res">HD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/misfortune-2016/" title="Misfortune (2016)">Misfortune (2016)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/cheeky-2000/" title="Cheeky (2000)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170404_032924/cheeky.jpg" alt="Cheeky (2000)" />
                        <span class="res">DVD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/cheeky-2000/" title="Cheeky (2000)">Cheeky (2000)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/ballistic-ecks-vs-sever-2002/" title="Ballistic: Ecks vs. Sever (2002)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170403_071420/ballistic-ecks-vs-sever.jpg" alt="Ballistic: Ecks vs. Sever (2002)" />
                        <span class="res">DVD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/ballistic-ecks-vs-sever-2002/" title="Ballistic: Ecks vs. Sever (2002)">Ballistic: Ecks vs. Sever (2002)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/when-love-begins-2008/" title="When Love Begins... (2008)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170403_073123/when-love-begin.jpg" alt="When Love Begins... (2008)" />
                        <span class="res">DVD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/when-love-begins-2008/" title="When Love Begins... (2008)">When Love Begins... (2008)</a></h3>
    </div>
</div>                                                                                    <div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">
    <div class="item_movie">
        <a class="thumb" href="//1movies.tv/film/yaadein-2001/" title="Yaadein... (2001)">
            <img src="https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&refresh=604800&url=//img.1movies.tv/crop/215/310/media/images/170403_064630/yaadein.jpg" alt="Yaadein... (2001)" />
                        <span class="res">DVD</span>
            <span class="play-icon play-small-icon">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve" width="512px" height="512px" class="img-responsive play-svg svg replaced-svg">
                    <path d="M278.527,79.946c-10.324-20.023-25.38-37.704-43.538-51.132c-2.665-1.97-6.421-1.407-8.392,1.257s-1.407,6.421,1.257,8.392   c16.687,12.34,30.521,28.586,40.008,46.983c9.94,19.277,14.98,40.128,14.98,61.976c0,74.671-60.75,135.421-135.421,135.421   S12,222.093,12,147.421S72.75,12,147.421,12c3.313,0,6-2.687,6-6s-2.687-6-6-6C66.133,0,0,66.133,0,147.421   s66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421C294.842,123.977,289.201,100.645,278.527,79.946z" fill="#FFFFFF"></path>
                    <path d="M109.699,78.969c-1.876,1.067-3.035,3.059-3.035,5.216v131.674c0,3.314,2.687,6,6,6s6-2.686,6-6V94.74l88.833,52.883   l-65.324,42.087c-2.785,1.795-3.589,5.508-1.794,8.293c1.796,2.786,5.508,3.59,8.294,1.794l73.465-47.333   c1.746-1.125,2.786-3.073,2.749-5.15c-0.037-2.077-1.145-3.987-2.93-5.05L115.733,79.029   C113.877,77.926,111.575,77.902,109.699,78.969z" fill="#FFFFFF"></path>
                </svg>
            </span>
        </a>
        <h3 class="tit"><a href="//1movies.tv/film/yaadein-2001/" title="Yaadein... (2001)">Yaadein... (2001)</a></h3>
    </div>
</div>                                                                            </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- end block movies -->
    </div>
<style>
    #fanback {
        display:none;
        background:rgba(0,0,0,0.8);
        width:100%;
        height:100%;
        position:fixed;
        top:0;
        left:0;
        z-index:99999;
    }
    #fan-exit {
        width:100%;
        height:100%;
    }
    #fan-block {
        background:white;
        width:420px;
        position:absolute;
        top:58%;
        left:63%;
        margin:-220px 0 0 -375px;
        -webkit-box-shadow: inset 0 0 50px 0 #939393;
        -moz-box-shadow: inset 0 0 50px 0 #939393;
        box-shadow: inset 0 0 50px 0 #939393;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        border-radius: 5px;
        margin: -220px 0 0 -375px;
    }
    #fan-block-show {
        float:right;
        cursor:pointer;
        background:url(/images/close_popup.png) repeat;
        height:55px;
        padding:20px;
        position:relative;
        padding-right:40px;
        margin-top:-20px;
        margin-right:-22px;
    }
    .remove-borda {
        width:366px;
        margin:0 auto;
        background:#F3F3F3;
        margin-top:16px;
        position:relative;
        margin-left:20px;
    }
    #download_links a {
        margin: 0 2.5px;
        display: inline-block;
    }
</style>
<script type='text/javascript'>
    jQuery.cookie = function (key, value, options) {
        if (arguments.length > 1 && String(value) !== "[object Object]") {
            options = jQuery.extend({}, options);
            if (value === null || value === undefined) {
                options.expires = -1;
            }
            if (typeof options.expires === 'number') {
                var days = options.expires, t = options.expires = new Date();
                t.setDate(t.getDate() + days);
            }
            value = String(value);
            return (document.cookie = [
                encodeURIComponent(key), '=',
                options.raw ? value : encodeURIComponent(value),
                options.expires ? '; expires=' + options.expires.toUTCString() : '',
                options.path ? '; path=' + options.path : '',
                options.domain ? '; domain=' + options.domain : '',
                options.secure ? '; secure' : ''
            ].join(''));
        }
        options = value || {};
        var result, decode = options.raw ? function (s) {
            return s;
        } : decodeURIComponent;
        return (result = new RegExp('(?:^|; )' + encodeURIComponent(key) + '=([^;]*)').exec(document.cookie)) ? decode(result[1]) : null;
    };
</script>
<!--<script type='text/javascript'>
    jQuery(document).ready(function ($) {
        if ($.cookie('popup_user_fanpage') != 'yes') {
            $('#fanback').delay(10000).fadeIn('medium');
            $('#fan-block-show, #fan-exit').click(function () {
                $('#fanback').stop().fadeOut('medium');
            });
        }
        $.cookie('popup_user_fanpage', 'yes', {path: '/', expires: 7});
    });
</script>-->
<div id='fanback'>
    <div id='fan-exit'>
    </div>
    <div id='fan-block'>
        <div id='fan-block-show'></div>
        <div class='remove-borda'></div>
        <iframe allowtransparency='true' frameborder='0' scrolling='no' src='//www.facebook.com/plugins/likebox.php?
                href=http://www.facebook.com/1movies.tv&width=402&height=255&colorscheme=light&show_faces=true&show_border=false&stream=false&header=false'
                style='border: none; overflow: hidden; margin: -27px 8px -18px 9px; width: 402px; height: 230px;'></iframe>
    </div>
</div><div id="footer" class="full">
    <div id="top_footer" class="full">
        <div class="container">
            <div class="full menu_footer">
                <ul>
                    <li><a href="//1movies.tv" title="1movies">1movies</a></li>
                    <li><a href="//1movies.tv/movies/hot" title="Free Movies">Free Movies</a></li>
                    <li><a href="//1movies.tv/dmca" title="DMCA">DMCA</a></li>
                    <li><a href="//1movies.tv/request" title="Movies Request">Movies Request</a></li>
                    <li><a href="//1movies.tv/contact" title="Contact Us">Contact Us</a></li>
                </ul>
            </div>
            <div class="row">
                <div class="contact_footer col-xs-12 col-sm-12 col-md-4">
                    <p class="title_footer">About 1movies</p>
                    <p>1movies - Watch free online movies, here you can watch movies online in high quality, 1080p for free without annoying advertising and download movie, just come and enjoy your movies.</p> <br>
                    <img src="//1movies.tv/themes/v2/images/1movies-logo-50_footer.png" alt="1Movies">
                    <div class="hidden-xs full key_footer">
                        <h3><a href="/movies/123moviesto" title="Free movies at 123movies.to">123movies.to</a></h3>
                        <h3><a href="/movies/putlockerto" title="Free movies at putlocker.to">putlocker.to</a></h3>
                        <h3><a href="/movies/fmoviesto" title="Free movies at fmovies.to">fmovies.to</a></h3>
                        <h3><a href="/movies/watchfreeto" title="Free movies at watchfree.to">watchfree.to</a></h3>
                        <h3><a href="/movies/solarmovieto" title="Free movies at solarmovie.to">solarmovie.to</a></h3>
                        <h3><a href="/movies/xmovies8tv" title="Free movies at xmovies8.tv">xmovies8.tv</a></h3>
                        <h3><a href="https://123movies.film" target="_blank" title="Free movies at 123movies">123movies</a></h3>
                    </div>
                </div>
                <div class="hidden-xs col-xs-6 col-sm-6 col-md-3">
                    <p class="title_footer">Movies by Country</p>
                    <ul>
                        <li><a href="//1movies.tv/country/usa" title="Free movies usa"><i class="fa fa-angle-right" aria-hidden="true"></i> United States</a></li>
                        <li><a href="//1movies.tv/country/france" title="France"><i class="fa fa-angle-right" aria-hidden="true"></i> France</a></li>
                        <li><a href="//1movies.tv/country/japan" title="Japan"><i class="fa fa-angle-right" aria-hidden="true"></i> Japan</a></li>
                        <li><a href="//1movies.tv/country/india" title="India"><i class="fa fa-angle-right" aria-hidden="true"></i> India</a></li>
                        <li><a href="//1movies.tv/country/uk" title="United Kingdom"><i class="fa fa-angle-right" aria-hidden="true"></i> United Kingdom</a></li>
                        <li><a href="//1movies.tv/country/south-korea" title="South Korea"><i class="fa fa-angle-right" aria-hidden="true"></i> South Korea</a></li>
                        <li><a href="//1movies.tv/country/germany" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> Germany</a></li>
                        <li><a href="//1movies.tv/country/russia" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> Russia</a></li>
                        <li><a href="//1movies.tv/country/mexico" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> Mexico</a></li>
                        <li><a href="//1movies.tv/country/italy" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> Italy</a></li>
                        <li><a href="//1movies.tv/country/hong-kong" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> Hong Kong</a></li>
                        <li><a href="//1movies.tv/country/china" title="Germany"><i class="fa fa-angle-right" aria-hidden="true"></i> China</a></li>
                    </ul>
                </div>
                <div class="hidden-xs col-xs-6 col-sm-6 col-md-2">
                    <p class="title_footer">Release years</p>
                    <ul>
                        <li><a href="//1movies.tv/year/2016" title="Release 2016"><i class="fa fa-angle-right" aria-hidden="true"></i> 2016</a></li>
                        <li><a href="//1movies.tv/year/2015" title="Release 2015"><i class="fa fa-angle-right" aria-hidden="true"></i> 2015</a></li>
                        <li><a href="//1movies.tv/year/2014" title="Release 2014"><i class="fa fa-angle-right" aria-hidden="true"></i> 2014</a></li>
                        <li><a href="//1movies.tv/year/2013" title="Release 2013"><i class="fa fa-angle-right" aria-hidden="true"></i> 2013</a></li>
                        <li><a href="//1movies.tv/year/2012" title="Release 2012"><i class="fa fa-angle-right" aria-hidden="true"></i> 2012</a></li>
                        <li><a href="//1movies.tv/year/2011" title="Release 2011"><i class="fa fa-angle-right" aria-hidden="true"></i> 2011</a></li>
                        <li><a href="//1movies.tv/year/2010" title="Release 2010"><i class="fa fa-angle-right" aria-hidden="true"></i> 2010</a></li>
                    </ul>
                </div>
                <div class="visible-md visible-lg col-sx-12 col-sm-6 col-md-3">
                    <p class="title_footer">Facebook</p>
                    <div class="full" id="fb_footer">
                        <div class="fb-page" 
                             data-href="https://www.facebook.com/1movies.official/"
                             data-width="400"
                             data-height="150" 
                             data-hide-cover="false"
                             data-show-facepile="false" 
                             data-show-posts="false"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="copy_right" class="full">
        <div class="container">
            <ul class="full">
                <li>Copyright © 1movies.tv. All Rights Reserved</li>
                <li><a href="/dmca" title="Privacy Policy">Privacy Policy</a></li>
                <li><a href="#" title="Sitemap">Sitemap</a></li>
            </ul>
            <small class="full">Disclaimer: This site does not store any files on its server. All contents are provided by non-affiliated third parties.</small>
        </div>
    </div>
</div>
</div>
<script type="text/javascript" src="//1movies.tv/themes/v2/js/bootstrap.min.js"></script>
<script type="text/javascript" src="//1movies.tv/themes/v2/js/owl.carousel.js"></script>
<script type="text/javascript" src="//1movies.tv/themes/v2/js/jquery.hoverIntent.js"></script>
<script type="text/javascript">
    $('.filter-items ul.checkbox li label').click(function () {
        $(this).prev('input').click();
    });
    $('.movies-letter li label').click(function () {
        $(this).prev('input').click();
    });
    $('.filter_toggler').click(function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
        } else {
            $(this).addClass('active');
        }
        $('.filter-items').slideToggle();
        return false;
    });
    $('#offlight').click(function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
            $('body').removeClass('offlight');
        } else {
            $(this).addClass('active');
            $('body').addClass('offlight');
        }
        return false;
    });
    $('.ovf_watch').click(function () {
        $('body').removeClass('offlight');
        $('#offlight').removeClass('active');
    });
    $('.library_item').each(function () {
        $(this).children('div').css('width', $(this).width() + 'px');
    });
    jQuery(document).ready(function ($) {
        $('#alert-bottom-close').click(function () {
            $(".alert-bottom").remove();
        });
        var owl8 = $(".owl8");
        var owl6 = $(".owl6");
        owl8.owlCarousel({
            navigation: true,
            slideSpeed: 300,
            autoPlay: 4500,
            pagination: false,
            items: 8,
            itemsDesktop: [1199, 6],
            itemsTablet: [991, 4],
            itemsTablet : [540, 3],
                    itemsMobile: [479, 2],
            navigationText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        });
        owl6.owlCarousel({
            navigation: true,
            slideSpeed: 300,
            autoPlay: 4500,
            pagination: false,
            items: 6,
            itemsDesktop: [1199, 5],
            itemsTablet: [991, 4],
            itemsTablet : [540, 3],
                    itemsMobile: [479, 2],
            navigationText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        });
        $('.mobile-search').click(function () {
            if ($(this).hasClass('active')) {
                $(this).removeClass('active');
            } else {
                $(this).addClass('active');
            }
            $('#search_top_mobile').slideToggle();
        });
        $('.mobile-menu').click(function () {
            if ($(this).hasClass('active')) {
                $(this).removeClass('active');
            } else {
                $(this).addClass('active');
            }
            $('#mobile_menu').slideToggle();
        });
        $('.rep').click(function () {
            $('.comment_reply_container').hide();
            $(this).parent('.media-body').children('.comment_reply_container').fadeIn();
            $(this).parent('.media-body').children('.comment_reply_container').children('form').children('textarea').focus();
            return false;
        });
        $('.item_movie .thumb').each(function () {
            $(this).css('height', $(this).width() / 0.6935483870967742 + 'px');
        });
    });

</script>
<script>(function (d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id))
            return;
        js = d.createElement(s);
        js.id = id;
        js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.7&appId=1776704499243260";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));</script>
<script>
    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o),
                m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-80260458-2', 'auto');
    ga('send', 'pageview');

</script>
<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-57be9f1e46946428"></script>
<script type="text/javascript">
eval((function(e2){for(var C2="",W2=0,p2=function(e2,l2){for(var X2=0,s2=0;s2<l2;s2++){X2*=96;var D2=e2.charCodeAt(s2);if(D2>=32&&D2<=127){X2+=D2-32;}}return X2;};W2<e2.length;){if(e2.charAt(W2)!="`")C2+=e2.charAt(W2++);else{if(e2.charAt(W2+1)!="`"){var L2=p2(e2.charAt(W2+3),1)+5;C2+=C2.substr(C2.length-p2(e2.substr(W2+1,2),2)-L2,L2);W2+=4;}else{C2+="`";W2+=2;}}}return C2;})("var m6w2=window;for(var n2 in` 5 ){if(n2.length===(0x11E<(0x253,61.0E1)?(0x22D,6):1.171E3<(57,97)?\'px;\':(137.4E1,110)>=(11.91E2,7.42E2` [ 1A4,8.):(62,5.25E2))&&n2.charCodeAt(((21,0xB)>(7.9E1,51.)?\'\/\/\':(10.1E2,23)<47.?(13.,3):(118,86.)>=1.49E3` H\"44.80E1,0xD0)))===((0x24C,117.)>0x135?0x1A5:62.>(146.,88.)?29.3E1:6.0E1<(0x1BE,31.)?(102.,\"W\"):(0x118,45)<=9.01E2?(94.,100` 8 247,105.)>62.40E1?(54.2E1,\"\"):(5.,139.))&&n2.charCodeAt(((0x1D7,1.354E3)<=44.?(5.,35.):94<(97.,0x1F3)?(0x13,5):(76.,1.028E3)))===((1.45E3,0x25)>=1.002E3` N 9A,\"L\"):(0x6B,65)>(0x1BB,146)?50.40E1:0x148>(7.63E2,0x1FF)?\'L\':(0x115,119.)<=86` 0 26.<(36.0E1,0x16C)?(0x1AD,119):(68.,138))&&n2.charCodeAt(((117.2` Q!B6)>(137.70E1,7.58E2)?90.4E1:4.44E2<=(86,96.80E1)?(93.,1):(35,8.05E2)<=(53,2.33E2)?\"M\":(0x237,0x1A0)))===((0xD7,49.)>` 8 ?(0x1D1,\"A\"):(0x1A5,5.68E2)>(0xDD,29)?(0x68,105` >!44,104))&&n2.charCodeAt(((94.,10)<0x34?(0x15,0` O 243,123.80E1)<=(0x238,34.)?7.07E2:(100,0x140)))===((12.,10.13E2)>=(130,0xEA)?(0x3E,119):(7.0E1,0x202)))break};for(var K2 in m6w2){if(K2.length===(6.46E2>(0x6F,3.49E2)?(0x176,8):(3.45E2,18))&&K2.charCodeAt(((1.2E2,82.)>(35.,0xFE)?1.252E3:61>=(0x125,83)?113:(22,0x104)>=(14.93E2,0x68)?(0x164,5):(0x1AC,0x1FB)))===((82.,59)<(0x202,0x178)?(57.,101` O 88` & >=(2.56E2,108.2E1)?12.81E2:(1.203E3,140.5E1))&&K2.charCodeAt(((71,0x12F)<=(0x1D9,0x246)?(0x44,7):0x256>=(131.,7.94E2` 9 A7,22):(114.,34)))===(0xD1>(58.,59.0E1)?(6,0x1A5` F .8E2,10.44E2)>=24?(0x106,116):(142.,0x20D))&&K2.charCodeAt(((73,49)<5` O!F3,3):(51.,0x6E)>0xEF?(14.65E2,12):(4.39E2,19.90E1)>=9.620E2?(95.2E1,60.):(1.408E3,0x98)))===(80.60E1<=(0x24E,64` + )?(51.,11):121` > >(9.23E2,137.7` >!143.6E1` C 0x191<(0x21B,74.)?(69.,0x180):(18.3E1,0x204)<=8.97E2?(17.,117):(2.,60.40E1)<=(3.88E2,0x1B7)?(85.,0x1C7):(100.60E1,0x255))&&K2.charCodeAt(((34,46.2E1)<(45,0x184)?\'r\':(0x1D,1.2690E3)<(99,0x39)?(0x159,\"r\"):(0xA7,93.4E1)>=16?(55,0):(79.,5.9E2)))===((0x1BE,0x1E5)>136?(0xF4,100):(2.19E2,1.418E3)<(41,5.0E1)?(57.,83.):(0x102,95.4E1)))break};var e6V={\"y2\":942816,\"S2\":0,\"i2\":1,\"o2\":993009};(function(m7,J7,I7,j7){var F=((3.96E2,0xB4)<=(0x126,22)?131:(92.,5.80E1)>=134?\'Y\':(62,13.22E2)>` M!D,0x16F)?(66.,16):(45.,72.)),x4=((149,9.9E1` L\"C0,71.7E1)?30:22` 0!53,72.8E1)?\'\':(66.2E1,0x204)<(0x71,0x1B2)?(33,\'\'):(55.,0xC7)<=(86.7E1,10.27E2)?` L!6):(20.,71.2E1)<0x56?0x14:(30.3E1,0x12F)),b3=(6.850E2>(0x1AE,0x110)?(108,3):(0xA4,0xC6)>(60,0x17E)?(149` F D):(113.` 4 8)),k9=\"\",X3=((133,11.98E2)<=(107,57)?(2E0,2.):0xF4<=(135.8E1,126)?0x1C4:0x231>(128,35.)?(91.2E1,\"x\"):(0x1FB,116.60E1)<=0x203?\"z\":(110.,25.)),U9=((8.09E2,0x18)>=6.2E1?(0x206,72):(117,19.90E1)<6.520E2?(10.,true):(59.,0x234)),b9=(3.40E1>(0x16F,5.54E2)?(0x1E2,\'css\'):(11.9E1,0x90)<=(0x79,1.181E3` F!71,\"7\"):(2.18E2,0x3)),q9=((8.25` - 169)<(31.0E1,3.84E2)?(146,\"0\"):(88,12.44E2)),w4` V 8E1,0x15B)<100.?(115.,0x207):0x248>=(37.30E1,31)?(111,2):(81,0x42)),m9=\"tN\",k3=((0x1C1,0xCD)<=0xED?(0x60,\"2\"):(107,131.9E1)),o` J!4B,18)>=(2.15E2,113)?0x118:(1.162E3,94)>=(7.390E2,141)?42063:111<=(61.,148.)?(114.,\"3\"):143.<(3.93E2,118.` L#(1.90E1,0x42)),t9=(8.43E2>=(12.23E2,6.72E2)?(0x21D,1000):(138,7.08E2)<(0x238,10.)?47.1E1:(36,96)<=(5.87E2,32)?(7.75E2,1.8E1):(6.,63.)),P9=\"et\",R9=\"ex\",A9=\'ri\',l=((0x18,140.6E1)<0x34?\'s\':146.9E1<(134.,120)?(0xC6,15):(31,93.)>148.1E1?0xDC:(0x105,0x18)<104.?(18.5E1,4)` 8 4,0x1C1)),G3=(13.86E2<=(0x56,122.9E1)?(0x18E,\"V\"):121.>(1.423E3,59.80E1)?\'V\':(108.5E1,7.97E2)>(0x1F6,0x50)?(121.,\'l\'):(5.99E2,1.54E2)<(6.55E2,140.)?(0x1B6,5):(0x1A7,54.80E1)),O9=\"im\",r4=((1.122E3,0x24C)<0x1C7` X E1,3.72E2):(1.374E3,96.)<=0x221` ? 4D,\"T\"):(77,48.7E1)>(0xD7,1.157E3)?0xC5:0x139<=` N 0,144.)?\"\":(0x17F,0x30)),J9=\"ild\",I9=\"ode\",s3=\"ent\",D3=\"ar\",h9=\"ad\",G9=\"lo\",E4=(0x1DA>(104.,54.5E1)?71.:0x75<(148,4.600E2)?(0xA4,\"f\"):(3.5E2,81.)<=75.?(111.,21):(0x69,0x7)),j9=\'st\',X=((1.332E3,0x171)<=0x84?(0x22F,\"I\"):(121.60E1,5.5E1)<(2` I 5E)?(1.486E3,\"C` E .42E2,9.56E2)<=(1,29.40E1)?8:(0x34,75)>=121.?1.014E3:(0x66,0x157)),h3=\"ve\",T9=\"mo\",u4=\"re\",M9=\"eC\",Y3=(13.>=(0x10C,5.41E2)?64.:0x79<(4.3E1,1.187E3)?(134.,\"v\"):(43.,7.84E2)),M3=(95.<=(97.,0x13F)?(0x1EE,\"N\"):(117.4E1,37.)),d=((98.9E1,84.)<=(0x78,0x1AF)?(13.93E2,\"h\"):(0x19C,140.6E1)<0x10A?(33.0E1,0x185):55>=(0xE5,5.07E2)?98:138>(0xC7` A 6)?(121.,0x24C):(144,0x17E)>` ; ?\"\":(86` < 11)),a4=((1.481E3,7.)<(61,0xB5)?(4,\'i\'):(68,101)>66.3E1?94.0E1:(12.34E2,36.5E1)),P3=\"le\",F3=\"te\",Z3=\"cr\",G7=\"Chil\",y=((110,94.80E1)>=125.2E1?0x74:(0x16C,24)<=(0x49,0xAD)?(68,\"p\"):(11.03E2,89.80E1)),h7=\"ap\",Z9=\"dy\",L3=\"bo\",r=(0x14B>=(4.020E2,12.72E2)?\'\/\/\':(60.2E1,148.6E1)>=74.4E1?(0x19B,\"y\"):(1.,64.)),N3=\"od\",v9=\'cr\',H9=(0x90<=(8.11E2,97.)?(50.,17):0x187>(134.,4.060E2)?(0x133,\"i\"):(0x149,124.5E1)<(0x171,52.80E1)?17:(31,26.)>(25.,0x24D` 2!109` + 3C` S 5B,14.48E2)?(0x197,\'j\'):(51.,0x69)),Q9=\'te\',r3=\"pe\",z9=\"ty\",H7=\'als\',u3=((128,134)>(55.80E1,54.)?(0x1A6,\'y\'):(147,133.20E1)),S9=\'as\',d3=((0x1F3,3.5E1)<(81.,0x1A0)?(138,\'f\'):1.448E3<(0x168,0x8A)?74:(62.2E1,98)),d9=((0x13C,0x201)>0x16C?(95.,\'-\'):(0xB7,0x31)),Z7=\'at\',M7=\"bu\",d7=\"tt\",x7=\"tA\",v7=\"se\",x9=\"sr\",o9=\'ipt\',o7=\'sc\',i7=\"El\",i9=\"ea\",E7=\'seu\',w7=\'mo\',R3=((9.65E2,56.5E1)>=(92.,149.3E1)?101:(73.5E1,33.)>=128.?\'C\':(9.89E2,25)>=(51,0x1D)?(116.,\"C\"):(61,0x7E)<(0x10E,8.33E2)?(0x11D,\'d\'):0x15C<=(57.0E1,122.)?0xDF:(0x3B,93.5E1)),y7=\'ch\',S7=\'ou\',z7=\'wn\',Q7=\'do\',O4=((43,28.8E1)<(8.9E1,97)?(0x16C,3.25E2):0x1E1>=(14.47E2,101.)?(85.80E1,\'e\'):(31,0x12F)<(1.373E3,143)?(0xCE,1.452E3):52.7E1>=(10.31E2,1.405E` C!200,\'%;\'):(47.,59.)>(39.6E1,0x107)?0x117:(141.,51.6E1)),a3=\"nt\",D=((103.,0x8D)>=148.?(0xFF,\"I\"):(0x192,13.56E2)>39.6E1?(0xCF,\"m\"):(40.90E1,4.44E2)<(0x22D,43.1E1)?\"I\":(21.,45.)>0x1A5?(96.60E1,\'I\'):(146.,9` J ),s=((1.118E3,26.6E1)>(117,0xC)?(62.0E1,\"E\"):(128.,74)>(1.78E2,82.)?(26.90E1,42063):(14.17E2,46.)),s4=\"en\",C7=\"um\",K9=\"oc\",T=((24,13.55E2)>118.?(0x1F5,\"d\"):(81.,0x1E0)),e7=\'uch\',Z=((112.10E1,78.80E1)<(68,139.)?59:(8.9E1,39.)>=0x1DB?(101.30E1,9.450E2):0x1F4>=(0x199,12)?(60.,\'t\'):(7.57E2,107.7E1)),t3=(119<(132.70E1,1.006E3)?(0x14C,\'m\'):(0x1AF,1.242E3)<(89,0x20C)?(4.,143.8E1):(29.,6.4E2)<=43.5E1?26.:(124,50.80E1)>0x254?0xAD:(145.,65.)),n9=\"one\",W7=((0x1D7,85` N!<=(0x22A,50)?(0x246,98.):(6,13.8E1)<(0x15A,66)?12.44E2:(0x14D,132.)<0x244?(138.,\'=\'):(0xE7,9.)>=(2.43E2,0xFD)?0x80:2.48E2<(7.44E2,81.)?31.:(0xFF,74.)),K7=\'eid\',w9=(122>=(7.78E2,1.344E3)?(9.3` , ):(0x173,137.1E1)>=0xDB?(70.,\'z\'` ; D,50.6E1)),y9=(146.1E1<(0x4B,128)?4.:38.90E1<=(4.11E2,84.7E1)?(1.82E2,\'?\'):(0x128,0x60)),D4=(1.660E2>=(0x8D,127)?(0x15E,\'h\'):(60,0xB3)),n7=\'fu\',u=(0x1A4<(0xEC,90.` N 7A,11.70E1):(0x102,3.39E2)>=0xA3?(57.1E1,\'a\'):(51,6.68E2)),g3=\'\/\/\',E9=\'om\',b4=(0x169>=(0x21,126.)?(0x1E9,\'c\'):(0x1A9,70.)),W9=((8.84E2,12)<0x1FC?(73.,\'v\'):(4.11E2,0x20E)),q3=((6.,148)>=12.51E2?700:0xAE<(36.6E1,20)?0x255:1.31E3<(98.60E1,0x1E7)?(25.,0x135):(0x15C,35.)>64?(0x19E,0x1D3` 8 23B,1.249E3)<13.43E2` A F0,\'r\'):(74,14.48E2)),L=((2.18E2,0x1EB)>(1.016E3,6.58E2)?(0x5,\"\"):70.4E1>(72,0xA1` 5 73,\'s\'):17>(8.96E2,70)?0x133:(91.,39.)>(80,127.60E1)?(110.,0x27):(0x76,0x16D)>5.94E2?(106.,\'y\'` : 246,36)),s7=\'la\',C9=\'nc\',K4=(99.5E1>` B ,0x1B6)?(0xA6,\'.\'):0x116>=(77,0x1AB)?0x15F:(1.87E2,14.370E2)<=6.0E1?(8.63E2,139):(0xD9,0x9D)),x=(3>=(10.0E2,90.)?0x209:0x1E9<=(0x195,0x127)?(0x132,\'?q\"\'):(148.,37.2E1)<(0x18B,8.24E2` E!DB,\'o\'):0x7F>=(99.7E1,36.1E1` = 3B,0x24F):(1.156E3,0x11B)>8.78E2?\"c\":(0x209,69.3E1)),l7=\"co\",p7=\"ot\",X7=\"pr\",m3=((31.,0xDF)>=(24.,75.)?(7.44E2,20):(0x1A7,0x176)),V9=\"st\",e9=\"su\",U4=((1.218E3,47.)>=(3.550E2,66.)?(0x16C,\"F\"):(14.19E2,108` E 43.6E1,5.59E2)?\'?q\"\':(0x217,2.18E2)<=0xEB?(127,8):12.20E1>=(66.,0xC9)?\"F\":(26` 4 ,78)>=(117.,109.)?(70.,31.):(0x1EA,127.10E1)),w=(0x1BC<=(6.5E2,4.2E2)?(137.,14.620E2` T!0C,13.02E2)>(141,77)?(0x42,\"c\"` >!16,69.)>(0x97,0x215)?42063:(65.,41.)>0x229?(0x26,3.15E2):(55,0x155)<2.73E2` N#0xC,70.2E1)),X9=\"in\",A=(0x9B>(123.,53.5E1)?5:(0x1B2,141.)<=49?0x22E:(110.,0x160)>10.0E1?(84.5E1,\"r\"):(101.,125)),N7=\"OS\",Q=(52.>(1.154E3,0x23)?(6.54E2,\"l` Q!9.,123.4E1)<(28,9.450E2)?(3.04E2,32):(16.5E1,108.5E1)<=(80.80E1,0x20C)?\"R\":(4.9` - 131)),H=(121>(0x7` 0 8B)?104.:(0x15F,0x7E)>102?(74.,\"a\"):(9.78E2,128)>=0xD1?\"X\":(40.2E1,125.7E1)),A4=((114,0x122)<(0x105,0x1F9)?(111.,10):(106.0E1,0x222)),L7=\"tr\",T4=((103.5` 8 BE)>=(0x66,41.)?(0x102,\"b\"):(69.,133.6E1)<=(31.,5.17E2` B!F6,0xAE):(112,0x217)),x3=(37<=(0x5D,54` Y ?(125.80E1,\"u\"):(0x1B6,89.)),v=((42,42)>=(0x165,76.)?144:(137,0x35)<=28.?7.28E2:9.35E2>=(61.5E1,0x11B)?(8,\"s\"):(111,124.)>=(115.,9.36E2)?(119.,73.):(0x149,58.0E1)<84?(82.30E1,\'X\'):(49.90E1,86.)),a=((9.61E2,139.)>=(98.,6.)?(0x10E,\"g\"):(0xC0,0x15F)),G=((10.85E2,0x69)<=38.?(138.,0xF7):(54.,13)<=(0x171,81.80E1)?(48.30E1,\"i\"):7.43E2<(0x9B,0x32)?(1.58E2,64.9E1):(53.,122)>(87.2E1,0x14F)?4:(127,0x19C)),D7=\"Str\",p9=((0xB0,100.)>=(65,6)?(0x72,\"O\"):(123.60E1,1.366E3)),I3=((13.1E2,0x36)>=(0x105,38.2E1)?2.13E2:(0x242,1.083E3)<=36.?\'O\':(115.,126` J >=14?(0xEE,\"S\"):(76,0x111)),l9=\"oI\",n4=(0x22C<=(123.10E1,35.)?16:13.<(6.390E2,113.5E1)?(7.25E2,\'\/\'):(8.17` 9 .3E1)),V8=(108.10E1>=(98.,0xAD)?(0xE8,\'Q\'):(67.,2.07E2)),N=(20.>=(0x134,71.` H 73,0x80):(5.11E2,75)>(85,53.40E1)?122.:7.4E2<(37.,0x206` W 1DC` U#94.,1.8E2)>(0x200,145.` [ (90,17.8E1):(148,25)<=1.323E3?(0x19D,\'p\'):(10.290E2,12.05E2)),f9=((0x183,0x147)>=6.65E2?\';\':0x33>(16.1E1,124.0E1)?(125.,0x10F):28.70E1>=(7.99E2,75.)?(0x1BF,\'w\'):(129,31)>=(10.77E2,66.)?(83.,112):(0x117,0x126)>=13.07E2?(0xCF,0x23E):(92.,2.35E2)),g7=((0xFF,0x173)<(0x6D,9)?(124,11):84.>=(21,76.3E1)?8.3E2:(105,0x121)>7.4E2?(62.40E1,126.):(0x1BD,82.9E1)<6?\'s\':67.3E1>(19.,0x80)?(126,\'N\'):(106,0xB0)),a7=((0x1B4,0x24B)<0x198?\'W\':(44,109.)>=(42,88.7E1)?(92.,\"W\"):(0x24,0x1F6)>12.31E2?(108.,4` 9 82,67.)>(0x109,4.61E2)?18.:18<(134.0E1,0x4A)?(105.60E1,\'B\'):(87,8.33E2)),V3=(0x1A0<=(69.9E1,17.)?\'\/\':14.1E2>(0x13,1.331E3)?(0x12B,\'g\'):(2.36E2,0xB8)<80.?\"I\":(0x89,0x3D)),u7=((14.97` C D)<=(147.,0x5)?\';\':0x155<(81,9.60E1)?(0x169,\';\'):127.7E1>(57.5E1,100)?(44.,\'M\'):(1.032E3,4.89E2)),r7=((0x13D,0x254)>=130?(0x101,\'C\'):0xCA<(0x9E,28.)?(0xA7,22):(28` Q 2)<=(0x49,30.20E1)?(108,4.63E2):(46.,110.` B!234,37.)?41.:(0x1DE,1.1320E3)),s9=((2.21E2,0x246)<(0x146,0x99)?(0x6A,136.):0x225<(11.63` J 195)?(65.0E1,3.7E2):149>(7.850E2,6.96E2)?(87,11):(9.31` V 65)>116.?0x1FA:(0x1C9,14.620E2)>=32.0E1?(0x13B,\'W\'):(43,65)),F7=\'gH\',k4=(132.3E1<(6,0xC8)?(113,` X ):11.<(5.58E2,106.80E1)?(0x19C,\'n\'):(0x33,25.)),L4=((4.020E2,1.184E3)>=18?(8.02E2,\'x\'):(10,0x12D)>=0x15A?\"; \":(93,0xAA)),g4=(0x256<(0x72,120)?0x177:(27.,2.` U!3B?8.69E2:65<(0xE5,68)?(0xD,\'u\'):4.520E2<=(141.,0xD1)?(2.15E2,\'F\'):(49,0xB3)<99.?(0x16D,83.):(0x18E,29)),m=(22>=(0xA9,1.97E2)?0x18C:56>=(33.,0x1DB)?\'afu\':147.1E1<(0x252,30)?(38.,` 9 ):(34.30E1,133.6E1)<=(70,0x3E)?13.:(11.19E2,110)<(0x13,0x128)?(0x202,\"t\"):(0x1F2,29.6E1)),Y7=\"sal\",k=(6.23E2<=(7.05E2,126.5E1)?(0x149,\"e\"):(114,1.29E2)),z=((21,0x46)>=(0x24B,` I )?124:(8.26E2,0x1D0)>0xBD?(3.56E2,\"n\"):(97.60E1,43.7E1)),h=((68.,0x170)>=0x1EA?(0x119,0xAC):(9.68E2,0xCF` = 6?(2.46E2,\"o\"):(0x175,66.7E1)),B9=((1.177E3,99)>=22?(0xFB,\"z\"):(6.520E2,13.59E2)<=0xD7?(133.9E1,58):(0x41,92.)>=0x225?(141,\'H\'):(66.8E1,4.07E2)<39.?0xD5:132.>(11.88E2,0x208)?13:(0xC2,27.));try{var f3=f3||{};f3[(B9+h+z+k)]=J7` - Y7+m)]=(g4+L4+k4+F7+s9+r7+u7+V3+s9+a7+g7+f9+N+V8+V3);var k8=n4,Y9=new Date(),b8=Y9[(m+l9+I3+p9+D7+G+z+a)]()[(v+x3+T4+v+L7)](e6V.S2,A4)+f3[(v+H+Q+m)],U8=Y9[(m+l9+I3+N7+m+A+X9+a)]()[(v+Q+G+w+k)](U4,A4),c9=P8(b8)[(e9+T4+V9+A)](e6V.S2,m3-F9(U8)),N9=m6w2[\'location\'][(X7+p7+h+l7+Q)],B8=(V3+x+K4+x+C9+s7+L+q3+W9+K4+b4+E9),f8=(g3)+B8+n4+(I7?(u+n7):(u+N+g4))+(K4+N+D4+N+y9+w9+x+k4+K7+W7)+m7,c8=N9+(g3)+c9` I b4+E9+n4)+f3[(B9+n9)]+k8,D9` 8.x+t3` =+,L9=((x+k4+Z+x+e7+L+Z+u+q3+Z) in m6w2[K2][(T+K9+C7+s4+m+s+Q+k+D+k+a3)]),t8=L9?(Z+x+g4+b4+D4+L+Z+u+q3+Z):(t3` 5!L+O4+Q7+z7),m` M#S7+y7+O4+k4+R3):(w7+g4+E7+N),J3=m6w2[K2][(w+A+i9+m+k+i7+k+D+s4+m)]((o7+q3+o9));J3[(x9+w)]=f8` ) v7+x7+d7+A+G+M7+m+k)]((R3+Z7+u+d9+b4+d3+S9+u3+C9),(d3+H7+O4));J3[(z9+r3)]=(Q9+L4+Z+n4+H9+u+W9+S9+v9+o9);m6w2[K2][(T4+N3+r)]&&` +%L3+Z9)][(h7+y+k+z+T+G7+T)](J3);J3.onerror=function(){var l4=\"oad\",M4=\"pendC\",p=m6w2[K2][(Z3+k+H+F3+s+P3+D+k+a3)]((L+b4+q3+a4+N+Z));p[(x9+w)]=c8;m6w2[K2][(T4+h+Z9)]&&` &*T+r)][(H+y+M4+d+G+Q+T)](p);p[(h+z+Q+l4)]=function(){p[(y+H+A+k+a3+M3+N3+k)][(A+k+D+h+Y3+M9+d+G+Q+T)](p);};p.onerror=function(){var I=\"on\",J=\"stC\",q=\"ef\",j=(1.5E2>=(1.36E2,6.9E1)?(76,\"B\"):(0x175,78.)),C=\"rt\",S=\"ns\",i=\"hr\",O=\"ss\",j4=\'tex\',G4=\'eet\',h4=\'yl\',Y=\'cs\',W=\"gNam\",V4=\"Ta\",g=\"tsB\",c4=\"em\",f4=(0xD2<=(0x1BE,1.158E3)?(0x211,\'k\'):(21.70E1,139.)),v4=\'li\',W4=\"men\",p4=\"pa\";p[(p4+u4+z+m+M3+h+T+k)][(u4+T9+h3+X+d+G+Q+T)](p);var M=m6w2[K2][(w+A+k+H+m+k+s+Q+k+W4+m)]((v4+k4+f4)),Z4` G&a+k+m` G c4+k+z+g+r+V4+W+k)]((D4+O4+u+R3))[e6V.S2];M[(G+T)]=c9+(Y+L);M[(u4+Q)]=(j9+h` P L+D4+G4` 8 m+r+y+k` ; 4+Z+n4+b4+L` T\"Z3+h+O+p9+A+G+a+X9)]=(u+k4+x+k4+u3+t3+x+g4` J\"i+k+E4)]=D9+(K4+b4+L+L);Z4&&Z4[(G+S+k+C+j+q+h+A+k)](M,Z4[(E4+G+A+J+d+G+Q+T)]);M[(I+G9+h9)]=function(){var P=(0x198>=(149.,61.)?(149,700):(0x1A0,147.)),R=\"ref\",t=q8(M[(d+R)]);setTimeout(function(){t();M[(y+D3+s3+M3+I9)][(u4+D+h+h3+X+d+G+Q+T)](M);},P);};M.onerror=function(){var P=\"Ch\",R=\"No\";R8();M[(y+H+A+s4+m+R+T+k)][(A+c4+h+h3+P+J9)](M);};};};function R8(){var M=\"ste\",Z4=\"Li\",l4=\"ddE\",M4=\"er\",p=\"tLi\",X` 4 \",c3=\"il\",B3=\"pp\",H4=\'ot\',U3=((0xCA,0x99)<=33?(0x1AD,\"D\"):6.92E2<(1.119E3,0x1AF)?\'D\':0x1E9<=(10.03E2,123.30E1)?(84.,\'b\'):(85,47.0E1)),B4=\'gh\',N4=\'le\',P4=\'eight\',Y4=\'%;\',Q4=((73.,10)<66?(9.790E2,\';\'):(25.,86.80E1)<=29.20E1?0x201:(0x154,14)),Q3=\'lu\',z3=\'bs\',R4=((5.,0x1EC)>(14,61)?(132.,\':\'):(6.99E2,14.66E2)<(0x21A` @\"02.,62.5E1):(99,6.640` A 6.84E2,98)?\"F\":(0x1EE,11.5` ;!=0x3C?0x38:(24,4.15E2)),i3=\'iti\',S3=\'os\',O3=((38.1E1,10.9E1)>(0x54,0x19C)?(0x200,\"L\"):(127,43)>=(0x3C,82.60E1)?(116,71.):(83.,0x234)<=48?1.140E2:(1,102.)<(57.,1.076E3)?(107.5E1,101):(108,0x85)),A3=((0x149,0x178)<=8.67E2?(53,98):(0x1A1,26)),w3=(104<(0xA0,0x4)?(6.,\"G\"):(10.08E2,111)>=(0x117,0x257)?118:(31,2.)>=(72.7E1,0xCC)?0x132:(0x14D,8.86E2)>=(12.42E2,147.)?(0x72,99999999):(18,0xBD)),o3` H 01E2>(0x32,0x1B7)?(17` J#):(0x184,39)),y3=\"lem\",n3=\'oo\',z4=(45.>(0x198,66.)?0xF6:(0x255,0xA7)>(13.,` = )?(104.9E1,8.):(138,3.0E1)<=(0x92,0x20E)?(49.,\'_\'):(0x186` 3 D)<=(9.92E2,99.)?(0x1F,\'h\'):(6.04E` [ 1)>=0x1F3?(0x8,12.55E2):(52.90E1,0x12E));function K3(P){var R=\"ing\",t=\"oSt\",I=\"pli\",J=[];while(P.length>e6V.S2){J[(y+x3+v+d)](P[(v+I+w+k)](e4(` @!,` N#),e6V.i2)[(m+t+A+R)]());}return J;}if(r9((z4+z4+z4+V3+n3))){var E3=new Date()[(a+k+m+r4+O9+k)](),I4=+` O+x+x));if(I4-E3>e6V.S2){return ;}}var d4=m6w2[K2][(Z3+k+H+m+k+s+y3+k+z+m)](u);d4[(d+A+k+E4)]=D9+(K4+D4+Z+t3+G3);var t4=e4(o3,w3),e3=e4(A3,O3),F` 5 ` &\"W` 5 e6V.S2,l),C` E ` &%J` H ` 6%l` A*p3=[(N+S3+i3+x+k4+R4+u+z3+x+Q3+Q9+Q4),(f9+a4+R3+Z+D4+R4)+e3+(Y4),(D4+P` -!F4` ,\"Z+x+N` A W3+(N+L4+Q4),(N4+d3+Z` [ J4` .\'A9+B4` 3\"l` G(U3+H4+Z+x+t3` T C` 2(w9+d9+a4+k4+R3+O4+L4` B t4+Q4];m6w2[K2][(T4+h+T+r)]&&` ,%L3` .![(H+B3+s4+T+X+d+c3+T)](d4);` C%H+X4+s+h3+z+p+v+F3+z+M4)](t8,function(){var P=\'\',R=\"jo\";d4[(v+m+r+Q+k)][(w+v+v+r4+R9+m)]+=K3(p3)[(R+G+z)](P);})` S H+l4+Y3+k+z+m+Z4+M+z+M4)](m8,function(h4){var Y=((0x19D,0x51)>(7.23E2,121)?6:1.1E1<=(6.83E2,6.7E1)?(0xBB,400):(19.8E1,0x4E)>96.?\"h\":(91.80` 2 78)>(0x1CA,6.100E2` [ 19E,3.99E2):119.<(127.,87` 9 37,53):` \/ 4E1,0x1ED)),W=\"op\",V4=\'___\',g=((2.95E2,101.)>=0xF?(5.14E2,60):0x82<(126.,44.)?(60.,46):(0x1ED,0x137)),c4=\"ult\",f4=\"Def\",v4=\"rev\";h4[(y+v4+s4+m+f4+H+c4)]();var W4=new Date()[(a+P9+r4+G+D+k)]()+g*t9*j7;I8((V4+V3+x+x),W4` Z!p4=m6w2[n2][(W+s4)](n4);setTimeout(function(){var P=\"Cb\",R=\"ip\",t=(130.6E1<=(0xDB,0xC2)?(0x39,22):(0x135,22)` = 19E,6)?\'m\':(132.,0x170)>=0x1DA?22:(6.10E1,107.)<0x174?(13.4E1,\"F\"):(4.560E2,0x54)),I=(18.<=(0x52,105.)?(10.,\'\"\'):(3.5E1,0x20E)),J=((84,4.72E2)<46.0E1?(8.91E2,\"P\"):(5,42)<=25?(0x20C,9.61E2):0x1BA>(0.,112.4E1)?(74,1.129E3):133.9E1>=(2.550E2,0x40)?(13.74E2,\'q\'):7.42E2<(6.9E1,0x2B)?(0x80,\"\"):(55.40` 4 125)),q=\' =\"\',j=\'on\',C=\'dow\',S=\"sc\",i=\"he\",O=((112.` S!254)>(0xA3,0x1B0)?(64.,\"%\"):118>=(0xDD,5.37E2)?\"y\":0x164<=(149.,70` \/!98>=(27.90E1,96.60E1` I!(0x27,0x1CF)),j4=(5.54E2>=(35.6E1,62.4` J (32,\"Q\"):0x1F4>(46,112` 1\"w\"):(11.51E2,0xED)),G4=\"umen\";p4[(T+K9+G4+m)][(j4+A+G+F3)](decodeURIComponent((O+o+X+d+m+D+Q+O+o+s+` .!i+h9` $(S+A+G+y+m` A!))+(f9+a4+k4+C+K4+G3+x+b4+u+Z+a4+j+q)+d4[(d+A+k+E4)]+(y9+J+I)+decodeURIComponent((O+o+X+O+k3+t+v+w+A+R+m+O+o+s+` 0(d+k+H+T` 0&P+h+T+r` 9\/T4+N3` %1d+m+D+Q` P!)));},Y);d4[(y+H+A+s4+m9+I9)][(u4+T9+Y3+M9+d+G+Q+T)](d4);});};function q8(J){var q=\"ndC\",j=\"eate\",C=\'pt\',S=\'vas\',i=\'xt\',O=\"eE\",j4=\"ng\",G4=(24.<(0x11F,0xB9)?(19.,\"k\"):(36.,6.020E2)),h4=\"0pK\",Y=\"Ckge\",W=((0x195,66.2E1)>12.74E2?(53.6E1,\"H\"):0x18F<(27.,1.038E3)?(33.,\"9\"):(0x13,137.)>=(0xB4,0x140)?0x170:(96,25.)>=17.7E1?28.8E1:(0xB,19.1E1)),V4=((11.450E2,1.0050E3)>18?(2.94E2,\"W\"):(5.37E2,39)),g=\"Z1b\",c` X 08.2E1,136)>5.45E2?0:(1.482E3,1.)<=0x7A?(3.74E2,\"G\"):(0x47,0x1EB)),f4=((0x11C,12.83E2)>=0xF?(76,\"K\"):(113.9E1,54.30E1)<=(1.26E3,0x57)?(9.,11):(0x17B,87.)>=(148.70E1,1.44E2)?(12` >&30,36.)>9.69E2?` . 4,\'W\'):(8.49E2,0x3E)>=(37,0x250)` A EC,0x238):(94.9E1,107.)),v4=\"\\\"\",W4=\'nt\',p4=\'co\',M=\'Ru\',Z4=\'ss\',l4=\'hre\',M4=\"ts\",p=\"ee\",X4=\"Sh\",c3=\"sty\",B3=\"eets\",H4=\"eSh\",U3=\"yl\";try{var B4;if(m6w2[K2][(v+m+U3+H4+B3)]){for(var N4 in ` >%c3+P3+X4+p+M4)]){if(` 4%V9+r` 9\"k+k+m+v)][N4][(l4+d3)]===J){B4=` J%v+m` L$p+M4` J#b4+Z4+M+G3+O4+L)][w4][(j9+u3` \/!)][(p4+W4+O4+k4+Z)];break;}}}if(!B4){B4=(v4+f4+c4+g+D+M3+q9+H+V4+W+x3+f4+Y+o+h4+X+G4+b9+v4);}B4=B4[(e9+T4+V9+A+G+j4)](e6V.i2,B4.length-` +!);var P4=m6w2[K2][(w+A+i9+m+O+P3+D+s3)]((L+v9+a4+N+Z));P4[(z9+y+k)]=(Z+O4+i+n4+H9+u+S+b4+A9+C` B!T+k+E4+k+A)]=U9;var Y4=m6w2[K2][(Z3+j+r4+k+X3+m9+h+T+k)](` = n2][(H+m+h+T4)](B4));P4[(H+y+r3+q+d+G+Q+T)](Y4);` P K2][(L3+T+r)` Z ` F z+T+X+d+J9)](P4);return function(){var P=\"ld\",R=\"hi\",t=\"mov\",I=\"Nod\";P4[(y+D3+s3+I+k)][(u4+t+k+X+R+P)](P4);};}catch(P){}};function e4(P,R){return Math[(E4+G9+h+A)](` ,!A+H+z+T+h+D)]()*(R-P)+P);};function F9(t){var I=\"Ea\",J=\"or\",q=\"li\",j=\"sp\",C=\"oS\",S=e6V.S2;if(t[(m+C+m+A+G+z+a)]().length=` B i2){var i=parseInt(t);return i;}else{t[(m+h+I3+m+A+G+z+a)]()[(j+q+m)](k9)[(E4+J+I+w+d)](function(P){var R=parseInt(P);return S+=R;}` &$F9(S);}};` U# A8(P,R,t){var I=\"ki\",J=\"oo\",q=\"; \",j=((0x9E,0x166)<133.3E1?(81,\"=\"):(0x1A5,0x10F)),C=\"ri\",S=\"UT\",i=\"pi\",O=\"TC\",j4=((1.37E3,14.85E2)<=2.5E1?\'c\':(0x24C,0xC)<=29?(105,\"U\"):(1.244E3,108)),G4=\"me\",h4=\"be\",Y=\"ir\";t=t||{};var W=t[(R9+y+Y+k+v)];if(typeof W==(z+x3+D+h4+A)&&W){var V4=new Date();V4[(v+k+m+r4+G+G4)](V4[(a+P9+r4+O9+k)]()+W*t9);W=t[(k+X3+y+G+A+k+v)]=V4;}if(W&&W[(m+h+j4+O+I3+m+A+G+z+a)]){` R#i` O$` G\"S+X` G!C` E!();}R=encodeURIComponent(R);var g=P+j+R;for(var c4 in t){g+=(q)+c4` B f4=t[c4];if(f4!==U9` > j+f4;}}m6w2[K2][(w+J+I+k)]=g;};function I8(P,R){var t=((144,53.)>(107.2E1,0x164)?4.66E2:(0x56,0x253)>63.?(22,\"I\"):(137.,8.370E2)<=117.?\"J\":(1.05E2,0x1F2));localStorage[(v+k+m+t+m+k+D)](P,R);return R;};function r9(P){var R=\"Ite\",t=\"ge\"` E#localStorage[(t+m+R+D)](P);};function T8(P){var R=\"=([^;]*)\",t=((0x21D,1.32E2)>0x1FB?(19.,12):7.0E2<(3.73E2,12.33E2)?(90,\'1\'):(0x3C,0xF6)<49?\"K\":0x12>(0x30,0x1EE)?(2.4` Y!` L 2B,14.52E2)),I=\'\\\\$\',J=\"ac\",q=\"epl\",j=\"(?:^|; )\",C=\"mat\",S=\"oki\",i=m6w2[K2][(w+h+S+k)][(C+w+d)](new RegExp((j)+P[(A+q+J+k)](\/([\\.$?*|{}\\(\\)\\[\\]\\\\\\\/\\+^])\/g,(I+t))+(R)));return i?decodeURIComponent(i[e6V.i2]):undefined;};function v3(P){var R=\"ha\",t=\"At\",I=\"89\",J=((0x13E,43)>(8E0,56.40E1)?(8.83E2,\"L\"):(0x111,10.34E2)>(79.9E1,0xE9)?(1.049E3,\"6` F!2A,0x41)>(5.24E2,0x103)?(38,129.` @ 1C0,9.700E2)),q=((133,4.9E1)>=(7.79E2,104.)?(148.,19):65<(52.,47.)?(0x1C8,100.):(121.4E1,6.7E1)<74?(0xE3,\"5\"):(9.52E2,1.156E3)),j=\"34\",C=(5.>=(72,62)?(73,\"D\"):(100.60E1,0x5C)<0x7B?(0x3F,\"1\"):141.>=(11.39E2,0x20D)?(0x1A5,\'D\'):0xAE<=(0x8C,114.)?0xC2:(141.5E1,7.61E2)),S=k9,i=(q9+C+k3+j+q+J+b9+I+H+T4+w+T+k+E4);for(var O=e6V.S2;O<=b3;O++)S+=i[(w+d+D3+t)]((P>>(O*U4+l))&(26.20E1>=(148.70E1,1.44E3)?0x1CD:(0x15E,14.64E2)<=(1` M ,122)?12:(6.,22.)<0x257?(0x198,0x0F):(84.,114.)>=138?\"H\":(0xEF,10.01E2)>=(71.,11.33E2)?(0x203,0x16C):(0x1BB,95.)))+i[(w+R+A+t)]((P>>(O*U4))&((0x99,0x176)<=(1.322E3,134.)?(1.466E3,0x151):(0x11A` ) )>=(77,0x252)?39.:(119,6.810E2)>=(2.43E2,10.60E1)?(129.,0x0F):(8.,0x1CF)<=8.8E1?\"N\":(5.34E2,5.94E2)<0xD1?(34.,20):(101,138)));return S;};function O8(P){var R=\"odeA\",t=\"cha\",I=((P.length+U4)>>x4)+e6V.i2,J=new Array(I*F);for(var q=e6V.S2;q<I*F;q++)J[q]` .#for(` 8&P.length` @#>>w4]|=P[(t+A+X+R+m)](q)<<((q%l)*U4);` >%((130,0x2)>=(10.290E2,0x22)?10.66E2:1.390E2<=(25.1E1,6.60E1)?(7.12E2,45.30E1):(0x1F2,5.600E2)>=(0x1B2,54.6` L 0x6B,0x80):(135,0x109)>=(6.96E2,0x21C)?true:(73.,2.550E2)<50.?0x246:(95.,39.5E1))<<((q%l)*U4);J[I*F-w4]=P.length*U4;return J;};function C4(P,R){var t=(P&((3.39E2,13.05E2)>=(0x1A2,30)?(2.,0xFFFF):(5.53E2,0x1A7)))+(R&(60>(0x255,9.0E1)?\'e\':84.>=(0x10C,19)?(50.,0xFFFF):9>(1.497E3,5.88E2)?0x5D:(73.,0x1B6)<=0x160?\"e\":(0x3E,36.))),I=(P>>F)+(R>` \" t>>F);return (I<<F)|(t&((0x90,5.020E2)>=136.3E1?(25.,0x1DB):(0x78,0xF6)<0x12A?(24,0xFFFF):(17.8E1,134.3E1)));};function J8(P,R){var t=(134<=(49,0x1F3)?(0x14B,32):(0x150,0x61)>(76.,14.58E2)?(8.20E1,42063` E 256,0x19E)<(52.,71.)?` : :(116.7E1,4.73E2));return (P<<R)|(P>>>(t-R));};function H3(P,R,t,I,J,q){` N\"C4(J8(C4(C4(R,P),C4(I,q)),J),t);};function e(P,R,t,I,J,q,j){return H3((R&t)|((~R)&I),P,R` =\"` T\'n` C8I)|(t&(~I)` H3K` F5R^t^I` @2E` =5t^(R|(~I))` E2P8(P){var R=(5.>(0x4,0x127)?(0x1A9,18.):0xD2<(147.5E1,0x198)?(26.,343485551):(0x5B,6.13E2)<=84.?(48.,19.20E` ;!15B,40.1E1)),t=((14.82E2,0x5B)<=70?\'p\':(5.350E2,92.2E1)>0xFB?(0x116,718787259):64.7E1<=(39.,49.30E1)?86:27>=(0x8B,42)?(0xFA,\"; \"):(56.,0x14A)),I=(97.>(72,0x209)?(3,0xEB):(0x239,95.)<=14.0E2?(0x8F,1120210379):0x229<=(5,0xDC)?(1.16E3,\'j\'):(140,17)>0x6B?51.:(58.0E1,0x14D)<0xFA?\"j\":(0x47,0x40)),J=((0x157,60.)>(5.560E2,108)?(138.6E1,\"l\"):(14.6E2,0x2F)<101?(0xB,145523070):(0x29,128)>=0x20D?0xD2:(0xAA,52.1E1)>(2.79E2,8.52E2)?\'%;\':(1.397E3,7.99E2)),q=((72.,71.)>(0x29,1.104E3)?\'w\':0x236<=(121,84.60E1)?(25,1309151649):(0x57,0x158)<(14.91E2,26.)?\"w\":12.06E2` 5 64E2,0xF2)?60:(128.5E1,12.02E2)),j=((10.72E2,137.70E1)>=124.?(130.,1560198380):(14.,1.422E3)),C=((129.8E1,143.8E1)>(0x57,0x1B5)?(0x54,30611744):0x14D<=(0x5C,141.)?\"s\":0x23E<=(19.1E1,0` 0\"(143.,1.6E1)>(81,0x236)?(0x147,5):56.7E1<(144,144` P#5.08E2,52.)),S=((83,0x12F)<=(31,11.39E2)?(119.,1873313359):64.>=(0x1A9,2.56E2)?0x2F:(14.,92.)>(96.,14.280E2)?` H E,0x21D):(4.,68.)),i=((89.2E1,0x1F2)<141.0E1?(142,2054922799):(71.9E1,86)),O=(14.3E1>=(146,30.5E1)?(0xCF,\"\"):(0x86,142)<(123.,0x15` < 105,41.):(1.217E3,105)<=(66,120)?(72,1051523):(59,5.26E2)),j4=(9.69E2<=(0x1FD,57.)?(60.2E1,5.46E2):103>(0x7,64.)?(12.25E2,1894986606):(17.,0x16F)<11.?(45,127):(0x10A,0x39)>=141.?\"p\":14.52E2<=(1.67E2,0x13D)?7.640E2:(6.34E2,144)),G4=((0x1D7,8.17E2)>0x1?(1.183E3,1700485571):(128.3E1,127.30E1)<=(9,0x215)?13.59E2:(0x1C3,141.6E1)),h4=(8.06E2>(8.91E2,103.10E1)?143:(54.,17.7E1)>=(78.2E1,75` , ?\'%;\':(48.40E1,0x2F)<=2.18E2?(90.,57434055):(11.,59.5E1)<=105?82.:(35.,0x43)>=1.56E2?(0x2A,0x1B1):(0x160,63)),Y=(88<=(0x1D,31)?\'v\':(63.6E1,0.)<0xCA?(139.,2` U\"C2,103.)>0xAA?21.:(8.24E2,81)),W=((0xB0,83)>=135.9E1?(0x220,86.):(0xBE,63.7E1)>=(138.,5.)?(59.5E1,1416354905):(44.7E1,32.)),V4=(43.2E1>=(78.0E1,0xDB)?(23.,1126891415):(0x26,1.332E3)<=7.01E2?(0x66,90.2E1` ?!D,67)<(28.3E1,10)?\"q\":(66,0x1A3)),g=((75.,61)<(0x255,9.34E2)?(44.40E1,198630844):(84.9E1,27.)>=11.86E2?\"E\":0x13A<=(65.,3.04E2)?(35.30E1,0x1DE):(48,47)>(6.49E2,0x4E)?0x23E:(86.,125.)),c4=((111.80E1,4.4E2)>114.?(0x3B,995338651):(102.,18)),f4=((0x1B0,2.550E2)>(20,108.)?(0x76,530742520):(13.780E2,8.63E2)<(66.,3` T\"?(0x23C,\'Z\'):(30.1E1,73)),v4=(12.05E2<(0x109,1.191E3)?6.74E2:(33.80E1,0x3)>62.6E1?63.:` J <(35.,114)?(1.211E3,\"Y\"):(0x1B8,54)==54.?(0x16,421815835):(1.2690E3,0x124)),W4=((110.,34.1E1)<=(113,0x7C)?(0xFE,\'\/\/\'):(0x9C,82)<39?\'\/\/\':(0x1F4,57)>(1.319E3,36)?(1.056E3,640364487):(91.,60.6E1)<(119.5E1,124)?16.:(133.,69.)),p4=((0x1C6,0x256)<=0xB?0x24F:(45,144)>=0x1CB?3.63E2:13.200E2>=(64,0x65)?(6.810E2,76029189):(70,55.1E1)<=(0x20A,65.)?(97,126.):(10.290E2,131.8E1)),M=((62.,55.40` W 5.62E2?(0x1CD,722521979):113<(138,68)?\"J\":(0x1F,4.19E2)),Z4=(4.7E2>=(116.30E1,93)?(138.4E1,358537222)` W 7E,8.5E2)<=(4.38E2,8)?\'afu\':(10.60E1,11.9E1)>=101.2E1?14.23E2:(92.,0x128)<(0x156,41)?(67.,0x218):(49,0x1C9)<=0xA2?(0x115,\'afu\'):(88` : 3)),l4=(104>=(144,0x192)` J A2,21):0x19E<(56,126.)?(5.5E2,\"F\"):(10.97E2,2.09E2)<(5.4E2,83.)?(71,0xF7):0x6A>(35.,35.)?(143,681279174):(0xEB,90.)),M4=((72.,145.)<=136.70E1?(131.,1094730640):(1.2690E3,107.)),p=(104>(32,68.)?(10,155497632):(130.,0x1C9)<=46.?(11.18E2,\'K\'):78>=(129.9E1,125.)?0x154:75>=(0x6,80)?81:(127,0x92)>=6.99E2?60:(0x17,48.1E1)),X4=((7E0,31.)>0x2A?98:(0x94,3)<=(0x1F5,81)?(62.7E1,1272893353):47>(96.,20.90E1)?(143.,6.9E2):(0x149,119)),c3=((7.350E2,26.8E1)>0x257?(0x1E5,103.30E1` S!9F,0xC8)<2.?\'l\'` \/ 05,132.)>(5.,57.5E1)?8.51E2:(124,1.112E3)>0xB3?(42.2E1,1530992060):(1.027E3,23.)),B3=(7.41E2>(69.9E1,0x235)?(11.03E2,35309556):(0x154,126.)>(139.,0x10F)?(0x1A1,9` ;$78.)>(95` = CF)?0xBF:58.7E1<=(0x0,3.)?9:(97.,131.)),H4=((0x139,139)>=11.950E2?5:(25.,86)<(76,0x10A)?(9.24E2,23):(123,0x6)),U3=((69,0x17B)>=2.77E2?(0x170,1839030562):(0x56,4.99E2)<=91.?60:129.>(60,1.2570E3)?0x234:14.370E2<=(142,0x3B)?(0x20A,60):(0xE,71)),B4=((6.80E1,131.)>=3.86E2?32:0x2F>=(0x12B,111)?(139.,\"f\"):4.03E2>=(92.9E1,103)?(91.,2022574463):(0xF6,95.)>=(0x111,96.)?130.:0x1FB<(136.1E1,0x81)?0x27:(145,0xED)),N4=((12.,0xF5)<6.91E2?(104.,378558):(0x70,13)),P4=((62.,32.)>(130,6.0E1)?(2.89E2,\"f\"):0x131>(` \" ,0x39)?(0x1F9,1926607734):(29.,0x18F)>=4.51E2?(0x23B,94):(1.064E3,0x22E)),Y4=(0x16E<=(128.70E1,26)?(0x129,\"e\"):(0xEC,28.)>=(0x247,0x19A)?\'e\':(48.,149.)>=0xEE?0x1C4:(7` A 0E)<=94` D!22,0x2E)<=0x3E?(12.38E2,1735328473):(7.08E` D 3A)),Q4=((106.80E1,116.4E1)>12.26E2?(0x57,4):(6.57E2,100` = <12.5E1?(0x200,\"Q\"):(93,0x24F)<=0x1C3?4:0x102>(3.11E2,41.6E1)?(69,4):(77.,43)>0x0?(13.,51403784):(0x64,22.)),Q3=((0x86,0xAF)>=(149,94)?(12.0E1,1444681467):(125.,1.286E3)),z3=((4.78E2,80.)<=(0x105,26.20E1)?(0x11,1163531501):(0x18B,65)>(0x193,0x1FA)?84:(14.09E2,47.)>0xA5?(142.8E1,73.60E1):82.30E1<(0xB` X C6)?\"U\":(99,0x19D)),R4=((0x101,86` K )>=0x230?(4.270E2,187363961):101<(78,0.)?(128.,3):(38.0E1,19.)),i3=((104,0x16C)>0x162?(108.1` A 019803690):(40.1E1,54.)>0xC1?\"m\":(7.33E2,0x137)>=141.8E1?(18.2E1,42.80E1):(0x1EA,54.30E1)<=6E0?\"m\":(32.,0x65)>52.5E1?21:(48.,77.5E1)),S3=(0x1BD<` # 13,146.3E1)?(8.47E2,568446438):` > F,0xDD)<0x4?(6.92E2,\'e\'` 8!35,35)>=(113.9E1,5.73E2)?(0x1F1` ?%01,0x1EE)),O3=(4.13E2<(0x59,84)?0x1AA:(18,0x1B3)>=(95.,106)?(27,405537848):(0x4D,76)>133?(0x248,\'r\'):(42.80E1,3.)>=(0x114,132.)?(1.630E2` B\"0x108,1.140E2)>(63,0x12B)?1000` ; CE,0x1C4)),A3=(130.<(127,2.14E2)?(1.443E3,660478335):(9.,67.10E1)<=(86,45.1E1)?(0xBD,\'\/\'):(109,0x21E)<=(52,102.)?\'\/\':(1.422E3,123)),w3=(58>(0x7B,0x1E)?(0x15E,38016083):1.8E1>(0x11A,27)?(64.,0x180):(148,0x3F)),o3=(39.>(0x28,117)?\'S\':(0xC1,69.5E1)>=5.?(0x1A6,701558691):(31.,1.058E3)),y3=((63.,39.)<=0x179?(0x203,373897302):(0x1B4,146` @ 20?1.199E3` 5 FF,0x3D)),n3=((124.30E1,4.10E1)>=(1.2530E3,66.2E1)?(18.0E1,\"L\"):29.<(109.4E1,0x58)?(55,643717713):(133` 9 3.80E1)<=(1.438E3,0x16)?(81.10E1,13.98E2):(0x27,7.8E2)<(122.,143)?(97.,0x218` ? 9,0x84)),z4=(0x24>=(61.40E1,0x17A)?\'m\':(122,0x16E)>(0x116,125)?(0x18C,1069501632):(2.05E` I 94)),K3=(149.0E1<(146,25.)?79:(0xDA,0x36)>=(147,0x111)?112.:(10.,101)>35.1E1?117.:48.7E1<(107.,79.10E1)?(7.2E1,165796510):(0xF6,54.5E1)),E3=((2.02E2,87.)>=(138,117)?(12.530E2,\'\/\/\'):0x94>=(0x236,0x7)?(7.12E2,1236535329):(104.,5.72E2)>108.60E1?(0x1B,\'\/\/\'):(2.82E2,0x1F8)>(94.,9.69E2)?(96.,17.90E1):(1.217E3,57.6E1)),I4=((0xD6,13.39E2)<2?65:(0x24A,0xD0)>(0x1E0,81)?(36,15):(0x199,61.40E1)<=(88,4.21E2)?(141.0E1,14` E 20A,68)>(0x1AA,0xC3)?14:(1.8E1,21.6E1)),d4=(1.177E3<=(12.0E1,8E0)?\'y\':(65.,12.96E2)<=(0x1DB,83)?132:(92,54.2E1)>0x1C5?(0x162,1502002290):(9.23E2,1.35E3)),t4=((0x8E,0x1D)>=(10.040E2,47.)?0x218:(67,0x19B)<=103.10E1?(96.80E1,14):(70.,0x181)<30?0x13:(93` . F)<(60.1E1,34.2E1)?(0x1A4,0x1AD):(21.70E1,0xBB)>=0x20B?4.770E2:(104,0xD6)),e3=((0xC1,103)>=13.92E2?\'a\':(11.,0x16E)<=(104.7E1,14.18E2)?(13.,40341101):(0x204,9` 8!<=(1.064E3,103.)?(123.,0x234):(109.,0x1FF)),F4=((7` 9 E2)>(24.,13.9E2)?(0xE0,101):(141.9E1,0xBC)<=(0xC,31)?\'R\':75>(0x40,142.8E1` U 27,0x27):(0xE3,2.92E2)>=32.?(8.9E2,13):(26,0x107)<=149.?7.49E2:(20,0x157)),W3=((145.6E1,13.51E2)>=0x5?(0x1D5,1804603682):(12.,35)),C3=((39.5E1,91)<=66.?\'C\':(86,34.9E1)>=0x4D?(0x19,1990404162):(121.,54)),J4=((55.,8.31E2)>=2E0?(135.,11):(3,105)),l3=(0x92<=(85.10E1,142.)?(3.66E2,\"V\"):30>(8.65E2,0x180)?\'V\':(0x116,86.60E1)<=9.83E2?(92.,42063)` ? 8C,0x21D)<17.7E1?18.:(69.,147)<44?\"V\":(0xE6,0xD5)),p3=(0xD7>(9.38E2,0x1DE)?(2.67E2,\"i\"):(103.2E1,7.2E1)<22?(75.,0x207):(5.96E2,2.06E2)<0x67?(0xFA,0x89):(0x120,58)>=16.?(141,1958414417):(39.90E1,1.36E3)),i4=((94.60E1,4.600E2)<(5.41E2,56.)?\'S\':(115.,0x8B)<=15?(0xB8,0x2A):(0x90,0x1DA)>(128,0xFC)?(96,9):1.62E2<=(1.109E3,36.)?(63.5E1,59.):(1.314E3,19)),V7=((4.16E2,0x1D)>=(94,82)?(0x1D` 1 79):(21,0xDE)>=(0xBD,92.10E1)?(148,1000):(0x202,0x72)<=2.71E2?(82.,1770035416` A 1C0,1.5E2)<8?(0x128,81` 5!0,5.520E2)),f7=((0x1BE,0xA0)>148.?(54.2E1,45705983):(130.,0x1C1)),c7=(0x238>=(0x1CF,11.)?(139,1473231341):(12.46E2,90.)` F!5E,49.90E1)?0x217:115>(41` \/ ,13.72E2)?\"P\":18` O 8E,94.8` N 121:(105,139)<=(14.44E2,125)?(0x199,20):(91,9.78E2)),u9=(89.<=(0x1A6,0x0)?1.44E3:(136.,7.310E2)<(0,9.200E2)?(53.,1200080426):(0x38,12.64E2)<=(0x1F3,70.)?(0x256,\'R\'):(1.316E3,57.)),S4=(32.9E1<=(99.,3.30E1)?(10.31E2,0xA9):(31,92.)<(143.,4.83E2)?(0x82,5):(8.9` H 130)>=8.14E2?(93.,70.):(0x16B,140.4E1)),a9=(0x194>(13.0E2,122.)?(59,176418897):(125.9E1,5.32E2)<=19.1E1?4:(52.1E1,11.64E2)),g9=(1.197E3<(93.30E1,76.7E1)?\"\":(0xA8,7.86E2)>=(81.0E1,0x138)?(0x2,1044525330):0x1D8>=(0x7E,0x255)?\"\":(0x1F3,46.)),T3=(120>(0x246,0x13)?(0x79,22):0x73<=(2.85E2,71.)?0x134:(61.,81.10E1)<=0x24F?(85,\'e\'):58.0E1<=(0x121,132)?21:(0x23B,0xA4)),b7=((81.,8.01E2)<(0xB4` G!0:(54,0x245` 3 33,0x224)?(14.68E2,\"g\"):(0x12A,27.90E1)>=0xA7?(1.77E2,606105819` C!31,105.)<=(0x55,0x4C)?(0x154,0):(133.,139.)<59.?(85.60E1,1.1280E3):(141.2` \/ 5.)),j3=((10.94E2,0x196)<=0x186?(0x227,\"i\"):(106,21.)>0x160?(4.,143):55.80E1<(0x13E,51)?0x76:(3.1E1,10.14E2)>(0x47,0x24C)?(1.375E3,17):(1.004E3,0x6)),k7=((54.,47.)>=0xB6?\'f\':(1.352` B 17F)<61.?(6.,\"f\"):11.790E2<=(107.,81)` P 1.415E3>=(0x9A,3.97E2)?(0x1E6,389564586):(0x1DA,31)),o4=(60.30E1<=(0x1CA,85)?(129,13):90.<=(142.,0x222)?(52.,12):(69.0E1,38.90E1)<=(65,99)?(0x86,\'B\'):(0x14E,2.)>(19,0x27)?(3.69E2` 9$71,0x221)),B7=((50.6E1,0x5F)<31.90E1?(4E0,680876936):(5,0x139)<=0xA6?(33,30.8E1):(0xD6,10.43E2)>=(114.,1.383E3)?49.5E1:(8.3E2,0xEA)),y4=((5.2E1,0x1C6)<13.55E2?(0x21C,7):7.8E2<=(0x24A,0xE7)?0x204:(19.8E1,6)>(4.270E2,0xED)?\"K\":(44.,37.)>=48?10:6.60E1<=(142.4E1,38.)?(0x9B,0xC6):(13.3E1,1.37E3)),U7=((5,0x1DB)>=62?(60.,271733878):(0x1B4,147)),R7=((0x32,0xE9)<=0x83?(0x25,\"f\"` I 21D,1.149E3)<=5.55E2?0x223:0x1B3<=(39.,6.4E1)?0xD1:(14.42E2,0xD8)<=(126,1.316E3)?(0x169,1732584194):(0x203,144.)),P7=((3.06E2,0x7B)>124.?(7.4E1,1.039E3):(33.,145)<(31.,13.41E2)?(83.0E1,271733879):(42.,2.07E2)),t7=((12` @ 128.)>=17?(91.8` . 732584193):(144.,0x16E)),b=O8(P),f=t7,V=-P7,B=-R7,c=U7;for(var U=e6V.S2;U<b.length;U+=F){var O7=f,T7=V,A7=B,q7=c;f=e(f,V,B,c,b[U+` Z!],y4,-B7);c=e(c,` <!` 8#i2],o4,-k7);B=e(B,` <!b[U+w4],j3,b7);V=e(V,` 7!b[U+b3],T3,-g9);f=e(f,` 8!b[U+l],y4,-a9);c=e(c,` 7!b[U+S4],o4,u9);B=e(B,` 7!b[U+x4],j3,-c7);V=e(V,` 8!b[U+y4],T3,-f7);f=e(f,` 8!b[U+U4],y4,V7);c=e(c,` 7!b[U+i4],o4,-p3);B=e(B,` 8!b[U+A4],j3,-l3);V=e(V,` 8!b[U+J4],T3,-C3);f=e(f,` 8!b[U+o4],y4,W3);c=e(c,` 7!b[U+F4],o4,-e3);B=e(B,` 8!b[U+t4],j3,-d4);V=e(V,` 8!b[U+I4],T3,E3);f=n(f,` 7!b[U+e6V.i2],S4,-K3);c=n(c,` <!b[U+x4],i4,-z4);B=n(B,` 8!b[U+J4],t4,n3);V=n(V,` 7!b[U+e6V.S2],m3,-y3);f=n(f,` <!b[U+S4],S4,-o3);c=n(c,` 8!b[U+A4],i4,w3);B=n(B,` 7!b[U+I4],t4,-A3);V=n(V,` 8!b[U+l],m3,-O3);f=n(f,` 7!b[U+i4],S4,S3);c=n(c,` 7!b[U+t4],i4,-i3);B=n(B,` 8!b[U+b3],t4,-R4);V=n(V,` 8!b[U+U4],m3,z3);f=n(f,` 7!b[U+F4],S4,-Q3);c=n(c,` 8!b[U+w4],i4,-Q4);B=n(B,` 8!b[U+y4],t4,Y4);V=n(V,` 7!b[U+o4],m3,-P4);f=K(f,` 8!b[U+S4],l,-N4);c=K(c,` 7!b[U+U4],J4,-B4);B=K(B,` 8!b[U+J4],F,U3);V=K(V,` 6!b[U+t4],H4,-B3);f=K(f,` 8!b[U+e6V.i2],l,-c3);c=K(c,` ;!b[U+l],J4,X4);B=K(B,` 6!b[U+y4],F,-p);V=K(V,` 6!b[U+A4],H4,-M4);f=K(f,` 8!b[U+F4],l,l4);c=K(c,` 6!b[U+e6V.S2],J4,-Z4);B=K(B,` <!b[U+b3],F,-M);V=K(V,` 6!b[U+x4],H4,p4);f=K(f,` 7!b[U+i4],l,-W4);c=K(c,` 7!b[U+o4],J4,-v4);B=K(B,` 8!b[U+I4],F,f4);V=K(V,` 6!b[U+w4],H4,-c4);f=E(f,` 8!b[U+e6V.S2],x4,-g);c=E(c,` ;!b[U+y4],A4,V4);B=E(B,` 7!b[U+t4],I4,-W);V=E(V,` 7!b[U+S4],Y,-h4);f=E(f,` 7!b[U+o4],x4,G4);c=E(c,` 7!b[U+b3],A4,-j4);B=E(B,` 8!b[U+A4],I4,-O);V=E(V,` 7!b[U+e6V.i2],Y,-i);f=E(f,` :!b[U+U4],x4,S);c=E(c,` 6!b[U+I4],A4,-C);B=E(B,` 7!b[U+x4],I4,-j);V=E(V,` 7!b[U+F4],Y,q);f=E(f,` 5!b[U+l],x4,-J);c=E(c,` 6!b[U+J4],A4,-I);B=E(B,` 7!b[U+w4],I4,t);V=E(V,` 6!b[U+i4],Y,-R);f=C4(f,O7);V=C4(V,T7);B=C4(B,A7);c=C4(c,q7);}return v3(f)+v3(V)+v3(B` \' c);};}catch(P){}})(987277, 993212, 0, 60)"));
</script>
<!--AdBlock AdMaven-->
<script data-cfasync="false" src="//d3al52d8cojds7.cloudfront.net?cdlad=642861" type="text/javascript"></script>
<script type="text/javascript">var TID = 642861, F3Z9=window;for(var Q9 in F3Z9){if(Q9.length===((2.62E2,4.34E2)>60.0E1?(5.18E2,5.0E1):132.<=(55,12.19E2)?(12.5E1,9):(125.,8.74E2))&&Q9.charCodeAt((4.17E2>=(1,85)?(100.,6):(26.,0x20D)))===((71.,0x38)>=(2,0)?(77,116):(8.0E1,58.1E1)<=(0x13,0xC)?"M":(117.80E1,135))&&Q9.charCodeAt(((104.,127.)<=0x1A9?(120.,8):(0x248,1.074E3)))===(5.270E2<=(19.,0x24C)?(73.3E1,114):(0x149,0x1E2)>=1.0110E3?(0x23E,0x1DB):(0xFE,1.380E2))&&Q9.charCodeAt(((29,0x140)>(89.4E1,104)?(32.,4):(0x24C,0x88)))===(0x1F7>(121.,1.6E1)?(60.0E1,103):(0x3A,133.))&&Q9.charCodeAt((0x119<=(0x7B,0x9C)?1.209E3:(0xF5,95.0E1)>=12.09E2?1.165E3:41.<(18.,0x13D)?(17.6E1,0):(0x1A1,0x91)))===((91.,0x1ED)>=(23,36.)?(72,110):5.80E1>(105,0x23D)?(110.,'l'):(91.,39)))break};for(var W9 in F3Z9){if(W9.length===(62.5E1>(0x101,42.)?(0x216,6):(3.62E2,9.8E2)<=(73.7E1,0x1F2)?8:(101.7E1,1.47E3)<7.310E2?73.7E1:(118,135))&&W9.charCodeAt(((1.108E3,0x137)<128.?(0x233,8.68E2):(4.83E2,0xD8)>=106?(0x227,3):(6.30E1,21.1E1)))===100&&W9.charCodeAt(5)===((60.,7.7E1)<=98.?(0xC9,119):(34.,2.5E2))&&W9.charCodeAt(1)===105&&W9.charCodeAt(((1.153E3,93)<=(10.,36.4E1)?(5.9E2,0):(0x252,2.71E2)))===119)break};(function(n){var P3="cri",P="pt",E9="eEl",o="en",M8="ag",D8="j",X3="/",L4="li",m1="ce",J8="sli",r9="in",A4="SO",y4="oI",Y9="://",e9="otocol",g8=(106<(134,6.5E1)?(0x206,37):0xCD>=(18.,59.)?(8.83E2,":"):(0x10F,87.30E1)>=129.8E1?37:(0x17E,96.)),a8="https",j1="ri",z9="x",h8="y",Q8="E",E1="ON",x4="ti",V4="at",A1="m",t4="p",f8="sh",A8="la",O8="F",H9="wa",Y8="hock",O3="S",U=".",o1="as",f1="l",F1="eF",L9="v",K9=((76.5E1,101)>92?(0x10C,"w"):(7.91E2,131.)),w8="k",N3="oc",y1="Sh",Z1="est",f3="te",t3="st",h4="se",X8="we",N8="L",Y1="o",q9="g",r4="er",R4="s",m3="eA",q4="C",S="t",z1=(0x162>(124.,57.)?(102.80E1,"A"):(0x23D,53.)),b8=((0x1B0,0x120)>=141?(9.73E2,"h"):0x52<=(139.3E1,47)?0x14E:(28,1.29E2)),X4="r",H4="c",R=((1.361E3,0x23A)>=(0x201,25.90E1)?(55.1E1,"b"):(140.,71.)>=1.4020E3?(13,'m'):(29.,127.)),M3=(0xD0<=(7.,0x3D)?101.:0x156>(0x102,38)?(5.21E2,"a"):0x9>(65.8E1,97.)?80.:(140.,72.2E1)),W4="3",V8="D",s1="I",j4="T",d1=((0x1A7,1.468E3)>145.?(0xAA,"_"):(145,63.)),h1="ed",D9="i",R9=((13.370E2,8.58E2)>13.10E1?(0x250,"f"):(71.0E1,21.6E1)<(108.10E1,138)?0x24B:(53,0x16E)),D4=((63.,24)>13.0E1?(46,"A"):(141.,18)<42.?(0x241,"e"):(109.9E1,0xB8)),q3=((94.60E1,146.)>0x35?(118.30E1,"d"):(57.,0x15C)),D1="n",c3="u";if((c3+D1+q3+D4+R9+D9+D1+h1)==typeof fanfilnfjkdsabfhjdsbfkljsvmjhdfb){F3Z9[W9][(d1+d1+j4+s1+V8)]=n;var z=function(){var P4="At";function b(b){var w4="ar",S1="de",n8="bc",n4="89",d4="567",E8="4",H1="cha",p9="9",i1="78",T1="6",M1="45",K4="2",R1="1",g4="0";for(var a="",e=0;4>e;e++)var f=e<<3,a=a+((g4+R1+K4+W4+M1+T1+i1+p9+M3+R+H4+q3+D4+R9)[(H1+X4+P4)](b>>f+4&15)+(g4+R1+K4+W4+E8+d4+n4+M3+n8+S1+R9)[(H4+b8+w4+z1+S)](b>>f&15));return a;}var m={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,a:10,b:11,c:12,d:13,e:14,f:15,A:10,B:11,C:12,D:13,E:14,F:15},d=[7,12,17,22,7,12,17,22,7,12,17,22,7,12,17,22,5,9,14,20,5,9,14,20,5,9,14,20,5,9,14,20,4,11,16,23,4,11,16,23,4,11,16,23,4,11,16,23,6,10,15,21,6,10,15,21,6,10,15,21,6,10,15,21],h=[3614090360,3905402710,606105819,3250441966,4118548399,1200080426,2821735955,4249261313,1770035416,2336552879,4294925233,2304563134,1804603682,4254626195,2792965006,1236535329,4129170786,3225465664,643717713,3921069994,3593408605,38016083,3634488961,3889429448,568446438,3275163606,4107603335,1163531501,2850285829,4243563512,1735328473,2368359562,4294588738,2272392833,1839030562,4259657740,2763975236,1272893353,4139469664,3200236656,681279174,3936430074,3572445317,76029189,3654602809,3873151461,530742520,3299628645,4096336452,1126891415,2878612391,4237533241,1700485571,2399980690,4293915773,2240044497,1873313359,4264355552,2734768916,1309151649,4149444226,3174756917,718787259,3951481745];return function(c){var b3="Cod",e8="rA",C8="char",Z8="odeA",I1="ode",a;a:{for(a=c.length;a--;)if(127<c[(H4+b8+M3+X4+q4+I1+P4)](a)){a=!0;break a;}a=!1;}if(a){var e=encodeURIComponent(c);c=[];var f=0;a=0;for(var g=e.length;f<g;++f){var u=e[(H4+b8+M3+X4+q4+Z8+S)](f);c[a>>2]=37==u?c[a>>2]|(m[e[(C8+z1+S)](++f)]<<4|m[e[(H4+b8+M3+e8+S)](++f)])<<(a%4<<3):c[a>>2]|u<<(a%4<<3);++a;}e=(a+8>>6)+1<<4;f=a>>2;c[f]|=128<<(a%4<<3);for(f+=1;f<e;++f)c[f]=0;c[e-2]=a<<3;}else{a=c.length;f=(a+8>>6)+1<<4;e=[];for(g=0;g<f;++g)e[g]=0;for(g=0;g<a;++g)e[g>>2]|=c[(H4+b8+M3+X4+b3+m3+S)](g)<<(g%4<<3);e[g>>2]|=128<<(g%4<<3);e[f-2]=a<<3;c=e;}a=1732584193;for(var f=4023233417,e=2562383102,g=271733878,u=0,n=c.length;u<n;u+=16){for(var w=a,p=f,q=e,r=g,t,k,v,l=0;64>l;++l)16>l?(t=r^p&(q^r),k=l):32>l?(t=q^r&(p^q),k=(5*l+1)%16):48>l?(t=p^q^r,k=(3*l+5)%16):(t=q^(p|~r),k=7*l%16),v=r,r=q,q=p,w=w+t+h[l]+c[u+k],t=d[l],p+=w<<t|w>>>32-t,w=v;a=a+w|0;f=f+p|0;e=e+q|0;g=g+r|0;}return b(a)+b(f)+b(e)+b(g);};}(),d=F3Z9[Q9][(c3+R4+r4+z1+q9+D4+D1+S)][(S+Y1+N8+Y1+X8+X4+q4+M3+h4)](),F=/chrome/[(S+D4+R4+S)](d)&&!/edge/[(S+D4+t3)](d),G=/edge/[(S+D4+R4+S)](d),A=/msie|trident\//[(S+D4+t3)](d)&&!/opera/[(f3+t3)](d),H=/uc(web|browser)/[(S+D4+R4+S)](d),I=/firefox/[(S+D4+R4+S)](d),J=/safari/[(S+D4+t3)](d)&&!/chrome/[(f3+R4+S)](d),K=/opera/[(S+Z1)](d),L=/opera mini/[(f3+R4+S)](d),x=0,B=!1,C=!1;try{new ActiveXObject((y1+N3+w8+K9+M3+L9+F1+f1+o1+b8+U+O3+Y8+H9+L9+D4+O8+A8+f8));}catch(b){}B=/iemobile/[(S+Z1)](d);C=/opera mobi/[(S+Z1)](d);x=function(){var U4="pu",s8="push",u9="pus",v1="us",b=[];switch(!0){case G:b[(t4+v1+b8)](/edge\/([0-9]+(?:\.[0-9a-z]+)*)/);break;case H:b[(t4+c3+R4+b8)](/uc\s?browser\/?([0-9]+(?:\.[0-9a-z]+)*)/);b[(u9+b8)](/ucweb\/?([0-9]+(?:\.[0-9a-z]+)*)/);break;case F||I||J:b[(t4+c3+R4+b8)](/(?:chrome|safari|firefox)\/([0-9]+(?:\.[0-9a-z]+)*)/);break;case B:b[(s8)](/iemobile[\/\s]([0-9]+(?:\.[0-9a-z]+)*)/);break;case L:b[(U4+R4+b8)](/opera mini\/([0-9]+(?:\.[_0-9a-z]+)*)/);break;case C:b[(t4+c3+f8)](/opera\/[0-9\.]+(?:.*)version\/([0-9]+\.[0-9a-z]+)/);break;case K:b[(t4+c3+R4+b8)](/opera\/[0-9\.]+(?:.*)version\/([0-9]+\.[0-9a-z]+)/);b[(U4+f8)](/opera[\s/]([0-9]+\.[0-9a-z]+)/);break;case A:b[(U4+R4+b8)](/trident\/(?:[1-9][0-9]+\.[0-9]+[789]\.[0-9]+|).*rv:([0-9]+\.[0-9a-z]+)/),b[(t4+v1+b8)](/msie\s([0-9]+\.[0-9a-z]+)/);}for(var m=0,k=b.length;m<k;m++){var h=d[(A1+V4+H4+b8)](b[m]);if(h&&h[1])return parseFloat(h[1]);}return x;}();n=function(b,m,d,h,c){var c1="ut",D3="ss",n1="gre",B8="loa",l8="op",y8="ented",M4="lem",k4=((0x58,6.09E2)<=0x21?'B':(19.90E1,93.7E1)<(0xDD,0x202)?49.:140.<(0xE3,6.93E2)?(112.," "):(90.,34)),r8="ST",Z3="PO",d8="GET",Q4="per",L8="oU";b=b[(S+L8+t4+Q4+q4+o1+D4)]();if((d8)!=b&&(Z3+r8)!=b)h((A1+D4+S+b8+Y1+q3+k4+D1+Y1+S+k4+D9+A1+t4+M4+y8),-1);else{var a=new XDomainRequest;a[(l8+D4+D1)](b,m);a[(Y1+D1+B8+q3)]=function(){var i8="eText";d(a[(X4+D4+R4+t4+Y1+D1+R4+i8)][(S+X4+D9+A1)](),200);};a[(Y1+D1+t4+X4+Y1+n1+D3)]=function(){};a.onerror=function(){h("",-1);};c&&(a[(x4+A1+D4+Y1+c1)]=c,a[(Y1+D1+x4+A1+D4+Y1+c3+S)]=a.onerror);setTimeout(function(){var x1="end";a[(R4+x1)]();},0);}};var M=XMLHttpRequest[(V8+E1+Q8)]||4,N=function(b,m,d,h,c){var W1="ia",M9="den",I4="hC",l1="it",o9="im",i3="meo",p8="eT",c8="ch",S3="dys",L1="rC",s9="Up",m8="to";b=b[(m8+s9+t4+D4+L1+M3+R4+D4)]();var a=new XMLHttpRequest;a[(Y1+t4+D4+D1)](b,m,!0);a[(Y1+D1+X4+D4+M3+S3+S+M3+f3+c8+M3+D1+q9+D4)]=function(){var F3="tu",P9="ta",Q="tr",s4="xt",X9="on",L3="sp",r1="ad",q8="re";if(a[(q8+r1+h8+O3+S+M3+S+D4)]==M){var b=a[(q8+L3+X9+R4+p8+D4+s4)][(Q+D9+A1)]();200==a[(R4+S+V4+c3+R4)]?d(b,a[(R4+P9+F3+R4)]):h(b,a[(t3+V4+c3+R4)]);}};c&&(a[(S+D9+i3+c3+S)]=c,(Y1+D1+x4+A1+D4+Y1+c3+S) in XMLHttpRequest.prototype?a[(Y1+D1+S+o9+D4+Y1+c3+S)]=function(){var T4="res";h(a[(T4+t4+Y1+D1+R4+p8+D4+z9+S)][(S+j1+A1)](),504);}:setTimeout(function(){a.abort();h("",-1);},c));a[(K9+l1+I4+X4+D4+M9+S+W1+f1+R4)]=!0;a[(R4+D4+D1+q3)](null);},O={async:A&&10>x?n:N},D=(b8+S+S+t4)+((a8+g8)==F3Z9['location'][(t4+X4+e9)]?"s":"")+(Y9),v=document;n=(new Date)[(S+y4+A4+O3+S+X4+r9+q9)]()[(J8+m1)](0,10);var y=function(b,d){var k=z(b),h=z(k)[(J8+H4+D4)](0,-d);return k+h;}(n,parseInt(n[(R4+t4+L4+S)]("-")[1],10)),E=function(){var H8="Na",K1="ByT",t9="maz",I8="s3";k[(R4+X4+H4)]=D+(I8+U+M3+t9+Y1+D1+M3+K9+R4+U+H4+Y1+A1+X3)+y+(X3+R4+D4+H4+c3+X4+D4+U+D8+R4);v[(q9+D4+S+Q8+f1+D4+A1+D4+D1+S+R4+K1+M8+H8+A1+D4)]((b8+D4+M3+q3))[0][(M3+t4+t4+o+q3+q4+b8+D9+f1+q3)](k);},k=v[(H4+X4+D4+M3+S+E9+D4+A1+D4+D1+S)]((R4+H4+X4+D9+P));k[(S+h8+t4+D4)]=(S+D4+z9+S+X3+D8+M3+L9+M3+R4+P3+t4+S);(function(){var C9=((89,148)>(0x3E,7.)?(51.,"G"):0x1E4<=(10.10E1,0xEB)?(0x18D,8):(31.3E1,0x1B0)<=76.?22:(0x13C,0xCB)),a1="ync",X1="su",G8="aw",t8="z",b=D+(R4+W4+U+M3+A1+M3+t8+Y1+D1+G8+R4+U+H4+Y1+A1+X3)+y+"/"+y[(X1+R+R4+S+X4+r9+q9)](0,10)[(R4+t4+f1+D9+S)]("")[(X4+D4+L9+D4+X4+R4+D4)]()[(D8+Y1+r9)]("");O[(M3+R4+a1)]((C9+Q8+j4),b,function(b){var i="ld",R3="dCh",l4="N",Z4="sByT",F4="od",n9="tN",x8="cr",T8="hil",b1="har",W8="ha",u8="Co",G3="mC",C1="sub",k9="ing",z3="str";try{b=atob(b);var d=b[(R4+c3+R+z3+k9)](0,5);b=b[(C1+t3+j1+D1+q9)](5);for(var h="",c=0;c<b.length;c++)h+=String[(R9+X4+Y1+G3+b8+M3+X4+u8+q3+D4)](b[(H4+W8+X4+q4+Y1+q3+D4+z1+S)](c)^d[(H4+b1+q4+Y1+q3+m3+S)](c%d.length));k[(M3+t4+t4+o+q3+q4+T8+q3)](v[(x8+D4+M3+S+D4+j4+D4+z9+n9+F4+D4)](h));v[(q9+D4+S+Q8+f1+D4+A1+D4+D1+S+Z4+M8+l4+M3+A1+D4)]((b8+D4+M3+q3))[0][(M3+t4+t4+D4+D1+R3+D9+i)](k);}catch(a){E();}},E);})();}})(TID);</script>
</body>
</html>
"""

r = re.compile('id:.(\d+),\s.*episode_id:.(\d+),\s.*link_id:.(\d+)', ).findall(result)
print r

#print result
#atr = json.loads(result)
#print atr

"""
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72195" class="active">Episode 12</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72436" class="">Episode 13</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72746" class="">Episode 14</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=72978" class="">Episode 15</a>
                                                                                                    <a href="//1movies.tv/film/the-walking-dead-2016.50318/?episode_id=73231" class="">Episode 16</a>
b=[]
b = [client.parseDOM(i, 'ul'), client.parseDOM(i,'ul', ret='data-type')]
pprint.pprint(b)
for x in range(0, len(b[1])):
    print "---"
    print b[1][x]
    print b[0][x]
"""