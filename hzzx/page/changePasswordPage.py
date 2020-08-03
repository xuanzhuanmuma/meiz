from hzzx.base.findElement import FindElement
import os

class ChangePasswordPager(object):
    def __init__(self, file_path, driver):
        file_path = os.path.dirname(os.getcwd()) + r'\config\elements.ini'
        self.current_element = FindElement(file_path, driver)

    def get_old_password_element(self):
        return self.current_element.get_element('ChangePassword', 'old_password')

    def get_new_password_element(self):
        return self.current_element.get_element('ChangePassword', 'new_password')

    def get_confirm_password_emlement(self):
        return self.current_element.get_element('ChangePassword', 'confirm_password')

    def get_save_btn(self):
        return self.current_element.get_element('ChangePassword', 'change_password_btn')
