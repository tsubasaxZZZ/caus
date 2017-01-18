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

        TestCommon.dropdown_expect = {"dropdown-platform": {"Android": "android", "Windows cluster": "windows-cluster", "XPlatCLI": "x-plat-cli", "Windows": "windows", "Ruby": "ruby", "PowerShell": "powershell", "Rest": "rest", "PHP": "php", "Node.js": "nodejs", "Java": "java", "Linux cluster": "linux-cluster", "Python": "python", "Xamarin": "xamarin", "iOS": "ios", "Media": "media"}, "dropdown-products": {"RemoteApp": "remoteapp", "Data Catalog": "data-catalog", "Azure DNS": "dns", "API Management": "api-management", "HockeyApp": "hockeyapp", "SQL Database": "sql-database", "App Service": "app-service", "Mobile Engagement": "mobile-engagement", "Azure Active Directory Domain Services": "active-directory-ds", "Service Bus": "service-bus", "Data Lake Store": "data-lake-store", "DocumentDB": "documentdb", "DataMarket": "marketplace", "Load Balancer": "load-balancer", "Media Services": "media-services", "Azure Active Directory": "active-directory", "Recovery Manager": "recovery-manager", "SQL Data Warehouse": "sql-data-warehouse", "StorSimple": "storsimple", "HDInsight": "hdinsight", "Machine Learning": "machine-learning", "Application Insights": "application-insights", "Key Vault": "key-vault", "Functions": "functions", "Power BI Embedded": "power-bi-embedded", "Security Center": "security-center", "Managed Cache Service": "cache", "Log Analytics": "log-analytics", "Microsoft Azure portal": "azure-portal", "Microsoft Azure classic portal": "management-portal", "Azure Search": "search", "Redis Cache": "redis-cache", "Application Gateway": "application-gateway", "Multi-Factor Authentication": "multi-factor-authentication", "Automation": "automation", "Content Delivery Network": "cdn", "VPN Gateway": "vpn-gateway", "Azure IoT Hub": "iot-hub", "Site Recovery": "site-recovery", "IoT Suite": "iot-suite", "Virtual Network": "virtual-network", "Azure DevTest Labs": "devtest-lab", "Cloud Services": "cloud-services", "Stream Analytics": "stream-analytics", "Service Fabric": "service-fabric", "Virtual Machines": "virtual-machines", "Logic Apps": "logic-apps", "Cognitive Services": "cognitive-services", "Azure Resource Manager": "azure-resource-manager", "Access Control Service": "access-control", "Backup": "backup", "Batch": "batch", "Event Hubs": "event-hubs", "ExpressRoute": "expressroute", "Azure Active Directory B2C": "active-directory-b2c", "BizTalk Services": "biztalk-services", "Data Factory": "data-factory", "Visual Studio Team Services": "visual-studio-team-services", "Recovery Services": "recovery-services", "Traffic Manager": "traffic-manager", "Azure Container Service": "container-service", "Notification Hubs": "notification-hubs", "Storage": "storage", "Mobile Services": "mobile-services", "SQL Server Stretch Database": "sql-server-stretch-database", "Data Lake Analytics": "data-lake-analytics", "Scheduler": "scheduler"}, "dropdown-updatetype": {"Regions and Datacenters": "regions-and-datacenters", "Services": "services", "Compliance": "compliance", "Management": "management", "Features": "features", "Pricing & Offerings": "pricing-offerings", "SDK and Tools": "sdk-and-tools", "Operating System": "operating-system", "Gallery": "gallery", "General Availability": "general-availability", "Preview": "preview"}, "service-type": {"ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"], "Data Insights": ["Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "Platform": ["Application Gateway", "Automation", "Azure Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Backup", "Content Delivery Network", "DataMarket", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Network"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "Azure IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "DocumentDB", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Power BI Embedded", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services"]}}


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

