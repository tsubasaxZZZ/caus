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

        TestCommon.dropdown_expect = {"service-type": {"Platform": ["Application Gateway", "Automation", "Azure Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Backup", "Content Delivery Network", "DataMarket", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure classic portal", "Microsoft Azure portal", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Network"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "DocumentDB", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Power BI Embedded", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services"], "Data Platform": ["Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"]}, "dropdown-updatetype": {"General Availability": "general-availability", "Gallery": "gallery", "Regions and Datacenters": "regions-and-datacenters", "Compliance": "compliance", "Services": "services", "Operating System": "operating-system", "SDK and Tools": "sdk-and-tools", "Features": "features", "Management": "management", "Preview": "preview", "Pricing & Offerings": "pricing-offerings"}, "dropdown-platform": {"Windows": "windows", "Linux cluster": "linux-cluster", "Media": "media", "PowerShell": "powershell", "Windows cluster": "windows-cluster", "Xamarin": "xamarin", "Java": "java", "Node.js": "nodejs", "Rest": "rest", "PHP": "php", "Python": "python", "iOS": "ios", "Ruby": "ruby", "Android": "android", "XPlatCLI": "x-plat-cli"}, "dropdown-products": {"Recovery Manager": "recovery-manager", "App Service": "app-service", "Azure Active Directory Domain Services": "active-directory-ds", "Backup": "backup", "Automation": "automation", "Azure Search": "search", "HockeyApp": "hockeyapp", "Load Balancer": "load-balancer", "Logic Apps": "logic-apps", "Batch": "batch", "DocumentDB": "documentdb", "API Management": "api-management", "Storage": "storage", "IoT Hub": "iot-hub", "HDInsight": "hdinsight", "Azure Active Directory": "active-directory", "Scheduler": "scheduler", "Key Vault": "key-vault", "StorSimple": "storsimple", "Traffic Manager": "traffic-manager", "Stream Analytics": "stream-analytics", "SQL Server Stretch Database": "sql-server-stretch-database", "Managed Cache Service": "cache", "Recovery Services": "recovery-services", "Azure DNS": "dns", "Access Control Service": "access-control", "Azure Container Service": "container-service", "Microsoft Azure classic portal": "management-portal", "Data Catalog": "data-catalog", "Service Bus": "service-bus", "Cognitive Services": "cognitive-services", "Azure DevTest Labs": "devtest-lab", "Mobile Engagement": "mobile-engagement", "SQL Database": "sql-database", "Cloud Services": "cloud-services", "IoT Suite": "iot-suite", "Microsoft Azure portal": "azure-portal", "Azure Resource Manager": "azure-resource-manager", "Virtual Machines": "virtual-machines", "SQL Data Warehouse": "sql-data-warehouse", "Virtual Network": "virtual-network", "Application Insights": "application-insights", "Data Factory": "data-factory", "RemoteApp": "remoteapp", "Multi-Factor Authentication": "multi-factor-authentication", "Event Hubs": "event-hubs", "ExpressRoute": "expressroute", "Mobile Services": "mobile-services", "Machine Learning": "machine-learning", "Content Delivery Network": "cdn", "BizTalk Services": "biztalk-services", "Azure Active Directory B2C": "active-directory-b2c", "Site Recovery": "site-recovery", "Notification Hubs": "notification-hubs", "DataMarket": "marketplace", "Functions": "functions", "Redis Cache": "redis-cache", "Service Fabric": "service-fabric", "Security Center": "security-center", "Power BI Embedded": "power-bi-embedded", "Log Analytics": "log-analytics", "Data Lake Store": "data-lake-store", "VPN Gateway": "vpn-gateway", "Media Services": "media-services", "Application Gateway": "application-gateway", "Data Lake Analytics": "data-lake-analytics", "Visual Studio Team Services": "visual-studio-team-services"}}

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

