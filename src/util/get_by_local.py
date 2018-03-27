# coding=utf-8
from read_init import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, section):
        read_ini = ReadIni()
        local = read_ini.get_value(key, section)
        if local is not None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            # noinspection PyBroadException
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                self.driver.save_screenshot("../images/test.png")
                # return None
        else:
            return None
