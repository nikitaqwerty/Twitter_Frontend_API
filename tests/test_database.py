import json
from conftest import PATH, os


def test_database_add_unique_ids(db):
    ## arrange
    with open(os.path.join(PATH, "outputs/rtfkt_ids.json"), "r") as f:
        test_ids1 = json.load(f)
    with open(os.path.join(PATH, "outputs/rtfkt_ids_2.json"), "r") as f:
        test_ids2 = json.load(f)

    ## act
    db.add_ids_from_list(test_ids1["ids"], test_ids1["next_cursor_str"])
    db.add_ids_from_list(test_ids2["ids"], test_ids2["next_cursor_str"])

    ## assert
    assert db.cur.execute("select count(*) from rtfkt_followers").fetchone()[0] == len(
        test_ids1["ids"]
    ) + len(test_ids2["ids"])
