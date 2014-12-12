__author__ = 'joaopaulomusico'

from selenium import webdriver

class AdminPage():

    _xpaths = {
        'span': {
            'item': 'test
        }
    }

    def __init__(self):
        self._driver= webdriver.Firefox()

    def navigate(self):
        self._driver.get('http://192.168.59.103:8080')