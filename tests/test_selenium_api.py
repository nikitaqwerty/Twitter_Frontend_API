from config import TWITTER_LOGIN, TWITTER_PASS
from twitter_selenium_api import TwitterBot
from time import sleep

def test_login():
    tb = TwitterBot(TWITTER_LOGIN, TWITTER_PASS)
    tb.login()
    tb.quit_browser()
    assert tb.is_logged_in == True
