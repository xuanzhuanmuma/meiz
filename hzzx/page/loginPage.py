from hzzx.base.findElement import FindElement


class LoginPage(object):
    def __init__(self, file_path, driver):
        self.current_element = FindElement(file_path, driver)

    def get_username_element(self):
        return self.current_element.get_element('LoginElement', 'username')

    def get_password_element(self):
        return self.current_element.get_element('LoginElement', 'password')

    def get_login_btn_element(self):
        return self.current_element.get_element('LoginElement', 'login')


