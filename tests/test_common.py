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

        TestCommon.dropdown_expect = {'dropdown-updatetype': {'Gallery': 'gallery', 'Pricing & Offerings': 'pricing-offerings', 'Management': 'management', 'Services': 'services', 'Operating System': 'operating-system', 'Compliance': 'compliance', 'Preview': 'preview', 'Features': 'features', 'Regions and Datacenters': 'regions-and-datacenters', 'SDK and Tools': 'sdk-and-tools', 'General Availability': 'general-availability'}, 'service-type': {'Microsoft Azure portal': 'IaaS', 'Machine Learning': 'Data Insights', 'Redis Cache': 'PaaS', 'Storage': 'IaaS', 'Mobile Services': 'PaaS', 'Data Lake Analytics': 'Data Insights', 'Functions': 'PaaS', 'Data Factory': 'Data Insights', 'SQL Server Stretch Database': 'Data Insights', 'Virtual Network': 'IaaS', 'Application Gateway': 'IaaS', 'Security Center': 'ID & Security', 'HDInsight': 'Data Insights', 'VPN Gateway': 'IaaS', 'HockeyApp': 'PaaS', 'ExpressRoute': 'IaaS', 'Multi-Factor Authentication': 'ID & Security', 'Scheduler': 'IaaS', 'Virtual Machines': 'IaaS', 'Power BI Embedded': 'PaaS', 'Cognitive Services': 'PaaS', 'Application Insights': 'PaaS', 'Key Vault': 'IaaS', 'Automation': 'IaaS', 'Azure Active Directory': 'ID & Security', 'Managed Cache Service': 'PaaS', 'Content Delivery Network': 'IaaS', 'Azure Search': 'PaaS', 'Cloud Services': 'PaaS', 'Service Fabric': 'PaaS', 'Azure Container Service': 'IaaS', 'SQL Database': 'Data Insights', 'Azure Active Directory Domain Services': 'ID & Security', 'Azure DNS': 'IaaS', 'App Service': 'PaaS', 'IoT Suite': 'PaaS', 'Stream Analytics': 'PaaS', 'Azure Resource Manager': 'IaaS', 'Site Recovery': 'IaaS', 'Traffic Manager': 'IaaS', 'SQL Data Warehouse': 'Data Insights', 'Recovery Manager': 'IaaS', 'Load Balancer': 'IaaS', 'Azure IoT Hub': 'PaaS', 'Mobile Engagement': 'PaaS', 'Visual Studio Team Services': 'PaaS', 'DocumentDB': 'PaaS', 'Logic Apps': 'PaaS', 'Access Control Service': 'PaaS', 'Event Hubs': 'PaaS', 'Backup': 'IaaS', 'API Management': 'PaaS', 'Data Catalog': 'Data Insights', 'Media Services': 'PaaS', 'Data Lake Store': 'Data Insights', 'Recovery Services': 'IaaS', 'Azure Active Directory B2C': 'ID & Security', 'BizTalk Services': 'PaaS', 'StorSimple': 'IaaS', 'Log Analytics': 'IaaS', 'DataMarket': 'IaaS', 'Service Bus': 'PaaS', 'RemoteApp': 'IaaS', 'Notification Hubs': 'PaaS', 'Azure DevTest Labs': 'IaaS', 'Batch': 'PaaS'}, 'dropdown-products': {'Microsoft Azure portal': 'azure-portal', 'Machine Learning': 'machine-learning', 'Redis Cache': 'redis-cache', 'Storage': 'storage', 'Mobile Services': 'mobile-services', 'Managed Cache Service': 'cache', 'Functions': 'functions', 'Data Factory': 'data-factory', 'SQL Server Stretch Database': 'sql-server-stretch-database', 'Virtual Network': 'virtual-network', 'Application Gateway': 'application-gateway', 'Security Center': 'security-center', 'HDInsight': 'hdinsight', 'VPN Gateway': 'vpn-gateway', 'HockeyApp': 'hockeyapp', 'Azure Active Directory B2C': 'active-directory-b2c', 'Multi-Factor Authentication': 'multi-factor-authentication', 'Scheduler': 'scheduler', 'Virtual Machines': 'virtual-machines', 'Power BI Embedded': 'power-bi-embedded', 'BizTalk Services': 'biztalk-services', 'Application Insights': 'application-insights', 'Key Vault': 'key-vault', 'Automation': 'automation', 'Azure Active Directory': 'active-directory', 'Data Lake Analytics': 'data-lake-analytics', 'Content Delivery Network': 'cdn', 'Logic Apps': 'logic-apps', 'Cloud Services': 'cloud-services', 'Service Fabric': 'service-fabric', 'Azure Container Service': 'container-service', 'SQL Database': 'sql-database', 'Azure Active Directory Domain Services': 'active-directory-ds', 'Azure DNS': 'dns', 'Azure DevTest Labs': 'devtest-lab', 'App Service': 'app-service', 'IoT Suite': 'iot-suite', 'Stream Analytics': 'stream-analytics', 'Azure Resource Manager': 'azure-resource-manager', 'Site Recovery': 'site-recovery', 'Traffic Manager': 'traffic-manager', 'SQL Data Warehouse': 'sql-data-warehouse', 'Recovery Manager': 'recovery-manager', 'Load Balancer': 'load-balancer', 'Azure IoT Hub': 'iot-hub', 'Mobile Engagement': 'mobile-engagement', 'Visual Studio Team Services': 'visual-studio-team-services', 'DocumentDB': 'documentdb', 'Azure Search': 'search', 'Access Control Service': 'access-control', 'Backup': 'backup', 'API Management': 'api-management', 'Data Catalog': 'data-catalog', 'Media Services': 'media-services', 'Data Lake Store': 'data-lake-store', 'Recovery Services': 'recovery-services', 'ExpressRoute': 'expressroute', 'Cognitive Services': 'cognitive-services', 'StorSimple': 'storsimple', 'Log Analytics': 'log-analytics', 'DataMarket': 'marketplace', 'Service Bus': 'service-bus', 'RemoteApp': 'remoteapp', 'Notification Hubs': 'notification-hubs', 'Event Hubs': 'event-hubs', 'Batch': 'batch'}, 'dropdown-platform': {'Java': 'java', 'Python': 'python', 'Windows': 'windows', 'Android': 'android', 'Ruby': 'ruby', 'Rest': 'rest', 'Windows cluster': 'windows-cluster', 'Node.js': 'nodejs', 'Media': 'media', 'Linux cluster': 'linux-cluster', 'PowerShell': 'powershell', 'Xamarin': 'xamarin', 'PHP': 'php', 'iOS': 'ios', 'XPlatCLI': 'x-plat-cli'}}


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

