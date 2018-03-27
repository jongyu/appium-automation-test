# coding=utf-8
import os


class DosCmd:

    def __init__(self):
        pass

    @staticmethod
    def execute_cmd_result(command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    @staticmethod
    def execute_cmd(command):
        os.system(command)


if __name__ == '__main__':
    dos = DosCmd()
    print(dos.execute_cmd_result('adb devices'))
