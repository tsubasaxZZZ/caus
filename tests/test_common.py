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

        TestCommon.dropdown_expect = {"dropdown-updatetype": {"Compliance": "compliance", "General Availability": "general-availability", "Operating System": "operating-system", "Management": "management", "Pricing & Offerings": "pricing-offerings", "Preview": "preview", "Regions and Datacenters": "regions-and-datacenters", "Features": "features", "Services": "services", "SDK and Tools": "sdk-and-tools", "Gallery": "gallery"}, "dropdown-platform": {"Windows": "windows", "Node.js": "nodejs", "Android": "android", "Windows cluster": "windows-cluster", "XPlatCLI": "x-plat-cli", "Xamarin": "xamarin", "Java": "java", "Rest": "rest", "Ruby": "ruby", "Linux cluster": "linux-cluster", "iOS": "ios", "PowerShell": "powershell", "Media": "media", "Python": "python", "PHP": "php"}, "dropdown-products": {"SQL Server Stretch Database": "sql-server-stretch-database", "Scheduler": "scheduler", "Azure Monitor": "monitor", "Network Watcher": "network-watcher", "Mobile Services": "mobile-services", "Virtual Machine Scale Sets": "virtual-machine-scale-sets", "Power BI Embedded": "power-bi-embedded", "Automation": "automation", "Log Analytics": "log-analytics", "HDInsight": "hdinsight", "RemoteApp": "remoteapp", "HockeyApp": "hockeyapp", "Application Gateway": "application-gateway", "Content Delivery Network (CDN)": "cdn", "Recovery Manager": "recovery-manager", "Azure Search": "search", "Virtual Network": "virtual-network", "Event Hubs": "event-hubs", "Azure Active Directory": "active-directory", "Data Catalog": "data-catalog", "Stream Analytics": "stream-analytics", "VPN Gateway": "vpn-gateway", "Multi-Factor Authentication": "multi-factor-authentication", "Application Insights": "application-insights", "Access Control Service": "access-control", "Security Center": "security-center", "API Management": "api-management", "Traffic Manager": "traffic-manager", "Machine Learning": "machine-learning", "StorSimple": "storsimple", "Notification Hubs": "notification-hubs", "Web Apps": "web-sites", "Logic Apps": "logic-apps", "Container Service": "container-service", "BizTalk Services": "biztalk-services", "Azure DNS": "dns", "Media Services": "media-services", "Mobile Engagement": "mobile-engagement", "App Service": "app-service", "ExpressRoute": "expressroute", "Site Recovery": "site-recovery", "Azure Active Directory B2C": "active-directory-b2c", "Virtual Machines": "virtual-machines", "SQL Data Warehouse": "sql-data-warehouse", "Azure Cosmos DB": "cosmos-db", "Cognitive Services": "cognitive-services", "Backup": "backup", "Service Bus": "service-bus", "Redis Cache": "redis-cache", "Azure DevTest Labs": "devtest-lab", "IoT Suite": "iot-suite", "Key Vault": "key-vault", "Visual Studio Team Services": "visual-studio-team-services", "Azure Active Directory Domain Services": "active-directory-ds", "Microsoft Azure portal": "azure-portal", "Load Balancer": "load-balancer", "Data Lake Store": "data-lake-store", "Storage": "storage", "IoT Hub": "iot-hub", "Data Lake Analytics": "data-lake-analytics", "Data Factory": "data-factory", "Marketplace": "marketplace", "Cloud Services": "cloud-services", "Functions": "functions", "Recovery Services": "recovery-services", "SQL Database": "sql-database", "Managed Cache Service": "cache", "Service Fabric": "service-fabric", "Azure Resource Manager": "azure-resource-manager", "Batch": "batch"}, "service-type": {"Data Platform": ["Azure Cosmos DB", "Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "Power BI Embedded", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"], "Platform": ["Application Gateway", "Automation", "Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Azure Monitor", "Backup", "Content Delivery Network (CDN)", "Marketplace", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Network Watcher", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Machine Scale Sets", "Virtual Network"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services", "Web Apps"]}}

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

