from typing import Optional
from psycopg2 import connect, OperationalError
from psycopg2.errors import UndefinedTable
from psycopg2.errors import DuplicateDatabase
#Python nie znajduje mi tej biblioteki mimo poprawnie zainstalowanego psycopg2


def execute_sql(sql_to_execute: str) -> Optional[list]:
    try:
        conn = connect(user='postgres',
                       password='coderslab',
                       host='localhost')
        with conn.cursor() as cur:
            conn.autocommit = True
            cur.execute(sql_to_execute)
            try:
                result = list(cur)
            except:
                result = None
    except OperationalError:
        print('Nieudane połączenie z bazą danych.')
        result = None
    except UndefinedTable:
        print('Nie znaleziono tabeli.')
        result = None
    except Exception as DuplictateDatabase:
        print("Such database arleady exists: ", DuplictateDatabase)
        result = None
    else:
        conn.close()
    return result


if __name__ == '__main__':
    sql_code = "CREATE DATABASE exam2;"
    execute_sql(sql_code)
