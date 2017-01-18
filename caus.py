#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
from datetime import datetime
from libs.common import DROP_DOWN_ID, Util, SERVICE_UPDATE_BASEURL, AZURE_BASEURL, CAUS_LOGGER
from pprint import pformat


#DROP_DOWN_ID = {"product" : "dropdown-products", "updateType" : "dropdown-updatetype"}
MONGODB_HOST = "aus-db"
MONGODB_PORT = 27017
# スクレイピングするページ数
MAX_PAGING = 100

def get_update_list(**condition):
    '''
    Update情報の解析
    '''
    
    html = requests.get(SERVICE_UPDATE_BASEURL, params = condition).text
    soup = BeautifulSoup(html, "html.parser")

    # 1件の情報をハッシュ(投稿日,タイトル,概要,URL)として持つリスト
    update_list = []

    #div_serviceupdate_list = soup.find_all("div", attrs={"class" : "serviceUpdate"})
    div_serviceupdate_list = soup.select('#top > main.wa-container > section > div.row.serviceUpdates-container > div.column > div.row.row-size1')
    for div_serviceupdate in div_serviceupdate_list:
        update_item = {}
        update_item['title'] = div_serviceupdate.h5.text
        update_item['url'] = div_serviceupdate.a['href']

        # サマリの取得
        summary_html = requests.get(AZURE_BASEURL + "/" + update_item['url']).text
        summary_soup = BeautifulSoup(summary_html, "html.parser")
        date_html = summary_soup.select('#top > main.wa-container > section.section > div.row > div.column > p')[0].text
        update_item['date'] = datetime.strptime(date_html,"%A, %B %d, %Y")
#        update_item['summary'] = ''.join([text.text for text in summary_soup.select('#top > div.wa-container > section.section > div.row.row-size3 > div.column.small-12.medium-9 > p')])
#        update_item['summary'] = summary_soup.select('#top > main.wa-container > section.section > div.row.row-size3 > div.column.small-12.medium-9 > p')
        update_item['summary'] = ''
        update_item['condition'] = [condition]
        CAUS_LOGGER.debug(update_item)
        update_list.append(update_item)

    return update_list

def create_updates_db(db):
    '''
    MongoDB へインサート
    '''
    util = Util(CAUS_LOGGER)
    dropdown_list = util.get_drop_downlist()
    
    for dropdown_type, dropdown_value in DROP_DOWN_ID.items():
        for _key, _val in dropdown_list[dropdown_value].items():

            CAUS_LOGGER.debug("*** DROPDOWN_TYPE=[{}], DROPDOWN_LIST_KEY=[{}], DROPDOWN_LIST_VAL=[{}] ***".format(dropdown_type, _key, _val))
            for page_num in range(1, MAX_PAGING):
                update_list = get_update_list(**dict({dropdown_type:_val, "page":page_num}))
                if(len(update_list) == 0):
                    break
                for update in update_list:
                    try:
                        db['update_temp1'].insert(update)
                    except Exception as e:
                        print(e)

def dedup_updates_db(db):
    while True:
        update_temp1_item = db['update_temp1'].find_one_and_delete({})
        if update_temp1_item == None:
            break
        dup_updates = update_temp1_item
        while True:
            updates = db['update_temp1'].find_one_and_delete({'url':update_temp1_item['url']})
            if updates == None:
                break
            print("-------S-DEDUP-----------")
            dup_updates['condition'].extend(updates['condition'])
            print(dup_updates)
            print("-------E-DEDUP-----------")
        try:
            db['update_temp2'].insert(dup_updates)
        except Exception as e:
            print(e)

def print_updates(db):
    collection = db['update_temp2']
    for update in collection.find():
        print("Date:{}, Title:{},  Condition:{}".format(update['date'], update['title'], update['condition']))

    
    

if __name__ == "__main__":
    client = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client.aus

    db['update_temp1'].create_index([("url", pymongo.DESCENDING), ("condition", pymongo.DESCENDING)], unique=True)
    db['update_temp2'].create_index([("url", pymongo.DESCENDING)], unique=True)
    create_updates_db(db)
    dedup_updates_db(db)

    #print_updates(db)
    #print_updates(db)

