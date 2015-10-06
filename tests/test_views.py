# -*- encoding: utf-8 -*-
import sys

from tests import HauskaTestCase
import hauska

class ViewTestCase(HauskaTestCase):
    def testIndexIs200(self):
        rv = self.app.get("/")
        self.assertEquals(rv.status_code, 200)

    def testNoRefs(self):
        rv = self.app.get("/refs")
        assert 'No entries yet' in rv.data

    def testRefs(self):
        db = hauska.get_db()
        db.execute("""INSERT INTO articles
        (bibtexkey, author, title, journal, year, volume, number, pages, month, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   ["123"]*10)
        rv = self.app.get("/refs")
        assert 'No entries yet' not in rv.data
