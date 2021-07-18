import os
import configparser

cur_path = os.path.dirname(__file__)
config_path = os.path.join(cur_path, '..\config\config.ini')


class Config:
    def __init__(self, path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path, encoding='utf-8')

    @property
    def url(self):
        url_value = self.cfg.get('default', 'URL')
        return url_value

    @property
    def driver_name(self):
        driver_name_value = self.cfg.get('default', 'driver_name')
        return driver_name_value

    @property
    def driver_path(self):
        driver_path_value = self.cfg.get('default', 'driver_path')
        return driver_path_value

    @property
    def time_out(self):
        time_out_value = float(self.cfg.get('default', 'time_out'))
        return time_out_value

    @property
    def screenshot_path(self):
        screenshot_path_value = self.cfg.get('default', 'screenshot_path')
        return screenshot_path_value

    @property
    def user_name(self):
        user_name_value = self.cfg.get('default', 'user_name')
        return user_name_value

    @property
    def password(self):
        password_value = self.cfg.get('default', 'password')
        return password_value


local_config = Config()

if __name__ == '__main__':
    print(Config().driver_path, Config().url, local_config.time_out)
