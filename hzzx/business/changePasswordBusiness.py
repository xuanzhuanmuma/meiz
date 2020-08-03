from hzzx.handler.changePasswordHandle import ChangePasswordHandle

class ChangePasswordBussiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.changee_password_handle = ChangePasswordHandle(driver)

    def change_password(self, old_password, new_password, confirm_password):
        self.changee_password_handle.send_old_password(old_password)
        self.changee_password_handle.send_new_password(new_password)
        self.changee_password_handle.send_confirm_password(confirm_password)
        self.changee_password_handle.click_save_btn()
