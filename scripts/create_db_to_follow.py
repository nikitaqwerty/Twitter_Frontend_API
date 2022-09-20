import os
from db import Database
from time import sleep
from random import random
from Twitter_Frontend_API import Client
PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

api = Client()

# SetUp
print(api.generate_ct0())
print(api.generate_authenticity())
print(api.generate_token())

db = Database(PATH,'twitter.db')

next_cursor = None
while True:
    out = api.followers_ids("RTFKT", cursor=next_cursor)
    ids = out["ids"]
    next_cursor = out["next_cursor_str"]
