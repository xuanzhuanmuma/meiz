from hzzx.util.excelUtil import ExcelUtil
import time
import os
import unittest
import ddt
data_path = os.path.dirname(os.getcwd()) + '\config\keyWord.xls'
excel = ExcelUtil(data_path)
excel.get_table_by_index(0)
all_case = excel.get_all_data()


@ddt
class KeyWordTest(unittest.TestCase):
    def __init__(self):
        pass

    @ddt.data(all_case)
    def test_operate(self, *data):

        print(all_case)

if __name__ == '__main__':
    keywordTest = KeyWordTest()
    keywordTest.operate()