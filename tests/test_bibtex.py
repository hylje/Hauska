# -*- encoding: utf-8 -*-

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
