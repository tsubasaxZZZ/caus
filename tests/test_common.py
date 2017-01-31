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

        TestCommon.dropdown_expect = {"service-type": {"ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"], "Platform": ["Application Gateway", "Automation", "Azure Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Backup", "Content Delivery Network", "Marketplace", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Network"], "Data Platform": ["Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"], "Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "DocumentDB", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Power BI Embedded", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services", "Web Apps"]}, "dropdown-platform": {"Python": "python", "iOS": "ios", "Linux cluster": "linux-cluster", "Rest": "rest", "Media": "media", "Windows": "windows", "Android": "android", "PHP": "php", "Java": "java", "Xamarin": "xamarin", "Node.js": "nodejs", "PowerShell": "powershell", "XPlatCLI": "x-plat-cli", "Windows cluster": "windows-cluster", "Ruby": "ruby"}, "dropdown-updatetype": {"Features": "features", "Gallery": "gallery", "Services": "services", "Operating System": "operating-system", "Pricing & Offerings": "pricing-offerings", "General Availability": "general-availability", "Regions and Datacenters": "regions-and-datacenters", "Management": "management", "Preview": "preview", "SDK and Tools": "sdk-and-tools", "Compliance": "compliance"}, "dropdown-products": {"Load Balancer": "load-balancer", "Recovery Manager": "recovery-manager", "RemoteApp": "remoteapp", "Virtual Network": "virtual-network", "Key Vault": "key-vault", "Service Bus": "service-bus", "SQL Server Stretch Database": "sql-server-stretch-database", "Azure Active Directory Domain Services": "active-directory-ds", "IoT Suite": "iot-suite", "API Management": "api-management", "Service Fabric": "service-fabric", "Backup": "backup", "Microsoft Azure portal": "azure-portal", "SQL Database": "sql-database", "Stream Analytics": "stream-analytics", "Automation": "automation", "Media Services": "media-services", "StorSimple": "storsimple", "Azure Resource Manager": "azure-resource-manager", "App Service": "app-service", "Event Hubs": "event-hubs", "Application Gateway": "application-gateway", "Security Center": "security-center", "Storage": "storage", "Azure Active Directory": "active-directory", "Web Apps": "web-sites", "DocumentDB": "documentdb", "Data Lake Analytics": "data-lake-analytics", "Content Delivery Network": "cdn", "Batch": "batch", "Managed Cache Service": "cache", "Azure Container Service": "container-service", "Azure Search": "search", "Mobile Services": "mobile-services", "Data Factory": "data-factory", "Azure DNS": "dns", "Functions": "functions", "Recovery Services": "recovery-services", "Data Catalog": "data-catalog", "Marketplace": "marketplace", "Redis Cache": "redis-cache", "Application Insights": "application-insights", "Scheduler": "scheduler", "Notification Hubs": "notification-hubs", "ExpressRoute": "expressroute", "Access Control Service": "access-control", "Log Analytics": "log-analytics", "Virtual Machines": "virtual-machines", "Multi-Factor Authentication": "multi-factor-authentication", "Traffic Manager": "traffic-manager", "SQL Data Warehouse": "sql-data-warehouse", "Azure DevTest Labs": "devtest-lab", "HDInsight": "hdinsight", "Cloud Services": "cloud-services", "Visual Studio Team Services": "visual-studio-team-services", "Machine Learning": "machine-learning", "Power BI Embedded": "power-bi-embedded", "IoT Hub": "iot-hub", "Cognitive Services": "cognitive-services", "Azure Active Directory B2C": "active-directory-b2c", "Logic Apps": "logic-apps", "Data Lake Store": "data-lake-store", "HockeyApp": "hockeyapp", "VPN Gateway": "vpn-gateway", "BizTalk Services": "biztalk-services", "Site Recovery": "site-recovery", "Mobile Engagement": "mobile-engagement"}}

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

