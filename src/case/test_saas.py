import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
import unittest
from selenium import webdriver
#from ....page.saas_page import SaasPage
from src.page.saas_page import saas_page
from time import sleep
from src.common import excel_data
from src.common.mylog import mylog




class TestSaasLogin(unittest.TestCase):
    def setUp(self):
        self.mylog = mylog()
        self.driver = webdriver.Chrome()
        self.url = 'https://tomorning.me:20001/login'
        self.saas_page = saas_page(self.driver, self.url, 'SaaS Web')
        self.excel = excel_data.excel()

    def test_login(self):
        '''demo'''
        name_list = self.excel.get_list('username')
        password_list = self.excel.get_list('password')
        print(password_list)
        for x in range(0, len(name_list)):
            for y in range(0, len(password_list)):
                username = name_list[x]["username"]
                password = password_list[y]["password"]
                try:
                    self.saas_page.openit()
                    self.saas_page.input_name(username)
                    self.saas_page.input_password(password)
                    self.saas_page.click_login()
                    sleep(1)
                    print(self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div/div[3]/span').text)
                except Exception as e:
                    self.mylog.error('error_log ')
                    self.saas_page.img_screenshot('error_img')
                    raise e




    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()








