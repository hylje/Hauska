from tests import HauskaTestCase
from tests.test_add import AddMixin

import os

class EditTestCase(HauskaTestCase, AddMixin):
    def _testEditing(self, reftype):
        first_rv = self.app.get("/%s/1" % reftype)
        random_author = os.urandom(8).encode("hex")

        self.assertNotIn(random_author, first_rv.data)

        dummy_data = dict(getattr(self, "%s_dummy_data" % reftype))
        dummy_data.update({"author": random_author})

        post_rv = self.app.post(
            "/%s/1/edit" % reftype,
            data=dummy_data,
            follow_redirects=True
        )

        self.assertEqual(post_rv.status_code, 200)

        check_rv = self.app.get("/%s/1" % reftype)

        self.assertIn(random_author, check_rv.data)

    def testEditArticle(self):
        self._postArticle()
        self._testEditing("article")

    def testEditBook(self):
        self._postBook()
        self._testEditing("book")

    def testEditBooklet(self):
        self._postBooklet()
        self._testEditing("booklet")

    def testEditConference(self):
        self._postConference()
        self._testEditing("conference")

    def testEditInproceedings(self):
        self._postInproceedings()
        self._testEditing("inproceedings")
