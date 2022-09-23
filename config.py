from dotenv import load_dotenv,dotenv_values

load_dotenv('.')
config = dotenv_values()

TWITTER_LOGIN = config['TWITTER_LOGIN']
TWITTER_PASS = config['TWITTER_PASS']
