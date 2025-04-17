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