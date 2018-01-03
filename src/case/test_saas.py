import sys

print(sys.path)


import unittest
from selenium import webdriver
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






