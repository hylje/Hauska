# -*- encoding: utf-8 -*-

import unittest

import hauska


class HauskaTestCase(unittest.TestCase):
    def setUp(self):
        hauska.app.config['DATABASE'] = ":memory:"
        hauska.app.config['TESTING'] = True
        self.app = hauska.app.test_client()
        hauska.init_db()

