# -*- encoding: utf-8 -*-
from tests import HauskaTestCase

class ViewTestCase(HauskaTestCase):
    def testIndexIs200(self):
        rv = self.app.get("/")
        self.assertEquals(rv.status_code, 200)

    # def testNoRefs(self):
    #     with self.app.app_context():
    #         rv = self.app.get("/refs")
    #         assert 'No refs yet' in rv.data
