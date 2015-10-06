# -*- encoding: utf-8 -*-
import hauska

from tests import HauskaTestCase
from hauska.views import handle_special_characters_in_bibtex_value

class GeneralTestCase(HauskaTestCase):
    def testArticlesTableExists(self):
        db = hauska.get_db()
        cursor = db.cursor()
        cursor.execute("PRAGMA table_info(articles)")
        self.assertGreater(len(cursor.fetchall()), 0)

    def test_handleing_special_characters_correctly(self):
        a="Åkerlöndä Ö. Äkå"
        handled=handle_special_characters_in_bibtex_value(a)
        self.assertEqual(handled,'{\\AA}kerl{\\\"o}nd{\\\"a} {\\\"O}. {\\\"A}k{\\aa}')
