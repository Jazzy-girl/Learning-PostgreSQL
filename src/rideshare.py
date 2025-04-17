from src.learning344_db_utils import *

def rebuildTables():
  """Rebuild the tables to initialize the db"""
  conn = connect()
  cur = conn.cursor()
  drop_sql = """
        DROP TABLE IF EXISTS example_table
    """
  create_sql = """
        CREATE TABLE example_table(
            example_col VARCHAR(40)
        )
    """
  cur.execute(drop_sql)
  cur.execute(create_sql)
  conn.commit()
  conn.close()
