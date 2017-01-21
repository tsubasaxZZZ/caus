# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
from libs.common import Util, SERVICE_UPDATE_BASEURL, DROP_DOWN_ID, CAUS_LOGGER, AZURE_BASEURL
from bs4 import BeautifulSoup
import urllib
import requests
from datetime import datetime
from scrapy import Spider
from scrapy.http import Request
from mauscraping.items import MauscrapingItem
from scrapy.crawler import CrawlerProcess
import pymongo
from pymongo import MongoClient
import unicodedata

#DROP_DOWN_ID = {"product" : "dropdown-products"}

class AzureupdateSpider(Spider):
    name = "azureupdate"
    allowed_domains = ["azure.microsoft.com"]

    def __init__(self, baseurl=None, *args, **kwargs):
        super(AzureupdateSpider, self).__init__(*args, **kwargs)        
        self.baseurl = baseurl

    def start_requests(self):
        util = Util(CAUS_LOGGER)
        dropdown_list = util.get_drop_downlist()

        # 引数でURL指定されている場合はそのURLのみクロール
        # ex)scrapy crawl azureupdate -a baseurl=https://azure.microsoft.com/en-us/updates/?updateType=compliance
        if self.baseurl is not None:
            yield Request(self.baseurl, self.parse_item)
        else:
            for dropdown_type, dropdown_value in DROP_DOWN_ID.items():
                for _key, _val in dropdown_list[dropdown_value].items():
                    url = SERVICE_UPDATE_BASEURL + "?" + urllib.parse.urlencode({dropdown_type:_val})
                    yield Request(url, self.parse_item, errback=self.errback)

    def parse_item(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        
        div_serviceupdate_list = soup.select('#top > main.wa-container > section.section > div.row.serviceUpdates-container > div.column > div.row.row-size1')
        for div_serviceupdate in div_serviceupdate_list:
            # items.py で定義したクラス
            update_item = MauscrapingItem()            
            update_item['title'] = div_serviceupdate.h5.text
            update_item['url'] = div_serviceupdate.a['href']
            update_item['baseurl'] = response.url

            # サマリの取得
            summary_html = requests.get(AZURE_BASEURL + "/" + update_item['url']).text
            summary_html = unicodedata.normalize('NFKC', summary_html).encode('ascii','ignore')
            summary_soup = BeautifulSoup(summary_html, "html.parser")
            date_html = summary_soup.select('#top > main.wa-container > section.section > div.row > div.column > p')[0].text
            update_item['date'] = datetime.strptime(date_html,"%A, %B %d, %Y")

            update_item['summary'] = ''.join([s.text for s in summary_soup.select('#top > main > section.section > div.row.row-size3 > div.column.small-12.medium-9')])
            if update_item['summary'] == '':
                update_item['summary'] = ''.join([s.text for s in summary_soup.select('#top > main.wa-container > section.section > div.row.row-size3 > div.column.small-12')])

            c = urllib.parse.parse_qs(urllib.parse.urlparse(response.url).query)
            
            # flatten
            for _key, _list in c.items():
                for v in _list:
                    c[_key] = v

            update_item['condition'] = [c]

            self.logger.debug(update_item)

            yield update_item

        # ページングへの対応
        next_page = None
        try:
            next_page = soup.select('#top > main > section > div.row.column > div > ul > li > a')[-1].get("href")
        except Exception as e:
            self.logger.debug(e)

        if next_page:
            url = AZURE_BASEURL + next_page
            yield Request(url, callback=self.parse_item, errback=self.errback)


    def errback(self, failure):
        self.logger.error("**** ERROR ****:{},{}".format(repr(failure), repr(failure.value)))
