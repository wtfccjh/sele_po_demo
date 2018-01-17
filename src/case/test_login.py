import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
import unittest
from selenium import webdriver
from src.page.login_page import login_page
from time import sleep
from src.common import excel_data
from src.common.mylog import mylog




class TestSaasLogin(unittest.TestCase):
    def setUp(self):
        self.mylog = mylog()
        self.driver = webdriver.Chrome()
        self.url = 'https://tomorning.me:20001/login'
        self.login_page = login_page(self.driver, self.url, 'SaaS Web')
        self.excel = excel_data.excel()



    def test_login(self):
        '''excel中数据驱动'''
        logindata_list = self.excel.get_list('logindata')
        print(logindata_list)
        for x in range(0, len(logindata_list)):
            username = logindata_list[x]["username"]
            password = logindata_list[x]["password"]
            assert_toast = logindata_list[x]["assert"]
            next_url = logindata_list[x]["next_url"]    #以上 获取每列数据
            try:
                self.login_page.openit()
                self.login_page.input_name(username)
                self.login_page.input_password(password)
                self.login_page.click_login()
                sleep(1)
                if self.driver.current_url == self.url:
                    toast_element = self.driver.find_element_by_xpath(self.login_page.toast_loc) #登录成功后无法定位此元素 因此先判断当前页面
                    toast = toast_element.text
                    self.assertEqual(toast, assert_toast) #与execl中数据进行比较断言
                else: 
                    self.assertEqual(self.driver.current_url, next_url)
            except Exception as e:
                self.mylog.error('error_log ')
                self.login_page.img_screenshot('error_img')
                raise e




    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()








