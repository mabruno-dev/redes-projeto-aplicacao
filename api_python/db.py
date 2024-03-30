import psycopg2 as postgresql
from psycopg2.extras import DictCursor


class Database():

    def __init__(self) -> None:
        try:

            self._conn = postgresql.connect("""dbname='proj-aplicacao-redes'
                                            host='localhost'
                                            port=5433
                                            user='postgres'
                                            password='root'
                                            """)
            self._cursor = self._conn.cursor(row_factory=DictCursor)
        except Exception as E:
            print(f'Erro: {str(E)}')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close(False)

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def queryone(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()