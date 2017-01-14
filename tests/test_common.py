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

        TestCommon.dropdown_expect = {"dropdown-updatetype": {"Gallery": "gallery", "Regions and Datacenters": "regions-and-datacenters", "General Availability": "general-availability", "Operating System": "operating-system", "Pricing & Offerings": "pricing-offerings", "Preview": "preview", "Features": "features", "Compliance": "compliance", "Services": "services", "SDK and Tools": "sdk-and-tools", "Management": "management"}, "dropdown-platform": {"Node.js": "nodejs", "Android": "android", "Linux cluster": "linux-cluster", "XPlatCLI": "x-plat-cli", "Java": "java", "iOS": "ios", "PHP": "php", "PowerShell": "powershell", "Rest": "rest", "Python": "python", "Ruby": "ruby", "Windows": "windows", "Xamarin": "xamarin", "Windows cluster": "windows-cluster", "Media": "media"}, "service-type": {"Data Insights": ["Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "Azure IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "DocumentDB", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Power BI Embedded", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services"], "Platform": ["Application Gateway", "Automation", "Azure Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Backup", "Content Delivery Network", "DataMarket", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Network"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"]}, "dropdown-products": {"Azure Active Directory B2C": "active-directory-b2c", "Machine Learning": "machine-learning", "Managed Cache Service": "cache", "Key Vault": "key-vault", "Redis Cache": "redis-cache", "Scheduler": "scheduler", "Azure Active Directory Domain Services": "active-directory-ds", "Azure Search": "search", "Azure IoT Hub": "iot-hub", "Data Lake Store": "data-lake-store", "Virtual Network": "virtual-network", "DocumentDB": "documentdb", "Recovery Manager": "recovery-manager", "Service Fabric": "service-fabric", "Azure Active Directory": "active-directory", "IoT Suite": "iot-suite", "SQL Database": "sql-database", "RemoteApp": "remoteapp", "Automation": "automation", "Content Delivery Network": "cdn", "VPN Gateway": "vpn-gateway", "Functions": "functions", "Mobile Services": "mobile-services", "Cognitive Services": "cognitive-services", "StorSimple": "storsimple", "Mobile Engagement": "mobile-engagement", "Virtual Machines": "virtual-machines", "Logic Apps": "logic-apps", "Microsoft Azure portal": "azure-portal", "Recovery Services": "recovery-services", "Azure DevTest Labs": "devtest-lab", "Batch": "batch", "Load Balancer": "load-balancer", "Media Services": "media-services", "Log Analytics": "log-analytics", "Azure DNS": "dns", "BizTalk Services": "biztalk-services", "SQL Data Warehouse": "sql-data-warehouse", "Access Control Service": "access-control", "API Management": "api-management", "Site Recovery": "site-recovery", "Security Center": "security-center", "Data Catalog": "data-catalog", "HDInsight": "hdinsight", "Data Factory": "data-factory", "Backup": "backup", "Notification Hubs": "notification-hubs", "SQL Server Stretch Database": "sql-server-stretch-database", "Stream Analytics": "stream-analytics", "Traffic Manager": "traffic-manager", "App Service": "app-service", "Multi-Factor Authentication": "multi-factor-authentication", "Azure Container Service": "container-service", "Service Bus": "service-bus", "ExpressRoute": "expressroute", "Application Insights": "application-insights", "Visual Studio Team Services": "visual-studio-team-services", "Azure Resource Manager": "azure-resource-manager", "Power BI Embedded": "power-bi-embedded", "Data Lake Analytics": "data-lake-analytics", "Cloud Services": "cloud-services", "Storage": "storage", "Event Hubs": "event-hubs", "HockeyApp": "hockeyapp", "DataMarket": "marketplace", "Application Gateway": "application-gateway"}}



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

