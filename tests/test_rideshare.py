import unittest
from src.rideshare import *
from src.learning344_db_utils import connect

class TestChat(unittest.TestCase):

    def test_rebuild_tables(self):
        """Rebuild the tables"""
        rebuildTables()
        result = exec_get_all('SELECT * FROM example_table')
        self.assertEqual([], result, "no rows in example_table")
    
    def test_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        rebuildTables()
        rebuildTables()
        result = exec_get_all('SELECT * FROM example_table')
        self.assertEqual([], result, "no rows in example_table")

    def test_db1_tables(self):
        """Rebuild the tables"""
        db1Tables()
        result1 = exec_get_all('SELECT * FROM riders')
        self.assertEqual([(1, 'Mike Easter', 'None', '4.3', 'abc123')], result1)
        # result2 = exec_get_all('SELECT * FROM drivers')
        # self.assertEqual([], result2, "no rows in drivers")