from bs4 import BeautifulSoup
import requests
import json
import os
from logging import getLogger,StreamHandler,DEBUG,Formatter

LIB_DIR = os.path.abspath(os.path.dirname(__file__))
DROPDOWNLIST_CACHE_FILE_PATH = os.path.join(LIB_DIR, 'dropdownlist.cache')
DROP_DOWN_ID = {"product" : "dropdown-products", "updateType" : "dropdown-updatetype", "platform" : "dropdown-platform"}
AZURE_BASEURL = "https://azure.microsoft.com/"
SERVICE_UPDATE_BASEURL = "https://azure.microsoft.com/en-us/updates/"
# ToDo: 一覧にないものをOthersに出す
SERVICE_TYPE = {'service-type': {
    'Platform' : [
        'Application Gateway',
        'Automation',
        'Container Service',
        'Azure DNS',
        'Azure DevTest Labs',
        'Azure Resource Manager',
        'Azure Monitor',
        'Backup',
        'Content Delivery Network (CDN)',
        'Marketplace',
        'ExpressRoute',
        'Key Vault',
        'Load Balancer',
        'Log Analytics',
        'Microsoft Azure portal',
        'Network Watcher',
        'Recovery Manager',
        'Recovery Services',
        'RemoteApp',
        'Scheduler',
        'Site Recovery',
        'StorSimple',
        'Storage',
        'Traffic Manager',
        'VPN Gateway',
        'Virtual Machines',
        'Virtual Machine Scale Sets',
        'Virtual Network'
    ],
    'Application' : [
        'API Management',
        'Access Control Service',
        'App Service',
        'Application Insights',
        'IoT Hub',
        'Azure Search',
        'Batch',
        'BizTalk Services',
        'Cloud Services',
        'Cognitive Services',
        'Event Hubs',
        'Functions',
        'HockeyApp',
        'IoT Suite',
        'Logic Apps',
        'Managed Cache Service',
        'Media Services',
        'Mobile Engagement',
        'Mobile Services',
        'Notification Hubs',
        'Redis Cache',
        'Service Bus',
        'Service Fabric',
        'Stream Analytics',
        'Visual Studio Team Services',
        'Web Apps'
    ],
    'ID & Security' : [
        'Azure Active Directory',
        'Azure Active Directory B2C',
        'Azure Active Directory Domain Services',
        'Multi-Factor Authentication',
        'Security Center'
    ],
    'Data Platform' :[
        'Azure Cosmos DB',
        'Data Catalog',
        'Data Factory',
        'Data Lake Analytics',
        'Data Lake Store',
        'HDInsight',
        'Machine Learning',
        'Power BI Embedded',
        'SQL Data Warehouse',
        'SQL Database',
        'SQL Server Stretch Database'
    ]}}

FORMATTER = Formatter('%(asctime)s - %(name)s.%(funcName)s():%(lineno)s - %(levelname)s - %(message)s')
handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(FORMATTER)
CAUS_LOGGER = getLogger(__name__)
CAUS_LOGGER.setLevel(DEBUG)
CAUS_LOGGER.addHandler(handler)

class Util:
    def __init__(self, logger):
        self.logger = logger.getChild(__name__)

    def parse_drop_downlist(self):
        '''
        ドロップダウンリストの解析とキャッシュファイルへの保存
        '''
        html = requests.get(SERVICE_UPDATE_BASEURL).text
        soup = BeautifulSoup(html, "html.parser")

        # ドロップダウンのハッシュ
        option_list = {}

        for dropdownId in DROP_DOWN_ID.values():
            select_html = soup.find_all("select", attrs={"id":dropdownId})[0].find_all("option")
            option_list[dropdownId] = {}
            for option in select_html:
                # ALL は除く
                if(option.get("value") == ''):
                    continue
                option_list[dropdownId].update({option.text.strip():option.get("value")})

                # サービスとIaaS等の種類のマッピングを追加する
            option_list.update(SERVICE_TYPE)

        # JSON で libs ディレクトリに書き出す
        with open(DROPDOWNLIST_CACHE_FILE_PATH, 'w') as f:
            json.dump(option_list, f)

        return option_list

    def get_drop_downlist(self):
        '''
        ファイルに保存されたドロップダウンリストを取得する
        '''
        option_list = ""
        self.logger.debug("Load JSON file:From=[{}]".format(DROPDOWNLIST_CACHE_FILE_PATH))
        try:
            with open(DROPDOWNLIST_CACHE_FILE_PATH, 'r') as f:
                option_list = json.load(f)
        except Exception as e:
            self.logger.warning(e)

        return option_list

if __name__ == "__main__":
    util = Util(CAUS_LOGGER)
    print(util.parse_drop_downlist())    
