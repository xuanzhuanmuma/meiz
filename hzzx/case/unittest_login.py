import HTMLTestRunner
import os
import time
import unittest

import ddt
from selenium import webdriver

from hzzx.business.loginBusiness import LoginBusiness
from hzzx.util.excelUtil import ExcelUtil
from hzzx.util.iniUtil import OperateIni

excel = ExcelUtil(os.path.dirname(os.getcwd()) + r'\config\caseData.xls')
excel.get_table_by_index(0)
data = excel.get_all_data()

@ddt.ddt
class LoginTest(unittest.TestCase):
    def setUp(self):
        url = OperateIni(os.path.dirname(os.getcwd()) + '\config\myConfig.ini').get_value('user_url', 'login_url')
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = LoginBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        # title不包含'登录',表示登录成功
        result = '登录' not in self.driver.title
        self.assertTrue(result)
        self.driver.quit()

    @ddt.data(*data)
    @ddt.unpack
    def test_login(self, username, password, expect):
        self.login.login_success(username, password)


if __name__ == '__main__':
    report = os.path.dirname(os.getcwd()) + r'\report\loginReport.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='测试报告',
            description='执行人：妍娜')
        runner.run(suite)
