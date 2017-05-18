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

        TestCommon.dropdown_expect = {"dropdown-products": {"Backup": "backup", "Mobile Services": "mobile-services", "VPN Gateway": "vpn-gateway", "Azure DevTest Labs": "devtest-lab", "Azure Active Directory Domain Services": "active-directory-ds", "API Management": "api-management", "Virtual Machines": "virtual-machines", "Power BI Embedded": "power-bi-embedded", "BizTalk Services": "biztalk-services", "Functions": "functions", "Recovery Services": "recovery-services", "App Service": "app-service", "IoT Suite": "iot-suite", "Content Delivery Network": "cdn", "Recovery Manager": "recovery-manager", "Data Catalog": "data-catalog", "RemoteApp": "remoteapp", "Azure Search": "search", "ExpressRoute": "expressroute", "Cognitive Services": "cognitive-services", "Service Bus": "service-bus", "Azure Active Directory B2C": "active-directory-b2c", "Stream Analytics": "stream-analytics", "Application Insights": "application-insights", "Machine Learning": "machine-learning", "Notification Hubs": "notification-hubs", "SQL Server Stretch Database": "sql-server-stretch-database", "SQL Database": "sql-database", "Virtual Network": "virtual-network", "Service Fabric": "service-fabric", "StorSimple": "storsimple", "Event Hubs": "event-hubs", "Media Services": "media-services", "Marketplace": "marketplace", "Azure Active Directory": "active-directory", "Virtual Machine Scale Sets": "virtual-machine-scale-sets", "Security Center": "security-center", "Data Lake Store": "data-lake-store", "HockeyApp": "hockeyapp", "Microsoft Azure portal": "azure-portal", "Multi-Factor Authentication": "multi-factor-authentication", "Scheduler": "scheduler", "Data Factory": "data-factory", "Automation": "automation", "Azure Monitor": "monitor", "Managed Cache Service": "cache", "Storage": "storage", "Visual Studio Team Services": "visual-studio-team-services", "Key Vault": "key-vault", "Load Balancer": "load-balancer", "Container Service": "container-service", "Cloud Services": "cloud-services", "Log Analytics": "log-analytics", "Batch": "batch", "Network Watcher": "network-watcher", "SQL Data Warehouse": "sql-data-warehouse", "Azure Resource Manager": "azure-resource-manager", "Application Gateway": "application-gateway", "Azure DNS": "dns", "Access Control Service": "access-control", "Mobile Engagement": "mobile-engagement", "Web Apps": "web-sites", "Logic Apps": "logic-apps", "Azure Cosmos DB": "cosmos-db", "Redis Cache": "redis-cache", "IoT Hub": "iot-hub", "HDInsight": "hdinsight", "Site Recovery": "site-recovery", "Traffic Manager": "traffic-manager", "Data Lake Analytics": "data-lake-analytics"}, "dropdown-platform": {"Node.js": "nodejs", "Xamarin": "xamarin", "Media": "media", "Android": "android", "Windows cluster": "windows-cluster", "iOS": "ios", "Python": "python", "Rest": "rest", "Windows": "windows", "Linux cluster": "linux-cluster", "PHP": "php", "Java": "java", "Ruby": "ruby", "XPlatCLI": "x-plat-cli", "PowerShell": "powershell"}, "service-type": {"Data Platform": ["Azure Cosmos DB", "Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "Power BI Embedded", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"], "Platform": ["Application Gateway", "Automation", "Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Azure Monitor", "Backup", "Content Delivery Network", "Marketplace", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Network Watcher", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Machine Scale Sets", "Virtual Network"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services", "Web Apps"]}, "dropdown-updatetype": {"Pricing & Offerings": "pricing-offerings", "Compliance": "compliance", "General Availability": "general-availability", "SDK and Tools": "sdk-and-tools", "Operating System": "operating-system", "Preview": "preview", "Gallery": "gallery", "Services": "services", "Features": "features", "Management": "management", "Regions and Datacenters": "regions-and-datacenters"}}

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

