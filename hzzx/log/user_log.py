import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        base_url = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_url, 'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + ".log"
        log_path = log_dir + "\\" + log_file
        self.file_handler = logging.FileHandler(log_path, 'a', encoding='utf-8')
        self.file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s ----> %(funcName)s %(levelno)s :             %(levelname)s ----> %(message)s')
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handler)
        self.file_handler.close()

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('123')
    log.info('你好')
    user.close_handle()

