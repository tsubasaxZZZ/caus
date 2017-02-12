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

        TestCommon.dropdown_expect = {"dropdown-products": {"IoT Suite": "iot-suite", "Scheduler": "scheduler", "Data Lake Analytics": "data-lake-analytics", "Azure Active Directory": "active-directory", "Azure Active Directory Domain Services": "active-directory-ds", "Recovery Services": "recovery-services", "Content Delivery Network": "cdn", "Service Fabric": "service-fabric", "Virtual Machines": "virtual-machines", "Site Recovery": "site-recovery", "Cloud Services": "cloud-services", "Security Center": "security-center", "Event Hubs": "event-hubs", "Azure DNS": "dns", "Key Vault": "key-vault", "API Management": "api-management", "DocumentDB": "documentdb", "SQL Data Warehouse": "sql-data-warehouse", "Batch": "batch", "Storage": "storage", "BizTalk Services": "biztalk-services", "Multi-Factor Authentication": "multi-factor-authentication", "Power BI Embedded": "power-bi-embedded", "Automation": "automation", "Logic Apps": "logic-apps", "Web Apps": "web-sites", "Virtual Machine Scale Sets": "virtual-machine-scale-sets", "Azure Active Directory B2C": "active-directory-b2c", "Azure Container Service": "container-service", "Access Control Service": "access-control", "SQL Database": "sql-database", "Visual Studio Team Services": "visual-studio-team-services", "Mobile Engagement": "mobile-engagement", "Redis Cache": "redis-cache", "Log Analytics": "log-analytics", "VPN Gateway": "vpn-gateway", "Backup": "backup", "IoT Hub": "iot-hub", "Mobile Services": "mobile-services", "Application Gateway": "application-gateway", "StorSimple": "storsimple", "SQL Server Stretch Database": "sql-server-stretch-database", "Media Services": "media-services", "Marketplace": "marketplace", "Managed Cache Service": "cache", "App Service": "app-service", "Notification Hubs": "notification-hubs", "Azure Search": "search", "Data Catalog": "data-catalog", "Functions": "functions", "ExpressRoute": "expressroute", "RemoteApp": "remoteapp", "Virtual Network": "virtual-network", "Data Lake Store": "data-lake-store", "Application Insights": "application-insights", "HockeyApp": "hockeyapp", "Traffic Manager": "traffic-manager", "Microsoft Azure portal": "azure-portal", "Cognitive Services": "cognitive-services", "Service Bus": "service-bus", "Azure Resource Manager": "azure-resource-manager", "Stream Analytics": "stream-analytics", "Azure DevTest Labs": "devtest-lab", "Load Balancer": "load-balancer", "HDInsight": "hdinsight", "Machine Learning": "machine-learning", "Data Factory": "data-factory", "Recovery Manager": "recovery-manager"}, "dropdown-platform": {"Xamarin": "xamarin", "Python": "python", "Media": "media", "Ruby": "ruby", "Linux cluster": "linux-cluster", "PHP": "php", "Java": "java", "Windows cluster": "windows-cluster", "PowerShell": "powershell", "Android": "android", "Node.js": "nodejs", "XPlatCLI": "x-plat-cli", "iOS": "ios", "Windows": "windows", "Rest": "rest"}, "dropdown-updatetype": {"Services": "services", "SDK and Tools": "sdk-and-tools", "Management": "management", "Pricing & Offerings": "pricing-offerings", "General Availability": "general-availability", "Regions and Datacenters": "regions-and-datacenters", "Operating System": "operating-system", "Features": "features", "Gallery": "gallery", "Compliance": "compliance", "Preview": "preview"}, "service-type": {"Application": ["API Management", "Access Control Service", "App Service", "Application Insights", "IoT Hub", "Azure Search", "Batch", "BizTalk Services", "Cloud Services", "Cognitive Services", "DocumentDB", "Event Hubs", "Functions", "HockeyApp", "IoT Suite", "Logic Apps", "Managed Cache Service", "Media Services", "Mobile Engagement", "Mobile Services", "Notification Hubs", "Power BI Embedded", "Redis Cache", "Service Bus", "Service Fabric", "Stream Analytics", "Visual Studio Team Services", "Web Apps"], "ID & Security": ["Azure Active Directory", "Azure Active Directory B2C", "Azure Active Directory Domain Services", "Multi-Factor Authentication", "Security Center"], "Platform": ["Application Gateway", "Automation", "Azure Container Service", "Azure DNS", "Azure DevTest Labs", "Azure Resource Manager", "Backup", "Content Delivery Network", "Marketplace", "ExpressRoute", "Key Vault", "Load Balancer", "Log Analytics", "Microsoft Azure portal", "Recovery Manager", "Recovery Services", "RemoteApp", "Scheduler", "Site Recovery", "StorSimple", "Storage", "Traffic Manager", "VPN Gateway", "Virtual Machines", "Virtual Machine Scale Sets", "Virtual Network"], "Data Platform": ["Data Catalog", "Data Factory", "Data Lake Analytics", "Data Lake Store", "HDInsight", "Machine Learning", "SQL Data Warehouse", "SQL Database", "SQL Server Stretch Database"]}}

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

