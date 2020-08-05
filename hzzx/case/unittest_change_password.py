import HTMLTestRunner
import os
import time
import unittest

import ddt
from selenium import webdriver

from hzzx.business.changePasswordBusiness import ChangePasswordBussiness
from hzzx.business.loginBusiness import LoginBusiness
from hzzx.util.excelUtil import ExcelUtil
from hzzx.util.iniUtil import OperateIni

excel = ExcelUtil(os.path.dirname(os.getcwd()) + r'\config\caseData.xls')
excel.get_table_by_index(1)
all_data = excel.get_all_data()
print(all_data)

@ddt.ddt
class ChangePasswordTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ini = OperateIni(os.path.dirname(os.getcwd()) + '\config\myConfig.ini')
        login_url = ini.get_value('user_url', 'login_url')
        cls.password_url = ini.get_value('user_url', 'change_password_url')

        cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        cls.driver.maximize_window()
        time.sleep(2)
        cls.login = LoginBusiness(cls.driver)
        cls.change_password_business = ChangePasswordBussiness(cls.driver)

        cls.login.login_success('admin', '1')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

    def tearDown(self):
        # tip = self.change_password_business.get_tip_message()
        # self.assertTrue('成功' in tip)
        pass

    @ddt.data(*all_data)
    @ddt.unpack
    def test_change_password(self, old_password, new_password, confirm_password, expect_ruslut):
        self.driver.get(self.password_url)
        self.change_password_business.change_password(old_password, new_password, confirm_password)

if __name__ == '__main__':
    report = os.path.dirname(os.getcwd()) + r'\report\changePasswordReport.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(ChangePasswordTest)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='测试报告',
            description='执行人：妍娜')
        runner.run(suite)





