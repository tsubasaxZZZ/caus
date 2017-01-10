# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient  # mongoDB との接続
import datetime

class MauscrapingPipeline(object):
    #def __init__(self, mongo_uri, mongo_db, mongolab_user, mongolab_pass, collection_name1):
    def __init__(self, mongo_uri, mongo_db, collection_name1, collection_name2):
        # インスタンス生成時に渡された引数で、変数初期化
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name1 = collection_name1
        self.collection_name2 = collection_name2
        #self.mongolab_user = mongolab_user
        #self.mongolab_pass = mongolab_pass

    @classmethod  # 引数にクラスがあるので、クラス変数にアクセスできる
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'), # settings.py て定義した変数にアクセスする
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'),
            collection_name1 = crawler.settings.get('MONGO_COLLECTION_NAME1'),
            collection_name2 = crawler.settings.get('MONGO_COLLECTION_NAME2')
            #mongolab_user=crawler.settings.get('MONGOLAB_USER'),
            #mongolab_pass=crawler.settings.get('MONGOLAB_PASS')
        ) # def __init__ の引数になる
                        
    def open_spider(self, spider): # スパイダー開始時に実行される。データベース接続
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

        # index の作成
        self.db[self.collection_name1].create_index([("url", pymongo.DESCENDING), ("condition", pymongo.DESCENDING)], unique=True)        
        self.db[self.collection_name2].create_index([("url", pymongo.DESCENDING)], unique=True)

        #self.db.authenticate(self.mongolab_user, self.mongolab_pass)
        
    def close_spider(self, spider): # スパイダー終了時に実行される。データベース接続を閉じる
        # 重複しているアイテムを結合
        while True:
            update_temp1_item = self.db[self.collection_name1].find_one_and_delete({})
            if update_temp1_item is None:
                break

            dup_updates = update_temp1_item
            while True:
                updates = self.db[self.collection_name1].find_one_and_delete({'url':update_temp1_item['url']})
                if updates is None:
                    break
                print("-------S-DEDUP-----------")
                dup_updates['condition'].extend(updates['condition'])
                print(dup_updates)
                print("-------E-DEDUP-----------")

#            try:
#                self.db[self.collection_name2].insert(dup_updates)
#            except Exception as e:
#                print(e)
        
            exists_item = self.db[self.collection_name2].find_one({'url':dup_updates['url']})
            try:
                # 既に登録済みのアイテムがある場合は、条件のみを更新する(エラー時の再処理のみ)
                # 注意:クロール時は毎回全てのデータを削除することを前提とする
                if exists_item is None:
                    print("------ Item is NOT exists -----")
                    print(exists_item)
                    print("------ Item is NOT exists -----")
                    self.db[self.collection_name2].insert(dup_updates)
                else:
                    print("------ Item is exists -----")
                    exists_item['condition'].extend(dup_updates['condition'])
                    self.db[self.collection_name2].update(
                        {'url':dup_updates['url']},
                        {'$set':
                         {'condition':exists_item['condition']}
                        }
                    )
                    print(exists_item)
                    print("------ Item is exists -----")
            except Exception as e:
                print(e)

        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name1].insert(item)

        return item

