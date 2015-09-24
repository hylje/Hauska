# -*- encoding: utf-8 -*-
from tests import HauskaTestCase

class ViewTestCase(HauskaTestCase):
    def testIndexIs200(self):
        rv = self.app.get("/")
        self.assertEquals(rv.status_code, 200)
