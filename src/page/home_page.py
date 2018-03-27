# coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal


class HomePage:

    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def get_dialog_element(self):
        """
        获取弹出框元素信息
        """
        return self.get_by_local.get_element('dialog', 'home_element')
