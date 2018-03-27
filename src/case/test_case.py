# coding=utf-8
import multiprocessing
import unittest

import sys

import time

from business.home_business import HomeBusiness
from util.server import Server
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpclass---->", parames
        cls.home_business = HomeBusiness(parames)

    def setUp(self):
        print "this is setup\n"

    def test_01(self):
        print "test case 里面的参数", parames
        self.home_business.dialog_pass()

    def tearDown(self):
        time.sleep(1)
        print "this is teardown\n"

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print "this is class teardown\n"


def appium_init():
    server = Server()
    server.main()


def get_suite(args):
    print "get_suite里面的", args
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", parame=args))
    unittest.TextTestRunner().run(suite)


def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        print i
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
