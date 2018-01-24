import unittest
from selenium import webdriver
from src.page.login_page import ShowAll_page
from time import sleep
from src.common import excel_data
from src.common.mylog import mylog
from src.common.page_url import url


class TestSaasShowAll(unittest.TestCase):
    def setUp(self):
        self.mylog = mylog()
        self.driver = webdriver.Chrome()
        self.url = url.login_page
        self.ShowAll_page = ShowAll_page(self.driver, self.url, 'SaaS Web')
        self.ShowAll_page.login_success()

        
        
    def test_selected(self):
        '''验证登录后默认选中'''
        try:
            status = self.driver.find_element_by_xpath(self.ShowAll_page.tab_loc).get_attribute("aria-current")
            self.assertEqual(status, 'true')
        except Exception as e:
                self.mylog.error('error_log ')
                self.ShowAll_page.img_screenshot('error_img')
                raise e

    def test_skipToSetting(self):
        '''验证hover并打开账号设置页面'''
        try:
            self.ShowAll_page.hover_it()
            self.ShowAll_page.click_setting()
            sleep(1)
            self.assertEqual(self.driver.current_url, url.setting_page)
        except Exception as e:
                self.mylog.error('error_log ')
                self.ShowAll_page.img_screenshot('error_img')
                raise e

    def test_skipToDetail(self):
        '''验证跳转点击查看button'''
        try:
            self.ShowAll_page.click_detail()
            sleep(1)
            self.assertIn(url.detail_page, self.driver.current_url)
        except Exception as e:
            self.mylog.error('error_log ')
            self.ShowAll_page.img_screenshot('error_img')                
            raise e

        
    def test_logout(self):    
        '''验证hover并退出登录'''
        try:
            self.ShowAll_page.hover_it()
            self.ShowAll_page.click_logout()
            sleep(1)
            self.driver.switch_to_alert().dismiss()
            self.assertEqual(self.driver.current_url, url.showAll_page)
        except Exception as e:
                self.mylog.error('error_log ')
                self.ShowAll_page.img_screenshot('error_img')
                raise e
        sleep(1)
        try:
            self.ShowAll_page.hover_it()
            self.ShowAll_page.click_logout()
            sleep(1)
            self.driver.switch_to_alert().accept()
            self.assertEqual(self.driver.current_url, url.login_page)
        except Exception as e:
                self.mylog.error('error_log ')
                self.ShowAll_page.img_screenshot('error_img')
                raise e
        
    
    def tearDown(self):
        self.driver.close() 


if __name__ == '__main__':
    unittest.main()