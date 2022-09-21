import os
from db import Database
from time import sleep
from random import random
from utility import generate_identities
from Twitter_Frontend_API import Client
PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# cycle setup
api = Client()
db = Database(PATH,'twitter.db')
db._create_tables()
next_cursor = None
i = 0
# iterate through ids
while True:
    print("step#",i)
    out = api.followers_ids("RTFKT", cursor=next_cursor)
    ids = out["ids"]
    next_cursor = out["next_cursor_str"]
    db.add_ids_from_list(ids,next_cursor)

    # no more pages    
    if next_cursor == '0':
        break

    i+= 1
    if random() > 0.95:
        sleep(3)
    if random() > 0.90:
        api = Client()
