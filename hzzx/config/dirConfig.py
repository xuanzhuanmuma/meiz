import os


# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__)))[0][0]

testdatas_dir = os.path.join(base_dir, 'case')

htmlreport_dir = os.path.join(base_dir, 'report')

config_dir = os.path.join(base_dir, 'config')

util_dir = os.path.join(base_dir, 'util')

