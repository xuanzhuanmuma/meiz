import os
import unittest
import HTMLTestRunner
import ddt


@ddt.ddt
class LoginTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('类的前置条件')

    @classmethod
    def tearDownClass(cls):
        print('类的后置条件')

    @ddt.data(
        ['admin', '1'],
        ['admin', '2'],
        ['admin', '3']
    )
    @ddt.unpack
    def test_login(self, username, password):
        print(username + '============' + password)


if __name__ == '__main__':
    report = os.path.dirname(os.getcwd()) + r'\report\test.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest1)
    fp = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title='测试报告',
        description='执行人：妍娜')
    runner.run(suite)
    fp.close()
