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
