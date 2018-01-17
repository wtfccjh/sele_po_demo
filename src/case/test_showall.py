import unittest
from selenium import webdriver
from src.page.login_page import ShowAll_page
from time import sleep
from src.common import excel_data
from src.common.mylog import mylog



class TestSaasShowAll(unittest.TestCase):
    def setUp(self):
        self.mylog = mylog()
        self.driver = webdriver.Chrome()
        self.url = 'https://tomorning.me:20001/login'
        self.ShowAll_page = ShowAll_page(self.driver, self.url, 'SaaS Web')
        self.excel = excel_data.excel()
        
    def test_showall(self):
        try:
            self.ShowAll_page.openit()
            self.ShowAll_page.input_name("1768230209")
            self.ShowAll_page.input_password("123456")
            self.ShowAll_page.click_login()
            print (self.ShowAll_page.selected)
        except Exception as e:
                self.mylog.error('error_log ')
                self.ShowAll_page.img_screenshot('error_img')
                raise e

    def tearDown(self):
        self.driver.close() 


if __name__ == '__main__':
    unittest.main()