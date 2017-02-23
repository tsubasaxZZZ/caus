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

        TestCommon.dropdown_expect = {"dropdown-platform": {"Ruby": "ruby", "XPlatCLI": "x-plat-cli", "Node.js": "nodejs", "Java": "java", "Windows cluster": "windows-cluster", "PowerShell": "powershell", "Rest": "rest", "Media": "media", "iOS": "ios", "PHP": "php", "Android": "android", "Python": "python", "Xamarin": "xamarin", "Linux cluster": "linux-cluster", "Windows": "windows"}, "service-type": {"Data Platform": ["Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "DocumentDB", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Power BI Embedded", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services", "Web Apps"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"], "Platform": ["Application Gateway", "Automation", "Azure Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Backup", "Content Delivery Network", "Marketplace", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Network Watcher", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Machine Scale Sets", "Virtual Network"]}, "dropdown-updatetype": {"Preview": "preview", "Regions and Datacenters": "regions-and-datacenters", "Operating System": "operating-system", "Management": "management", "General Availability": "general-availability", "Services": "services", "SDK and Tools": "sdk-and-tools", "Features": "features", "Gallery": "gallery", "Pricing & Offerings": "pricing-offerings", "Compliance": "compliance"}, "dropdown-products": {"Azure Resource Manager": "azure-resource-manager", "Functions": "functions", "Virtual Machine Scale Sets": "virtual-machine-scale-sets", "Azure DevTest Labs": "devtest-lab", "VPN Gateway": "vpn-gateway", "Batch": "batch", "Key Vault": "key-vault", "Backup": "backup", "Virtual Network": "virtual-network", "Load Balancer": "load-balancer", "Marketplace": "marketplace", "DocumentDB": "documentdb", "Recovery Manager": "recovery-manager", "Automation": "automation", "SQL Data Warehouse": "sql-data-warehouse", "BizTalk Services": "biztalk-services", "Azure Active Directory Domain Services": "active-directory-ds", "Redis Cache": "redis-cache", "Azure Container Service": "container-service", "Access Control Service": "access-control", "Microsoft Azure portal": "azure-portal", "Service Bus": "service-bus", "Application Insights": "application-insights", "Visual Studio Team Services": "visual-studio-team-services", "App Service": "app-service", "Logic Apps": "logic-apps", "Data Lake Store": "data-lake-store", "Managed Cache Service": "cache", "Notification Hubs": "notification-hubs", "StorSimple": "storsimple", "Content Delivery Network": "cdn", "Web Apps": "web-sites", "Scheduler": "scheduler", "Event Hubs": "event-hubs", "IoT Hub": "iot-hub", "Media Services": "media-services", "Site Recovery": "site-recovery", "HockeyApp": "hockeyapp", "Network Watcher": "network-watcher", "Mobile Services": "mobile-services", "Storage": "storage", "ExpressRoute": "expressroute", "Data Catalog": "data-catalog", "SQL Database": "sql-database", "RemoteApp": "remoteapp", "Security Center": "security-center", "IoT Suite": "iot-suite", "Cloud Services": "cloud-services", "Cognitive Services": "cognitive-services", "Log Analytics": "log-analytics", "Azure Active Directory": "active-directory", "Azure DNS": "dns", "Application Gateway": "application-gateway", "Data Factory": "data-factory", "Traffic Manager": "traffic-manager", "Service Fabric": "service-fabric", "Azure Search": "search", "Virtual Machines": "virtual-machines", "HDInsight": "hdinsight", "Multi-Factor Authentication": "multi-factor-authentication", "SQL Server Stretch Database": "sql-server-stretch-database", "Power BI Embedded": "power-bi-embedded", "Stream Analytics": "stream-analytics", "Mobile Engagement": "mobile-engagement", "API Management": "api-management", "Azure Active Directory B2C": "active-directory-b2c", "Data Lake Analytics": "data-lake-analytics", "Machine Learning": "machine-learning", "Recovery Services": "recovery-services"}}

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

