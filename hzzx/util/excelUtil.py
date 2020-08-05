import xlrd
import os
import traceback
from datetime import datetime
from xlrd import xldate_as_tuple

class ExcelUtil:
    def __init__(self, file_path):
        try:
            self.book = xlrd.open_workbook(file_path)
        except Exception:
            print(traceback.print_exc())
            print('路径有误')

    # 通过索引顺去获取一个工作表
    def get_table_by_index(self, index=None):
        if index is None:
            index = 0
        self.table = self.book.sheets()[index]
        # self.table = self.book.sheet_by_index(index)
        # 通过索引顺去获取一个工作表

    # 通过名称获取一个工作表
    def get_table_by_name(self, table_name):
        self.table = self.book.sheet_by_name(table_name)

    # 返回book中所有工作表的名字
    def get_all_table(self):
        self.book.sheet_names()

    # 获取sheets中的有效行数
    def get_row_num(self):
        rows = self.table.nrows
        if rows >= 1:
            return self.table.nrows
        return None

    # 获取sheets中的有效列数
    def get_col_num(self):
        cols = self.table.ncols
        if cols >= 1:
            return self.table.ncols
        return None

    def get_all_data(self):
        result = []
        if self.get_row_num() is not None and self.get_col_num() is not None:
            for i in range(1, self.table.nrows):
                row_contet = []
                for j in range(self.table.ncols):
                    # 表格数据类型
                    ctype = self.table.cell(i, j).ctype
                    cell = self.table.cell_value(i, j)
                    # 整形
                    if ctype == 2 and cell % 1 == 0:
                        cell = int(cell)
                    elif ctype == 3:
                        time = datetime(*xldate_as_tuple(cell, 0))
                        cell = time.strftime('%Y/%d/%m %H:%M:%S')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    row_contet.append(cell)
                result.append(row_contet)
        return result

if __name__ == '__main__':
    file_path = os.path.dirname(os.getcwd()) + r'\config\keyWord.xls'
    excel = ExcelUtil(file_path)
    excel.get_table_by_index(0)
    print(excel.get_all_data())
