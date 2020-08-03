from hzzx.page.loginPage import LoginPage


class LoginHandle(object):
    def __init__(self, driver):
        self.login_p = LoginPage(driver)

    def send_user_name(self, username):
        self.login_p.get_username_element().send_keys(username)

    def send_password(self, password):
        self.login_p.get_password_element().send_keys(password)

    def click_login_button(self):
        self.login_p.get_login_btn_element().click()

    def is_display_button(self):
        self.login_p.get_login_btn_element().is_displayed()