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

        TestCommon.dropdown_expect = {"dropdown-platform": {"Rest": "rest", "Linux cluster": "linux-cluster", "PHP": "php", "PowerShell": "powershell", "Windows": "windows", "Python": "python", "Media": "media", "Windows cluster": "windows-cluster", "XPlatCLI": "x-plat-cli", "Ruby": "ruby", "iOS": "ios", "Xamarin": "xamarin", "Node.js": "nodejs", "Java": "java", "Android": "android"}, "dropdown-products": {"BizTalk Services": "biztalk-services", "Traffic Manager": "traffic-manager", "Automation": "automation", "Storage": "storage", "Data Lake Store": "data-lake-store", "Content Delivery Network": "cdn", "API Management": "api-management", "StorSimple": "storsimple", "RemoteApp": "remoteapp", "Logic Apps": "logic-apps", "SQL Database": "sql-database", "Application Gateway": "application-gateway", "Azure Active Directory B2C": "active-directory-b2c", "Data Lake Analytics": "data-lake-analytics", "Microsoft Azure portal": "azure-portal", "Media Services": "media-services", "App Service": "app-service", "Azure DNS": "dns", "Virtual Network": "virtual-network", "ExpressRoute": "expressroute", "HDInsight": "hdinsight", "Scheduler": "scheduler", "Multi-Factor Authentication": "multi-factor-authentication", "HockeyApp": "hockeyapp", "SQL Server Stretch Database": "sql-server-stretch-database", "Machine Learning": "machine-learning", "Data Factory": "data-factory", "Batch": "batch", "Azure Active Directory": "active-directory", "Cognitive Services": "cognitive-services", "Log Analytics": "log-analytics", "Key Vault": "key-vault", "SQL Data Warehouse": "sql-data-warehouse", "Azure Active Directory Domain Services": "active-directory-ds", "Site Recovery": "site-recovery", "Mobile Services": "mobile-services", "Azure DevTest Labs": "devtest-lab", "Visual Studio Team Services": "visual-studio-team-services", "Azure Search": "search", "Application Insights": "application-insights", "Security Center": "security-center", "IoT Suite": "iot-suite", "Managed Cache Service": "cache", "Access Control Service": "access-control", "Service Fabric": "service-fabric", "Virtual Machines": "virtual-machines", "Virtual Machine Scale Sets": "virtual-machine-scale-sets", "Marketplace": "marketplace", "Recovery Manager": "recovery-manager", "Service Bus": "service-bus", "DocumentDB": "documentdb", "Azure Resource Manager": "azure-resource-manager", "Functions": "functions", "VPN Gateway": "vpn-gateway", "Power BI Embedded": "power-bi-embedded", "Recovery Services": "recovery-services", "Network Watcher": "network-watcher", "Cloud Services": "cloud-services", "Load Balancer": "load-balancer", "Redis Cache": "redis-cache", "Notification Hubs": "notification-hubs", "Mobile Engagement": "mobile-engagement", "Backup": "backup", "Data Catalog": "data-catalog", "Event Hubs": "event-hubs", "IoT Hub": "iot-hub", "Web Apps": "web-sites", "Azure Container Service": "container-service", "Stream Analytics": "stream-analytics", "Azure Monitor": "monitor"}, "dropdown-updatetype": {"Regions and Datacenters": "regions-and-datacenters", "Services": "services", "Management": "management", "Pricing & Offerings": "pricing-offerings", "Compliance": "compliance", "Preview": "preview", "Gallery": "gallery", "Features": "features", "General Availability": "general-availability", "SDK and Tools": "sdk-and-tools", "Operating System": "operating-system"}, "service-type": {"Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "DocumentDB", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Power BI Embedded", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services", "Web Apps"], "Data Platform": ["Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "Platform": ["Application Gateway", "Automation", "Azure Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Azure Monitor", "Backup", "Content Delivery Network", "Marketplace", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Network Watcher", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Machine Scale Sets", "Virtual Network"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"]}}

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

