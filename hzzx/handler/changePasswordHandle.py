from hzzx.page.changePasswordPage import ChangePasswordPager
import os


class ChangePasswordHandle(object):
    def __init__(self, driver):
        self.change_password_p = ChangePasswordPager(driver)

    def send_old_password(self, old_password):
        self.change_password_p.get_old_password_element().send_keys(old_password)

    def send_new_password(self, new_password):
        self.change_password_p.get_new_password_element().send_keys(new_password)

    def send_confirm_password(self, confirm_password):
        self.change_password_p.get_confirm_password_emlement().send_keys(confirm_password)

    def click_save_btn(self):
        self.change_password_p.get_save_btn().click()

