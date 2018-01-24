import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
from selenium.webdriver.common.by import By
from selenium import webdriver
from src.common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep





class login_page(BasePage):
    name_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[1]/div/input')
    password_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[2]/div/input')
    login_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[3]/div/a')
    toast_loc = ( '//*[@id="root"]/div/div[4]/div/div/div[3]/span')

    def openit(self):
        self._open(self.url, self.title)

    def input_name(self, name_value):
        self.find_element(*self.name_loc).send_keys(name_value)
    
    def input_password(self, password_value):
        self.find_element(*self.password_loc).send_keys(password_value)
    
    def click_login(self):
        self.find_element(*self.login_loc).click()


class ShowAll_page(login_page):
    tab_loc = ('//*[@id="root"]/div/div[4]/section/div/div/aside/ul[1]/li/a')
    button_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/nav/div[2]/div[2]/div')
    setting_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/nav/div[2]/div[2]/div/div/div[1]/div/a')
    detail_loc = (By.XPATH,'//*[@id="root"]/div/div[4]/section/div/div/div/div/div/div/div/div/div[3]/div[2]/a')
    logout_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/nav/div[2]/div[2]/div/div/div[3]/a')
    
    def login_success(self):
        '''封装登录'''
        try:
            self.openit()
            self.input_name("12341988924") 
            self.input_password("123456")
            self.click_login()
            sleep(1)
        except:
            self.mylog.error('登录失败')


    def attribute(self, element):
        self.find_element(*self.tab_loc).get_attribute(element)
        

    def hover_it(self):
        self.hover(*self.button_loc)
    
    def click_setting(self):
        self.find_element(*self.setting_loc).click()

    def click_detail(self):
        self.find_element(*self.detail_loc).click()
    
    def click_logout(self):
        self.find_element(*self.logout_loc).click()
        


