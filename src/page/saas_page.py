import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
from selenium.webdriver.common.by import By
from src.common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains





class saas_page(BasePage):
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



