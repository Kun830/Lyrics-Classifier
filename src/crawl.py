import sys
sys.path.append('..')
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
from conf.crawl_conf import Chrome_PATH,PhantomJS_PATH,DATA_SAVE_PATH, destination_urls, use_pool


class Crawl(object):
    def __init__(self):
        self.save_path = DATA_SAVE_PATH
        if os.path.exists(self.save_path) is not True:
            os.mkdir(self.save_path)
        self.urls = destination_urls

    @staticmethod
    def crawl_url(dic_urls):
        urls = list(dic_urls.values())[0]
        label = list(dic_urls.keys())[0]
        results = {}
        for url in urls:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            driver = webdriver.Chrome(Chrome_PATH,chrome_options=option)
            driver.get(url)
            driver.switch_to.frame('g_iframe')
            page = driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            body = soup.find('tbody')
            lists = body.find_all('tr')
            for l in lists:
                span = l.find('span', class_='txt')
                title = span.find('b')['title']
                url = 'http://music.163.com/#' + span.find('a')['href']
                print(url)
                results.setdefault(title, url+'\t'+label)
        return results

    @staticmethod
    def crawl_lyrics(url):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(Chrome_PATH,chrome_options=option)
        driver.get(url)
        driver.switch_to.frame('g_iframe')
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        content = soup.find('div', class_='cnt').get_text()
        print('success')
        pos = content.index('>')
        result = content[pos+1:]
        return result

    def write_to_txt(self, results, path):
        count = 0
        for key, value in results.items():
            try:
                url = value.strip().split('\t')[0]
                lyrics = self.crawl_lyrics(url).split(':')[-1]
                label = value.strip().split('\t')[1]
                if os.path.exists(os.path.join(path, label)) is not True:
                    os.mkdir(os.path.join(path, label))
                with open(os.path.join(path, label, str(count)+'.txt'), 'w',encoding='utf-8') as f:
                    f.write(lyrics)
                count += 1
            except:
                print("Error")
            else:
                print("Write Success")

    def run(self):
        results = []
        for urls in self.urls:
            result = self.crawl_url(urls)
            results.append(result)
        if use_pool:
            p = Pool(len(results))
            for i in range(len(results)):
                p.apply_async(self.write_to_txt(results[i], self.save_path))
            p.close()
            p.join()
        else:
            for result in results:
                C.write_to_txt(result, C.save_path)


if __name__=='__main__':
    C = Crawl()
    C.run()