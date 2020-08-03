from hzzx.business.changePasswordBusiness import ChangePasswordBussiness
from selenium import webdriver
import unittest
import ddt
import time
import os
from hzzx.util.excelUtil import ExcelUtil
excel = ExcelUtil(os.path.dirname(os.getcwd()) + r'\config\caseData.xls')
excel.get_table_by_index(1)
data = excel.get_all_data()


@ddt.ddt
class ChangePasswordTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.1.13:9001/login')
        self.driver.maximize_window()
        time.sleep(2)
        self.change_password_business = ChangePasswordBussiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    @data.data(*data)
    def test_change_password(self, *data):
        old_password, new_password, confirm_password, expect_ruslut, result = data
        self.change_password_business.change_password( old_password, new_password, confirm_password)




