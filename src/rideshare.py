from src.learning344_db_utils import *

DB1_FILE = "src/test.sql"
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

def db1Tables():
  """Rebuild the tables to initialize the db"""
  conn = connect()
  cur = conn.cursor()
  drop_sql = """
        DROP TABLE IF EXISTS riders, drivers
    """
  create_sql = read_sql_file(DB1_FILE)
  cur.execute(drop_sql)
  cur.execute(create_sql)
  conn.commit()
  conn.close()
