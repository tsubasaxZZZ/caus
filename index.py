# -*- coding:utf-8 -*-

import math
import os
from bottle import route, run, default_app, get, post, request, static_file
from bottle import TEMPLATE_PATH, jinja2_template as template
import pymongo
from pymongo import MongoClient
import re
from libs.common import Util, DROP_DOWN_ID, CAUS_LOGGER

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
#TEMPLATE_PATH.append(BASE_DIR + "/views")


# ToDo:コンフィグ化
MONGODB_HOST = "aus-db"
MONGODB_PORT = 27017
NUM_PER_PAGE = 20
COLLECTION_NAME = 'update_temp2'
DATABASE_NAME = 'aus-copy'

@route('/')
def servicelist():
    client = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client[DATABASE_NAME]
    

    condition = {}
    # ToDo: クエリのキーをドロップダウンリストから取ってくる
    for type_str in ("product", "updateType", "platform"):
        # 複数選択に対応
        query = request.query.getall(type_str)
        if len(query) > 0:
            # 条件式の組み立て
            condition.update({'condition.{}'.format(type_str):{'$in' :query}}) 


    '''
    # ORで検索
    if condition != {}:
        temp_arr = []
        for k,v in condition.items():
            temp_arr.append(dict({k:v}))
        condition = {'$or': temp_arr}
    # ---------
    '''

    # ToDo: ログ出力
    print(condition)

    # ソート
    sort = request.query.get("datesort") or -1

    # 件数
    itemnum = db[COLLECTION_NAME].find(condition).count()

    # 最大ページ数
    max_pagenum = math.ceil(itemnum / NUM_PER_PAGE)

    # ページネーション
    # ToDo: 適当なページネーションをちゃんと修正する
    try:
        page = int(request.query.get("page") or 1)
    except Exception as e:
        print(e)
        page = 1
    prev_page = 1 if page <= 1 else page - 1
    next_page = page + 1 if page < max_pagenum else max_pagenum

    if re.search("page=", request.query_string):
        prev_page_query = re.sub('page=([^&]*)', 'page={}'.format(prev_page), request.query_string)
        next_page_query = re.sub('page=([^&]*)', 'page={}'.format(next_page), request.query_string)
    else:
        prev_page_query = request.query_string
        next_page_query = '{}&page={}'.format(request.query_string, next_page)
        

    # クエリの発行
    list_db = list(db[COLLECTION_NAME]
             .find(condition)
             .sort("date", sort)
             .skip(NUM_PER_PAGE * (page - 1))
             .limit(NUM_PER_PAGE))

    '''
    #-- temp1 から抽出 --
    list_db_by_url = [db[COLLECTION_NAME].find({'url':u['url']}) for u in list_db]
    update_list = list()
    from collections import deque
    list_db_queue = deque(list_db)
    list_db_by_url_queue = deque(list_db_by_url)

    while len(list_db_queue) > 0:
        list_db_item = list_db_queue.popleft()
        while len(list_db_by_url_queue) > 0:
            list_db_by_url_item = list(list_db_by_url_queue.popleft())
            for same_url_item in list_db_by_url_item:
                if list_db_item['url'] == same_url_item['url']:
                    list_db_item['condition'].extend(same_url_item['condition'])
        update_list.append(list_db_item)
    #---------------------
    '''

    # ドロップダウンリストの取得
    util = Util(CAUS_LOGGER)
    dropdown_list = util.get_drop_downlist()

    return template(
        'servicelist',
        update_list=list_db,
        request=request,
        pageinfo=dict({"page":page, "condition":condition, "itemnum":itemnum, "max_pagenum":max_pagenum}),
        prev_page_query = prev_page_query,
        next_page_query = next_page_query,
        product_list = dropdown_list[DROP_DOWN_ID['product']],
        updatetype_list = dropdown_list[DROP_DOWN_ID['updateType']],
        platform_list = dropdown_list[DROP_DOWN_ID['platform']],
        service_type_list = dropdown_list['service-type']
    )

@route('/static/<file_path:path>')
def static(file_path):
        return static_file(file_path, root=BASE_DIR + '/static')

if __name__ == '__main__':
    # コマンドから"python3 index.py"で起動した場合
    run(host='0.0.0.0', port=8080, debug=True)

else:
    # uWSGIから起動した場合
    application = default_app()
