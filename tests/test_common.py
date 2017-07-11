# coding: utf-8

from libs.common import DROP_DOWN_ID, Util, SERVICE_UPDATE_BASEURL, AZURE_BASEURL, DROPDOWNLIST_CACHE_FILE_PATH
import unittest
from logging import getLogger,StreamHandler,DEBUG,Formatter,WARNING

import os

from pprint import pprint

class TestCommon(unittest.TestCase):
    def setup_class():
        # ロガーの設定
        formatter = Formatter('%(asctime)s - %(name)s.%(funcName)s():%(lineno)s - %(levelname)s - %(message)s')
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)

        TestCommon.logger = getLogger(__name__)
        TestCommon.logger.setLevel(DEBUG)
        TestCommon.logger.addHandler(handler)

        # キャッシュファイルの削除
        try:
            os.remove(DROPDOWNLIST_CACHE_FILE_PATH)
        except:
            pass

        TestCommon.dropdown_expect = {"dropdown-products": {"Content Delivery Network (CDN)": "cdn", "Key Vault": "key-vault", "Azure Monitor": "monitor", "Virtual Machines": "virtual-machines", "StorSimple": "storsimple", "Recovery Manager": "recovery-manager", "Security Center": "security-center", "Mobile Engagement": "mobile-engagement", "Access Control Service": "access-control", "Mobile Services": "mobile-services", "API Management": "api-management", "Azure Active Directory B2C": "active-directory-b2c", "Marketplace": "marketplace", "Data Lake Analytics": "data-lake-analytics", "Azure Cosmos DB": "cosmos-db", "Data Lake Store": "data-lake-store", "Batch": "batch", "Virtual Network": "virtual-network", "Application Insights": "application-insights", "RemoteApp": "remoteapp", "IoT Hub": "iot-hub", "Application Gateway": "application-gateway", "Network Watcher": "network-watcher", "Traffic Manager": "traffic-manager", "ExpressRoute": "expressroute", "Azure DNS": "dns", "Cloud Services": "cloud-services", "Automation": "automation", "Notification Hubs": "notification-hubs", "Event Hubs": "event-hubs", "Machine Learning": "machine-learning", "Power BI Embedded": "power-bi-embedded", "Virtual Machine Scale Sets": "virtual-machine-scale-sets", "Microsoft Azure portal": "azure-portal", "HockeyApp": "hockeyapp", "SQL Data Warehouse": "sql-data-warehouse", "Azure Resource Manager": "azure-resource-manager", "VPN Gateway": "vpn-gateway", "Data Factory": "data-factory", "Recovery Services": "recovery-services", "SQL Database": "sql-database", "Stream Analytics": "stream-analytics", "Functions": "functions", "Multi-Factor Authentication": "multi-factor-authentication", "SQL Server Stretch Database": "sql-server-stretch-database", "Data Catalog": "data-catalog", "IoT Suite": "iot-suite", "Site Recovery": "site-recovery", "Scheduler": "scheduler", "Container Service": "container-service", "Web Apps": "web-sites", "Backup": "backup", "HDInsight": "hdinsight", "Cognitive Services": "cognitive-services", "Log Analytics": "log-analytics", "Service Fabric": "service-fabric", "Media Services": "media-services", "Azure Active Directory Domain Services": "active-directory-ds", "Logic Apps": "logic-apps", "Load Balancer": "load-balancer", "Service Bus": "service-bus", "Visual Studio Team Services": "visual-studio-team-services", "Azure DevTest Labs": "devtest-lab", "Managed Cache Service": "cache", "Azure Search": "search", "Azure Active Directory": "active-directory", "Redis Cache": "redis-cache", "Storage": "storage", "BizTalk Services": "biztalk-services", "App Service": "app-service"}, "service-type": {"Platform": ["Application Gateway", "Automation", "Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Azure Monitor", "Backup", "Content Delivery Network", "Marketplace", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Network Watcher", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Machine Scale Sets", "Virtual Network"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services", "Web Apps"], "Data Platform": ["Azure Cosmos DB", "Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "Power BI Embedded", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"]}, "dropdown-platform": {"PowerShell": "powershell", "Linux cluster": "linux-cluster", "Java": "java", "Xamarin": "xamarin", "XPlatCLI": "x-plat-cli", "Node.js": "nodejs", "iOS": "ios", "Python": "python", "PHP": "php", "Media": "media", "Android": "android", "Windows cluster": "windows-cluster", "Windows": "windows", "Rest": "rest", "Ruby": "ruby"}, "dropdown-updatetype": {"Features": "features", "Regions and Datacenters": "regions-and-datacenters", "Pricing & Offerings": "pricing-offerings", "SDK and Tools": "sdk-and-tools", "Preview": "preview", "Management": "management", "Services": "services", "Compliance": "compliance", "General Availability": "general-availability", "Gallery": "gallery", "Operating System": "operating-system"}}

    def test_10_parse_drop_downlist_checkdropdownlist(self):
        '''
        ドロップダウンリストの結果が同じかどうかをテストする
        '''
        option_list = Util(TestCommon.logger).parse_drop_downlist()

        self.logger.debug(option_list)


        # ドロップダウンリストの内容が期待値と一致していることを確認する
        assert(option_list == TestCommon.dropdown_expect)

        # ファイルが保存できていることを確認する
        assert(os.path.isfile(DROPDOWNLIST_CACHE_FILE_PATH))

    def test_20_get_drop_downlist(self):
        '''保存されたドロップダウンリストの内容を取得出来ることをテストする'''
        option_list = Util(TestCommon.logger).get_drop_downlist()

        assert(option_list == TestCommon.dropdown_expect)

