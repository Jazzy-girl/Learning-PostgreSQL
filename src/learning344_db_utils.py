import psycopg2
import yaml
import os




def read_sql_file(file_path):
    """
    Opens and reads an sql file. Returns the file as a string to be used for commands.
    """
    try:
        with open(file_path, "r") as file:
            sql_content = file.read()
        return sql_content
    except FileNotFoundError:
        print(f"Error: SQL file not found at {file_path}")
    except Exception as e:
        print(f"Error reading SQL file: {e}")
        exit()


def connect():
    """
    Connects you to Postgres via config. Closing this connection is up to you.
    """
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__), '../config/db.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])


def exec_sql_file(path):
    """
Opens up an SQL file and blindly executes everything inside. Useful for test data and your schema.
Having your code in an SQL file also gives syntax highlighting!
"""
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()


def exec_get_one(sql, args={}):
    """
Runs a query and assumes that you only want the top result and return that.
Does NOT commit any changes (don't use it for updates).
"""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one


def exec_get_all(sql, args={}):
    """
Runs a query and returns all results, usually as a list of tuples.
Does NOT commit any changes (don't use it for updates).
"""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    # https://www.psycopg.org/docs/cursor.html#cursor.fetchall
    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples


def exec_commit(sql, args={}):
    """
Runs SQL and does a commit operation (use this for updating/changing the database).
"""
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result

