import os
import yaml
from common.config_utils import local_config
cur_path = os.path.dirname(__file__)
yaml_path = os.path.join(cur_path, '..\\elements_info_datas\\login_page.yaml')


class ElementDataUtils:
    def __init__(self, page_name='login_page'):
        self.element_path = os.path.join(cur_path, '..\\elements_info_datas\\', page_name, 'yaml')

    def get_element_info(self, locator_page='login_page'):
        with open(yaml_path, encoding='utf-8') as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
            element_data = {}
            for i, j in data.items():    # 取出字典里的键值对，存入新的字典
                if j['locator_page'] == locator_page:
                    # timeout字段必须是浮点型
                    j['time_out'] = j['time_out'] if isinstance(j['time_out'], float) else local_config.time_out
                    element_data[i] = j
        return element_data


if __name__ == '__main__':
    elementdata = ElementDataUtils()
    elementdata.get_element_info()