# coding=utf-8
from page.home_page import HomePage


class HomeHandle:

    def __init__(self, i):
        self.home_page = HomePage(i)

    def click_dialog(self):
        """
        点击弹出框
        """
        self.home_page.get_dialog_element().click()
