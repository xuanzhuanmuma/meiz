import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from hzzx.base.findElement import FindElement


class SeleniumDriver(object):
    def __init__(self):
        self.driver = self.open_browser()

    def open_browser(self, browser='chrome'):
        try:
            if browser == 'chrome':
                driver = webdriver.Chrome()
            elif browser == 'firefox':
                driver = webdriver.Firefox()
            elif browser == 'ie':
                driver = webdriver.Ie()
            else:
                driver = webdriver.Edge()
            time.sleep(1)
            return driver
        except:
            print('open browser fail!')
            return None

    def get_url(self, url):
        if self.driver is not None:
            self.driver.maximize_window()
            if 'http://' in url and 'https://' in url:
                self.driver.get(url)
            else:
                print('你的url有误，请检查')
        else:
            print('获取浏览器失败')

    def close_browser(self):
        self.driver.close()

    def quit_browser(self):
        self.driver.quit()

    def handle_window(self, *args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'forward':
                self.driver.forward()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'refresh':
                self.driver.refresh()
            else:
                print('没有该操作')
        elif value == 2:
            self.driver.get_window_size(args[0], args[1])
        else:
            print('参数有问题，请重新上传')


    def assert_title(self, title_name=None):
        '''判断title是否正确'''
        if title_name is not None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def open_url_is_true(self, url, title_name=None):
        self.get_url(url)
        return self.assert_title(title_name)

    def switch_window(self, title_name=None):
        '''切换windows'''
        handle_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in handle_list:
            if i is not current_handle:
                time.sleep(2)
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break
        time.sleep(2)

    def element_is_display(self, element):
        return element.is_displayed()

    def element_is_selected(self, element):
        return element.is_selected()

    def element_is_enabled(self, element):
        return element.is_enabled()

    def get_element(self, file_path, node, key):
        find_element = FindElement(file_path, self.driver)
        return find_element.get_element(node, key)

    def send_value(self, file_path, node, key, value):
        element = self.get_element(file_path, node, key)
        if element is not None:
            if self.element_is_display(element):
                element.send_keys(value)
            else:
                print('输入失败，定位元素不可编辑')
        else:
            print('输入失败，定位元素没有找到')

    def click_element(self, file_path, node, key):
        element = self.get_element(file_path, node, key)
        if element is not None:
            if self.element_is_display(element):
                element.click()
            else:
                print('点击失败，元素不可见')
        else:
            print('点击失败，定位元素没有找到')
