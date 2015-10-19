# -*- encoding: utf-8 -*-

from tests import HauskaTestCase
import hauska

class AddMixin(object):
    article_dummy_data = {
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

    def _postArticle(self, update_data=None):
        if update_data:
            dummy_data = dict(self.article_dummy_data)
            dummy_data.update(update_data)
        else:
            dummy_data = self.article_dummy_data

        return self.app.post("/add/article",
                             data=dummy_data,
                             follow_redirects=True)

    book_dummy_data = {
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

    def _postBook(self, update_data=None):
        if update_data:
            dummy_data = dict(self.book_dummy_data)
            dummy_data.update(update_data)
        else:
            dummy_data = self.book_dummy_data

        return self.app.post("/add/book",
                             data=dummy_data,
                             follow_redirects=True)

    booklet_dummy_data = {
            "bibtexkey": "3",
            "author": "123",
            "title": "123",
            "howpublished": "123",
            "address": "123",
            "year": "123",
            "month": "123",
            "note": "123",
    }

    def _postBooklet(self, update_data=None):
        if update_data:
            dummy_data = dict(self.booklet_dummy_data)
            dummy_data.update(update_data)
        else:
            dummy_data = self.booklet_dummy_data

        return self.app.post("/add/booklet",
                             data=dummy_data,
                             follow_redirects=True)

    conference_dummy_data = {
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
        }

    def _postConference(self, update_data=None):
        if update_data:
            dummy_data = dict(self.conference_dummy_data)
            dummy_data.update(update_data)
        else:
            dummy_data = self.conference_dummy_data

        return self.app.post("/add/conference",
                             data=dummy_data,
                             follow_redirects=True)

    inproceedings_dummy_data = {
            "bibtexkey": "5",
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
    }

    def _postInproceedings(self, update_data=None):
        if update_data:
            dummy_data = dict(self.inproceedings_dummy_data)
            dummy_data.update(update_data)
        else:
            dummy_data = self.inproceedings_dummy_data

        return self.app.post("/add/inproceedings",
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

        rv = self._postBooklet()

        cur = db.execute("SELECT count(1) FROM booklets")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: 3", rv.data)

    def testAddingConferenceActuallyAdds(self):
        db = hauska.get_db()

        cur = db.execute("SELECT count(1) FROM conferences")
        self.assertEqual(cur.fetchone()[0], 0)

        rv = self._postConference()

        cur = db.execute("SELECT count(1) FROM conferences")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: 4", rv.data)

    def testAddingInproceedingsActuallyAdds(self):
        db = hauska.get_db()

        cur = db.execute("SELECT count(1) FROM inproceedings")
        self.assertEqual(cur.fetchone()[0], 0)

        rv = self._postInproceedings()

        cur = db.execute("SELECT count(1) FROM inproceedings")
        self.assertEqual(cur.fetchone()[0], 1)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("bibtex key: 5", rv.data)
