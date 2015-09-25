# -*- encoding: utf-8 -*-
import hauska

from tests import HauskaTestCase

class GeneralTestCase(HauskaTestCase):
    def testRefsTableExists(self):
        db = hauska.db_connection()
        cursor = db.cursor()
        result_count = cursor.execute("PRAGMA table_info(refs)")
        self.assertGreater(result_count, 0)
