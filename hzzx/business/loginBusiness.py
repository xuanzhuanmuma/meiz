from hzzx.handler.loginHandle import LoginHandle


class LoginBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_handler = LoginHandle(driver)

    def user_base(self, username, password):
        self.login_handler.send_user_name(username)
        self.login_handler.send_password(password)
        self.login_handler.click_login_button()

    def login_success(self, username, password):
        self.user_base(username, password)




