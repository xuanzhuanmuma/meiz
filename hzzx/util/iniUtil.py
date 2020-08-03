import configparser


class OperateIni(object):
    def __init__(self, file_path):
        if file_path is None:
            file_path = ''
        self.cf = self.load_ini(file_path)

    def load_ini(self, file_path):
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8")
        return cf

    # 获取所有的section节点
    def get_all_section(self):
        return self.cf.sections()

    # 获取指定section的options
    def get_all_options(self, node):
        return self.cf.options(node)

    # 获取指定section的所有配置信息
    def get_all_key_value(self, node):
        return self.cf.items(node)

    # 获取指定section指定option值
    def get_value(self, node, key):
        return self.cf.get(node, key)

    # 修改某个option的值，如果不存在就创建
    def update_value(self, file_path, node, key, value):
        self.cf.set(node, key, value)
        self.write_ini(file_path)

    # 检查section或option是否存在
    def has_section(self, node):
        return self.cf.has_section(node)

    def has_option(self, node, key):
        return self.has_option(node, key)

    # 添加session和option
    def add_section(self, file_path, node):
        if not self.cf.has_section(node):
            self.cf.add_section(node)
            self.write_ini(file_path)

    def add_option(self, file_path, node, key, value):
        if not self.cf.has_option(node, key):
            self.cf.set(node, key, value)
            self.write_ini(file_path)

    # 删除section或者option
    def del_section(self, node):
        self.cf.remove_section(node)

    def del_optinon(self, node, key):
        self.cf.remove_option(node, key)

    def write_ini(self, file_path):
        self.cf.write(open(file_path, 'w'))

