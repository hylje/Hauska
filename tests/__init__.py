# -*- encoding: utf-8 -*-

import unittest

import hauska


class HauskaTestCase(unittest.TestCase):
    def setUp(self):
        hauska.app.config['DATABASE'] = ":memory:"
        hauska.app.config['TESTING'] = True
        self.app = hauska.app.test_client()

        self.app_context = hauska.app.app_context()
        self.app_context.push()
        hauska.init_db()

    def tearDown(self):
        self.app_context.pop()
