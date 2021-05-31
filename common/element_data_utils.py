import os
import yaml

cur_path = os.path.dirname(__file__)
yaml_path = os.path.join(cur_path, '..\\elements_info_datas\\login_page.yaml')


class ElementDataUtils:
    def __init__(self, page_name='login_page'):
        self.element_path = os.path.join(cur_path, '..\\elements_info_datas\\', page_name, 'yaml')

    def get_element_info(self):
        with open(yaml_path, encoding='utf-8') as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
            return data


if __name__ == '__main__':
    elementdata = ElementDataUtils()
    print(elementdata.get_element_info())