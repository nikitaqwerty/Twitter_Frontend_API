import sqlite3
import os


class Database:
    def __init__(self, path, db_name, recreate=False) -> None:
        DB_PATH = os.path.join(path,'outputs',db_name)
        if recreate and os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        self._create_connection(DB_PATH)
        self.cur = self.con.cursor()
        self.con.row_factory = lambda cur, row: row[0]


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
        try:
            self.cur.executemany(
                "insert into rtfkt_followers (id, next_cursor) VALUES(?, ?)", data
            )
            self.con.commit()
        except sqlite3.IntegrityError:
            ids_exists = self.con.execute('''SELECT id from rtfkt_followers''').fetchall()
            new_ids = set(ids).difference(ids_exists) 
            new_data = [(id, next_cursor) for id in new_ids]
            self.cur.executemany(
                "insert into rtfkt_followers (id, next_cursor) VALUES(?, ?)", new_data
            )
            self.con.commit()

# if __name__ == "__main__":

#     DB_PATH = os.path.join(PATH, "outputs/twitter.db")
#     os.remove(DB_PATH)
#     db = Database(DB_PATH)
#     db._create_tables()

#     import json

#     with open(os.path.join(PATH, "outputs/rtfkt_ids.json"), "r") as f:
#         test_ids1 = json.load(f)
#     with open(os.path.join(PATH, "outputs/rtfkt_ids_2.json"), "r") as f:
#         test_ids2 = json.load(f)

#     db.add_ids_from_list(test_ids1["ids"], test_ids1["next_cursor_str"])
#     db.add_ids_from_list(test_ids2["ids"], test_ids2["next_cursor_str"])
