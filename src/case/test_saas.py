import unittest
from selenium import webdriver
from src.page.saas_page import SaasPage
from time import sleep




class TestSaasLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://tomorning.me:20001/login'
        self.saas_page = SaasPage(self.driver, self.url, u'saas')
        self.excel = excel_data.excel()

    def test_login(self):
        u'demo'





