import sys
sys.path.append("/home/ccjh/demo_git/sele_po_demo")
from selenium.webdriver.common.by import By
from src.common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains





class SaasPage(BasePage):
    name_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[1]/div/input')
    password_loc = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div[2]/div/input')
    login_loc = (By.CLASS_NAME, 'button is-link is-outlined tile')

    def open(self):
        self._open(self.url, self.title)

    def input_name(self, name_loc):
        self.find_element(*self.name_loc).send_keys(name_loc)
    
    def input_password(self, password_loc):
        self.find_element(*self.password_loc).send_keys(password_loc)
    
    def click_login(self, login_loc):
        self.find_element(*self.login_loc).click()
