import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import *
from src.common import mylog
from config.parameter import img_path





class BasePage(object):
    def __init__(self, selenium_driver, base_url, page_title):
        self.driver = selenium_driver
        self.url = base_url
        self.title = page_title
        self.mylog = mylog.mylog()

    #   打开页面,并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
    #断言titie
            assert page_title in self.driver.title, u'打开页面失败：%s' % url
        except:
            self.mylog.error(u'未能正确打开页面:'+url)

    #封装定位
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            #self.driver.finf_element(*loc)
        except:
            self.mylog.error(u'找不到元素:'+str(loc))

    #封装输入
    def send_keys(self, value, clear=True, *loc):
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.mylog.error(u'输入失败,loc='+str(loc)+u';value='+value)



    #   截图
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path+img_name+'.png')
        except:
            self.mylog.error(u'截图失败：'+img_name)

    #   hover
    def hover(self, *loc):
        try:
            ActionChains(self.driver).move_to_element(self.find_element(*loc)).perform()
        except:
            self.mylog.error('悬停失败')


