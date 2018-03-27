# coding=utf-8
from handle.home_handle import HomeHandle


class HomeBusiness:

    def __init__(self, i):
        self.home_handle = HomeHandle(i)

    def dialog_pass(self):
        """
        关闭红包
        """
        self.home_handle.click_dialog()
