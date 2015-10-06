# -*- encoding: utf-8 -*-
import sys

from tests import HauskaTestCase
from hauska.views import handle_special_characters_in_bibtex_value

class ViewTestCase(HauskaTestCase):
    def testIndexIs200(self):
        rv = self.app.get("/")
        self.assertEquals(rv.status_code, 200)

    # def testNoRefs(self):
    #     with self.app.app_context():
    #         rv = self.app.get("/refs")
    #         assert 'No refs yet' in rv.data
    def test_handleing_special_characters_correctly(self):
        a="Åkerlöndä Ö. Äkå"
        handled=handle_special_characters_in_bibtex_value(a)
        self.assertEqual(handled,'{\\AA}kerl{\\\"o}nd{\\\"a} {\\\"O}. {\\\"A}k{\\aa}')