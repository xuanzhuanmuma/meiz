import unittest
import os
import HTMLTestRunner

def allTests():
    case_path = os.path.dirname(__file__)
    suite = unittest.defaultTestLoader.discover(
        start_dir=case_path,
        pattern='unittest_*.py',
        top_level_dir=None
    )
    return suite

def run():
    fp = os.path.dirname(os.getcwd()) + r'\report\loginReport.html'
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=open(fp, 'wb'),
        title='自动化测试报告',
        description='执行人：妍娜'
    )
    runner.run(allTests())

if __name__ == '__main__':
    run()
