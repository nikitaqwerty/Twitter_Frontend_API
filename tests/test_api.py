from Twitter_Frontend_API import Client
from scripts.utility import generate_identities
from time import sleep
from fake_useragent import UserAgent

def test_fake_ua():
    ua = UserAgent()
    ua2 = UserAgent()
    assert ua.random != ua2.random


def test_reset_connection():
    api = Client()
    token1 = api.guest_token
    api = Client()
    token2 = api.guest_token
    assert token1 != token2

def test_get_id_change_token_get_next_ids():
    api = Client()
    next_cursor = None

    # get first followers batch
    out1 = api.followers_ids("RTFKT", cursor=next_cursor)
    ids1 = out1["ids"]
    next_cursor = out1["next_cursor_str"]

    # update identity and get next followers batch
    api = Client()
    out2 = api.followers_ids("RTFKT", cursor=next_cursor)
    ids2 = out2["ids"]
    next_cursor2 = out2["next_cursor_str"]

    assert len(ids1) == 5000
    assert len(ids2) == 5000

def test_final_step_in_followers_ids_list():
    api = Client()
    next_cursor = '1679834483866289874'

    out1 = api.followers_ids("RTFKT", cursor=next_cursor)
    next_cursor = out1["next_cursor_str"]

    assert next_cursor == '0'


    



# def test_guest_connection_with_gen_identity():
#     print('='*50)

#     # arange
#     api = Client()

#     # act
#     generate_identity(api)
#     rate_limit = api.rate_limit_status()
#     print(rate_limit)

#     # assert
#     assert rate_limit
