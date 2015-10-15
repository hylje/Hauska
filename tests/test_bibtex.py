# -*- encoding: utf-8 -*-

from hauska import get_db
from hauska.utils import bibtexkey_exists

from tests import HauskaTestCase
from tests.test_add import AddMixin


class BibtexTestCase(HauskaTestCase, AddMixin):
    def testArticleBibtexLooksCorrect(self):
        self._postArticle()

        reference_data = """
@article{1,
	author = "123",
	title = "123",
	journal = "123",
	year = "123",
	volume = "123",
	number = "123",
	pages = "123",
	month = "123",
	note = "123",
}""".strip()

        rv = self.app.get("/article/1/bib")

        self.assertEqual(
            rv.data.strip(),
            reference_data
        )

    def testBibtexkeyGlobalUnique(self):
        self.assertFalse(bibtexkey_exists(1))

        self._postArticle()

        self.assertTrue(bibtexkey_exists("1"))
        self.assertTrue(bibtexkey_exists(1))
        self.assertFalse(bibtexkey_exists("2"))

        self._postArticle({
            "bibtexkey": "2",
            "author": "123",
            "title": "123",
            "journal": "123",
            "year": "123",
            "volume": "123",
            "number": "123",
            "pages": "123",
            "month": "123",
            "note": "123",
        })

        self.assertTrue(bibtexkey_exists("2"))

    def testCannotSubmitDuplicateArticle(self):
        db = get_db()

        self._postArticle()
        cur = db.execute("SELECT count(1) FROM articles WHERE bibtexkey=1")
        self.assertEqual(cur.fetchone()[0], 1)

        rv = self._postArticle()
        cur = db.execute("SELECT count(1) FROM articles WHERE bibtexkey=1")
        self.assertEqual(cur.fetchone()[0], 1)

        self.assertIn("This reference name already exists", rv.data)

    def testCannotSubmitDuplicateNonArticle(self):
        db = get_db()

        self._postArticle()
        cur = db.execute("SELECT count(1) FROM articles WHERE bibtexkey=1")
        self.assertEqual(cur.fetchone()[0], 1)

        rv = self._postBook({"bibtexkey": "1"})

        cur = db.execute("SELECT count(1) FROM books WHERE bibtexkey=1")
        self.assertEqual(cur.fetchone()[0], 0)

        self.assertIn("This reference name already exists", rv.data)
