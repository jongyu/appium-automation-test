# coding=utf-8
import os

from dos_cmd import DosCmd
from port import Port
import threading
import time
from write_user_command import WriteUserCommand

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()

    def get_devices(self):
        """
        获取设备信息
        """

        devices_list = []
        result_list = self.dos.execute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        """
        创建可用端口
        """
        port = Port()
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        """
        生成命令
        """
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        # noinspection PyTypeChecker
        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + \
                  device_list[i] + " --no-reset --session-override --log " + PATH("../../build/logs/appium-") + "" + str(i + 1) + ".log"
        command_list.append(command)
        self.write_file.write_data(i, device_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))

        return command_list

    def start_server(self, i):
        """
        启动服务
        """
        self.start_list = self.create_command_list(i)
        print self.start_list

        self.dos.execute_cmd(self.start_list[0])

    def kill_server(self):
        server_list = self.dos.execute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.execute_cmd('taskkill -F -PID node.exe')

    def main(self):
        thread_list = []
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(25)


if __name__ == '__main__':
    server = Server()
    print server.main()
