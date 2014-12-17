__author__ = 'joaopaulomusico'

from selenium import webdriver
from model.base_page_object import BasePageObject

class AdminPage(BasePageObject):

    _xpaths = {
        'input': {
            'login_username': ".//input[@id='user_login']",
            'login_password': ".//input[@id='user_pass']",
            'login_submit': ".//input[@id='wp-submit']"
        }
    }

    def navigate(self):
        self._driver.get('http://192.168.59.103:8080/wp-login.php')

    def do_login(self,username,password):
        xpath = self._xpaths['input']['login_username']
        username_field = self._driver.find_element_by_xpath(xpath)
        username_field.send_keys(username)
        xpath = self._xpaths['input']['login_password']
        password_field = self._driver.find_element_by_xpath(xpath)
        password_field.send_keys(password)
        xpath = self._xpaths['input']['login_submit']
        login_button = self._driver.find_element_by_xpath(xpath)
        login_button.click()