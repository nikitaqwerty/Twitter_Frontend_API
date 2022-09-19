import sqlite3
import os

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Database:
    def __init__(self) -> None:
        DB_PATH = os.path.join(PATH, "outputs/twitter.db")
        self._create_connection(DB_PATH)
        self.cur = self.con.cursor()

    def _create_connection(self, db_file):
        """create a database connection to a SQLite database"""
        self.con = sqlite3.connect(db_file)
        print(sqlite3.version)

    def _create_tables(self):
        sql = """
        CREATE TABLE account_ids(
            id UNSIGNED BIG INT PRIMARY KEY UNIQUE,
            t TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            followed BOOLEAN DEFAULT(FALSE)
        );
        """
        self.cur.execute(sql)


if __name__ == "__main__":
    db = Database()
    db._create_tables()
