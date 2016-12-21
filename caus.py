#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
from datetime import datetime

#DROP_DOWN_ID = {"product" : "dropdown-products", "updateType" : "dropdown-updatetype", "platform" : "dropdown-platform"}
DROP_DOWN_ID = {"product" : "dropdown-products", "updateType" : "dropdown-updatetype"}
MONGODB_HOST = "172.17.0.4"
MONGODB_PORT = 27017

def parse_drop_downlist():
    '''
    ドロップダウンリストの解析 
    '''
    html = requests.get("https://azure.microsoft.com/en-us/updates/").text
    soup = BeautifulSoup(html, "html.parser")

    # ドロップダウンのハッシュ
    option_list = {}

    for dropdownId in DROP_DOWN_ID.values():
        select_html = soup.find_all("select", attrs={"id":dropdownId})[0].find_all("option")
        option_list[dropdownId] = []
        for option in select_html:
            option_list[dropdownId].append(option.get("value"))

    return option_list

def get_update_list(**condition):
    '''
    Update情報の解析
    '''
    html = requests.get("https://azure.microsoft.com/en-us/updates/", params = condition).text
    soup = BeautifulSoup(html, "html.parser")

    # 1件の情報をハッシュ(投稿日,タイトル,概要,URL)として持つリスト
    update_list = []

    div_serviceupdate_list = soup.find_all("div", attrs={"class" : "serviceUpdate"})
    for div_serviceupdate in div_serviceupdate_list:
        update_item = {}
        update_item['title'] = div_serviceupdate.h5.text
        update_item['url'] = div_serviceupdate.a['href']
        update_item['date'] = datetime.strptime(div_serviceupdate.find_all('span', attrs={"class" : "text-slate07"})[0].text, "%B %d, %Y")
        update_item['summary'] = div_serviceupdate.find_all('span', attrs={"class" : False})[0].text.replace('- ','')
        update_item['condition'] = [condition]
        update_list.append(update_item)

    return update_list

def create_updates_db(db):
    '''
    MongoDB へインサート
    '''
    dropdown_list = parse_drop_downlist()

    for dropdown_type, dropdown_listID in DROP_DOWN_ID.items():
        for dropdown_item in dropdown_list[dropdown_listID]:
            # ALLの時はDBへインサートはしない
            if dropdown_item == "":
                continue

            print("============== {}:{} ===========".format(dropdown_type, dropdown_item))

            for page_num in range(1, 20):
                update_list = get_update_list(**dict({dropdown_type:dropdown_item, "page":page_num}))
                if(len(update_list) == 0):
                    break
                for update in update_list:
                    print(update)
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
        db['update_temp2'].insert(dup_updates)

def print_updates(db):
    collection = db['update_temp2']
    for update in collection.find():
        print("Date:{}, Title:{},  Condition:{}".format(update['date'], update['title'], update['condition']))

    
    

if __name__ == "__main__":
    client = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client.aus

    db['update_temp1'].create_index([("url", pymongo.DESCENDING), ("condition", pymongo.DESCENDING)], unique=True)
    db['update_temp2'].create_index([("url", pymongo.DESCENDING), ("condition", pymongo.DESCENDING)], unique=True)
    create_updates_db(db)
    dedup_updates_db(db)

    #print_updates(db)
    #print_updates(db)

