# -*- encoding: utf-8 -*-

from tests import HauskaTestCase
import hauska

class DeleteTestCase(HauskaTestCase):
    def testDeletingReferenceActuallyDeletes(self):
        db = hauska.get_db()

        cur = db.execute("SELECT count(1) FROM articles")
        self.assertEqual(cur.fetchone()[0], 0)

        rv = self.app.post("/add/article", data={
            "bibtexkey": "xx1",
            "author": "123",
            "title": "123",
            "journal": "123",
            "year": "123",
            "volume": "123",
            "number": "123",
            "pages": "123",
            "month": "123",
            "note": "123",
        }, follow_redirects=True)

        cur = db.execute("SELECT count(1) FROM articles")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: xx1", rv.data)
        
        #send form containing bibtexkey to /delete via button in view_<ref>.html
        rv = self.app.post("/delete", data={
            "bibtexkey": "xx1"
        }, follow_redirects=True)
        
        self.assertNotIn("bibtex key: xx1", rv.data)
        
        