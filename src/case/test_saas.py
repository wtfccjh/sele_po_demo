import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
import unittest
from selenium import webdriver
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
        logindata_list = self.excel.get_list('logindata')
        print(logindata_list)
        for x in range(0, len(logindata_list)):
            username = logindata_list[x]["username"]
            password = logindata_list[x]["password"]
            assert_toast = logindata_list[x]["assert"]
            next_url = logindata_list[x]["next_url"]
            try:
                self.saas_page.openit()
                self.saas_page.input_name(username)
                self.saas_page.input_password(password)
                self.saas_page.click_login()
                sleep(1)
                toast_element = self.driver.find_element_by_xpath(self.saas_page.toast_loc)
                toast = toast_element.text
                if toast_element:
                    self.assertEqual(toast, assert_toast)
                #print(self.driver.find_element_by_xpath(self.saas_page.toast_loc).text)
                #driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div/div[3]/span').text
                else:
                    self.assertEqual(self.driver.current_url, next_url)
            except Exception as e:
                self.mylog.error('error_log ')
                self.saas_page.img_screenshot('error_img')
                raise e




    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()








