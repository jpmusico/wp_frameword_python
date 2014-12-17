__author__ = 'joaopaulomusico'

from model.base_test_case import BaseTestCase
from pages.wp_admin_page import AdminPage

class PlayGround(BaseTestCase):

    def test_test01(self):
        admin_page = AdminPage(self._driver)
        admin_page.navigate()
        admin_page.do_login('test','test')