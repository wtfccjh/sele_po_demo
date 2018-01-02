from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import log
from src.config.parameter import img_path





class BasePage(object):
    def __init__(self, base_url, selenium_driver,  page_title):
        self.driver = selenium_driver
        self.url = base_url
        self.title = page_title
        self.mylog = log.log()

    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            assert page_title in self.driver.title, u'打开页面失败：%s ' %url
        except:
            self.mylog.error('error' + url)
    
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            self.mylog.error('error' +str(loc))
        
    def send_keys(self, value, clear=True, *loc):
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except:
            self.mylog.error('输入失败, loc='+str(loc)+ ' value='+value)
    
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file()
        except:
            self.mylog.error('截图失败：'+img_name)

