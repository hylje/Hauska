# -*- encoding: utf-8 -*-

from tests import HauskaTestCase
import hauska

class AddMixin(object):
    def _postArticle(self, update_data=None):
        dummy_data = {
            "bibtexkey": "1",
            "author": "123",
            "title": "123",
            "journal": "123",
            "year": "123",
            "volume": "123",
            "number": "123",
            "pages": "123",
            "month": "123",
            "note": "123",
        }

        if update_data:
            dummy_data.update(update_data)

        return self.app.post("/add/article",
                             data=dummy_data,
                             follow_redirects=True)

    def _postBook(self, update_data=None):
        dummy_data = {
            "bibtexkey": "2",
            "author": "123",
            "title": "123",
            "editor": "123",
            "publisher": "123",
            "year": "123",
            "volume": "123",
            "number": "123",
            "series": "123",
            "address": "123",
            "edition": "123",
            "month": "123",
            "note": "123",
        }

        if update_data:
            dummy_data.update(update_data)

        return self.app.post("/add/book",
                             data=dummy_data,
                             follow_redirects=True)


class AddTestCase(HauskaTestCase, AddMixin):
    def testAddingArticleActuallyAdds(self):
        db = hauska.get_db()

        cur = db.execute("SELECT count(1) FROM articles")
        self.assertEqual(cur.fetchone()[0], 0)

        rv = self._postArticle()

        cur = db.execute("SELECT count(1) FROM articles")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: 1", rv.data)

    def testAddingBookActuallyAdds(self):
        db = hauska.get_db()

        cur = db.execute("SELECT count(1) FROM books")
        self.assertEqual(cur.fetchone()[0], 0)

        rv = self._postBook()

        cur = db.execute("SELECT count(1) FROM books")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: 2", rv.data)

    def testAddingBookletActuallyAdds(self):
        db = hauska.get_db()

        cur = db.execute("SELECT count(1) FROM booklets")
        self.assertEqual(cur.fetchone()[0], 0)

        rv = self.app.post("/add/booklet", data={
            "bibtexkey": "3",
            "author": "123",
            "title": "123",
            "howpublished": "123",
            "address": "123",
            "month": "123",
            "year": "123",
            "note": "123",
        }, follow_redirects=True)

        cur = db.execute("SELECT count(1) FROM booklets")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: 3", rv.data)

    def testAddingConferenceActuallyAdds(self):
        db = hauska.get_db()

        cur = db.execute("SELECT count(1) FROM conferences")
        self.assertEqual(cur.fetchone()[0], 0)

        rv = self.app.post("/add/conference", data={
            "bibtexkey": "4",
            "author": "123",
            "title": "123",
            "booktitle": "123",
            "year": "123",
            "editor": "123",
            "volume": "123",
            "number": "123",
            "series": "123",
            "pages": "123",
            "address": "123",
            "month": "123",
            "organization": "123",
            "publisher": "123",
            "note": "123",
        }, follow_redirects=True)

        cur = db.execute("SELECT count(1) FROM conferences")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: 4", rv.data)
