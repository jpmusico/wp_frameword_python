__author__ = 'joaopaulomusico'

import unittest

from pages.wp_admin_page import AdminPage

class PlayGround(unittest.TestCase):

    def test_test01(self):
        admin_page = AdminPage()
        admin_page.navigate()