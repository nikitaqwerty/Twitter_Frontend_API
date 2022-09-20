import sqlite3
import os

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Database:
    def __init__(self, path) -> None:
        DB_PATH = path
        self._create_connection(DB_PATH)
        self.cur = self.con.cursor()

    def _create_connection(self, db_file):
        """create a database connection to a SQLite database"""
        self.con = sqlite3.connect(db_file)
        print("Sqlite version",sqlite3.version)

    def _create_tables(self):
        sql = """
        CREATE TABLE if not exists rtfkt_followers(
            id UNSIGNED BIG INT PRIMARY KEY UNIQUE,
            next_cursor TEXT,
            followed BOOLEAN DEFAULT(FALSE),
            t TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );
        """
        self.cur.execute(sql)

    def add_ids_from_list(self, ids, next_cursor):

        data = [(id, next_cursor) for id in ids]
        self.cur.executemany(
            "insert into rtfkt_followers (id, next_cursor) VALUES(?, ?)", data
        )
        self.con.commit()


if __name__ == "__main__":

    DB_PATH = os.path.join(PATH, "outputs/twitter.db")
    os.remove(DB_PATH)
    db = Database(DB_PATH)
    db._create_tables()

    import json

    with open(os.path.join(PATH, "outputs/rtfkt_ids.json"), "r") as f:
        test_ids1 = json.load(f)
    with open(os.path.join(PATH, "outputs/rtfkt_ids_2.json"), "r") as f:
        test_ids2 = json.load(f)

    db.add_ids_from_list(test_ids1["ids"], test_ids1["next_cursor_str"])
    db.add_ids_from_list(test_ids2["ids"], test_ids2["next_cursor_str"])
