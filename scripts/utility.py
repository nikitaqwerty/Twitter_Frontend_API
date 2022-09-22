from Twitter_Frontend_API import Client

def generate_identities(api: Client):
    ct0 = api.generate_ct0()
    auth = api.generate_authenticity()
    token = api.generate_token()
    return ct0, auth, token