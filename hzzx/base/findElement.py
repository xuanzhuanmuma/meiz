from hzzx.util.iniUtil import OperateIni


class FindElement(object):
    def __init__(self, file_path, driver):
        self.file_path = file_path
        self.driver = driver

    def get_element(self, node, key):
        ini_ = OperateIni(self.file_path)
        data = ini_.get_value(node, key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'class_name':
                return self.driver.find_element_by_class_name(value)
            elif by == 'tag_name':
                return self.driver.find_element_by_tag_name(value)
            elif by == 'link_text':
                return self.driver.find_element_by_link_text(value)
            elif by == 'partial_link_text':
                return self.driver.find_element_by_partial_link_text(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value)
            else:
                return None
        except:
            return None

    def get_elements(self, node, key):
        ini_ = OperateIni(self.file_path)
        data = ini_.get_value(node, key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_elements_by_id(value)
            elif by == 'name':
                return self.driver.find_elements_by_name(value)
            elif by == 'class_name':
                return self.driver.find_elements_by_class_name(value)
            elif by == 'tag_name':
                return self.driver.find_elements_by_tag_name(value)
            elif by == 'link_text':
                return self.driver.find_elements_by_link_text(value)
            elif by == 'partial_link_text':
                return self.driver.find_elements_by_partial_link_text(value)
            elif by == 'xpath':
                return self.driver.find_elements_by_xpath(value)
            elif by == 'css':
                return self.driver.find_elements_by_css_selector(value)
            else:
                return None
        except:
            return None





