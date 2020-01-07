import os

PhantomJS_PATH = 'D:/Documents/Python37 File/selenium dependency/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe'

Chrome_PATH = 'D:/Documents/Python37 File/selenium dependency/chromedriver.exe'
# 存储根路径
DATA_SAVE_PATH = '../data/'

# 歌曲页的目标链接
#288
liuxing_urls = {u'流行':
                  ['http://music.163.com/#/playlist?id=418165881',
                   'http://music.163.com/#/playlist?id=2585690348',
                   'http://music.163.com/#/playlist?id=942178423']}
#344
gufeng_urls = {u'古风':
                  ['https://music.163.com/#/playlist?id=7373370']}
#194
ertong_urls = {u'儿歌':
                  ['http://music.163.com/#/playlist?id=2251388916']}
#354
rap_urls = {u'RAP':
                  ['http://music.163.com/#/playlist?id=323233144']}

destination_urls = [liuxing_urls,gufeng_urls,ertong_urls,rap_urls]  # 目标url

use_pool = 1  # 1:使用多进程 0:不使用多进程

