import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
import unittest
from selenium import webdriver
#from ....page.saas_page import SaasPage
from src.page.saas_page import SaasPage
from time import sleep
from src.common import excel_data




class TestSaasLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://tomorning.me:20001/login'
        self.saas_page = SaasPage(self.driver, self.url, u'saas')
        self.excel = excel_data.excel()

    def test_login(self):
        '''demo'''
        name_list = self.excel.get_list('username')
        password_list = self.excel.get_list('password')
        print(type(name_list))
        for x in range(0, len(name_list)):
            for y in range(0, len(password_list)):
                username = name_list[x]
                password = password_list[y]
            try:
                self.SaasPage.open()
                self.SaasPage.input_name(username)
                self.SaasPage.input_password(password)
                self.SaasPage.click_login()
            except Exception as e:
                self.mylog.error('error ')
                self.sogou_page.img_screenshot('error')
                raise e

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()








