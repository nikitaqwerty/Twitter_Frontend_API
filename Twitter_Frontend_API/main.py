# -*- coding: utf-8 -*-
import requests
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

###例外クラス###
class TwitterError(Exception):
    pass


###ログイン無し情報取得###

class Client:
    def __init__(self) -> None:
        self.ua = UserAgent()

        headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'User-Agent': self.ua.random
        }
        self.guest_token = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers).json()["guest_token"]

        self.headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-guest-token': self.guest_token,
            'User-Agent': self.ua.random
        }
        

    def generate_ct0(self):
        response = requests.get('https://twitter.com/i/release_notes')
        ct0 = response.cookies.get_dict()["ct0"]

        return ct0

    def generate_authenticity(self):
        response = requests.get('https://twitter.com/account/begin_password_reset')
        soup = BeautifulSoup(response.text, "lxml")
        authenticity_token = soup.find(attrs={'name':'authenticity_token'}).get('value')

        return authenticity_token

    def generate_token(self):
        headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'User-Agent': self.ua.random
        }
        response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers).json()

        return response

    ### Twitter API v1.1 ###

    def rate_limit_status(self, resources=None):
        url = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
        if resources != None:
            url = url + '?resources=' + resources
        response = requests.get(url, headers=self.headers).json()
        return response

    def collections_entries(self, id, count=None, max_position=None, min_position=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/collections/entries.json?id=' + id
        if count != None:
            url = url + '&count=' + count
        if max_position != None:
            url = url + '&max_position=' + max_position
        if min_position != None:
            url = url + '&min_position=' + min_position
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def favorites_list(self, screen_name, count=None, since_id=None, max_id=None, include_entities=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/favorites/list.json?screen_name=' + screen_name
        if count != None:
            url = url + '&count=' + count
        if since_id != None:
            url = url + '&since_id=' + since_id
        if max_id != None:
            url = url + '&max_id=' + since_id
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def followers_ids(self, screen_name, cursor=None, stringify_ids=None, count=None):
        url = 'https://api.twitter.com/1.1/followers/ids.json?screen_name=' + screen_name
        if cursor != None:
            url = url + '&cursor=' + cursor
        if stringify_ids != None:
            url = url + '&stringify_ids=' + stringify_ids
        if count != None:
            url = url + '&count=' + count
        response = requests.get(url, headers=self.headers).json()
        return response

    def followers_list(self, screen_name, cursor=None, count=None, skip_status=None, include_user_entities=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/followers/list.json?screen_name=' + screen_name
        if cursor != None:
            url = url + '&cursor=' + cursor
        if count != None:
            url = url + '&count=' + count
        if skip_status != None:
            url = url + '&skip_status=' + skip_status
        if include_user_entities != None:
            url = url + '&include_user_entities=' + include_user_entities
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def friends_ids(self, screen_name, cursor=None, stringify_ids=None, count=None):
        url = 'https://api.twitter.com/1.1/friends/ids.json?screen_name=' + screen_name
        if cursor != None:
            url = url + '&cursor=' + cursor
        if stringify_ids != None:
            url = url + '&stringify_ids=' + stringify_ids
        if count != None:
            url = url + '&count=' + count
        response = requests.get(url, headers=self.headers).json()
        return response

    def friends_list(self, screen_name, cursor=None, count=None, skip_status=None, include_user_entities=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/friends/list.json?screen_name=' + screen_name
        if cursor != None:
            url = url + '&cursor=' + cursor
        if count != None:
            url = url + '&count=' + count
        if skip_status != None:
            url = url + '&skip_status=' + skip_status
        if include_user_entities != None:
            url = url + '&include_user_entities=' + include_user_entities
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def friendships_show(self, source_screen_name, target_screen_name):
        url = 'https://api.twitter.com/1.1/friendships/show.json?source_screen_name=' + source_screen_name + '&target_screen_name=' + target_screen_name
        response = requests.get(url, headers=self.headers).json()
        return response

    def geo_id(self, place_id):
        url = 'https://api.twitter.com/1.1/geo/id/' + place_id + '.json'
        response = requests.get(url, headers=self.headers).json()
        return response

    def geo_reverse_geocode(self, lat, long, accuracy=None, granularity=None, max_results=None):
        url = 'https://api.twitter.com/1.1/geo/reverse_geocode.json?lat=' + lat + '&long=' + long
        if accuracy != None:
            url = url + '&accuracy=' + accuracy
        if granularity != None:
            url = url + '&granularity=' + granularity
        if max_results != None:
            url = url + '&max_results=' + max_results
        response = requests.get(url, headers=self.headers).json()
        return response

    def geo_search(self, query, granularity=None, accuracy=None, max_results=None, contained_within=None, attribute_street_address=None):
        url = 'https://api.twitter.com/1.1/geo/search.json?query=' + query
        if granularity != None:
            url = url + '&granularity=' + granularity
        if accuracy != None:
            url = url + '&accuracy=' + accuracy
        if max_results != None:
            url = url + '&max_results=' + max_results
        if contained_within != None:
            url = url + '&contained_within=' + contained_within
        if attribute_street_address != None:
            url = url + '&attribute_street_address=' + attribute_street_address
        response = requests.get(url, headers=self.headers).json()
        return response

    def lists_list(self, screen_name, reverse=None):
        url = 'https://api.twitter.com/1.1/lists/list.json?screen_name=' + screen_name
        if reverse != None:
            url = url + '&reverse=' + reverse
        response = requests.get(url, headers=self.headers).json()
        return response

    def lists_members(self, list_id, count=None, cursor=None, include_entities=None, skip_status=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/lists/members.json?list_id=' + list_id
        if count != None:
            url = url + '&count=' + count
        if cursor != None:
            url = url + '&cursor=' + cursor
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if skip_status != None:
            url = url + '&skip_status=' + skip_status
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def lists_memberships(self, screen_name, count=None, cursor=None):
        url = 'https://api.twitter.com/1.1/lists/memberships.json?screen_name=' + screen_name
        if count != None:
            url = url + '&count=' + count
        if cursor != None:
            url = url + '&cursor=' + cursor
        response = requests.get(url, headers=self.headers).json()
        return response

    def lists_ownerships(self, screen_name, count=None, cursor=None):
        url = 'https://api.twitter.com/1.1/lists/ownerships.json?screen_name=' + screen_name
        if count != None:
            url = url + '&count=' + count
        if cursor != None:
            url = url + '&cursor=' + cursor
        response = requests.get(url, headers=self.headers).json()
        return response     

    def lists_show(self, list_id):
        url = 'https://api.twitter.com/1.1/lists/show.json?list_id=' + list_id
        response = requests.get(url, headers=self.headers).json()
        return response

    def lists_statuses(self, list_id, since_id=None, max_id=None, count=None, include_entities=None, include_rts=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/lists/statuses.json?list_id=' + list_id
        if since_id != None:
            url = url + '&since_id=' + since_id
        if max_id != None:
            url = url + '&max_id=' + max_id
        if count != None:
            url = url + '&count=' + count
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if include_rts != None:
            url = url + '&include_rts=' + include_rts
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def lists_subscribers(self, list_id, count=None, cursor=None, include_entities=None, skip_status=None):
        url = 'https://api.twitter.com/1.1/lists/subscribers.json?list_id=' + list_id
        if count != None:
            url = url + '&count=' + count
        if cursor != None:
            url = url + '&cursor=' + cursor
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if skip_status != None:
            url = url + '&skip_status=' + skip_status
        response = requests.get(url, headers=self.headers).json()
        return response

    def lists_subscriptions(self, screen_name, count=None, cursor=None):
        url = 'https://api.twitter.com/1.1/lists/subscriptions.json?screen_name=' + screen_name
        if count != None:
            url = url + '&count=' + count
        if cursor != None:
            url = url + '&cursor=' + cursor
        response = requests.get(url, headers=self.headers).json()
        return response
    
    def search_tweets(self, q, geocode=None, lang=None, locale=None, result_type=None, count=None, until=None, since_id=None, max_id=None, include_entities=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + q
        if geocode != None:
            url = url + '&geocode=' + geocode
        if lang != None:
            url = url + '&lang=' + lang
        if locale != None:
            url = url + '&locale=' + locale
        if result_type != None:
            url = url + '&result_type=' + result_type
        if count != None:
            url = url + '&count=' + count
        if until != None:
            url = url + '&until=' + until
        if since_id != None:
            url = url + '&since_id=' + since_id
        if max_id != None:
            url = url + '&max_id=' + max_id
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def statuses_lookup(self, id, include_entities=None, trim_user=None, map=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/statuses/lookup.json'
        if len(id) != 0:
            url = url + '?id=' + ','.join(id)
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if trim_user != None:
            url = url + '&trim_user=' + trim_user
        if map != None:
            url = url + '&map=' + map
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def statuses_retweeters_ids(self, id, cursor=None, stringify_ids=None):
        url = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=' + id
        if cursor != None:
            url = url + '&cursor=' + cursor
        if stringify_ids != None:
            url = url + '&stringify_ids=' + stringify_ids
        response = requests.get(url, headers=self.headers).json()
        return response       

    def statuses_retweets(self, id, count=None, trim_user=None):
        url = 'https://api.twitter.com/1.1/statuses/retweets/' + id + '.json'
        if count != None:
            url = url + '&count=' + count
        if trim_user != None:
            url = url + '&trim_user=' + trim_user
        response = requests.get(url, headers=self.headers).json()
        return response

    def statuses_show(self, id, trim_user=None, include_entities=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/statuses/show.json?id=' + id
        if trim_user != None:
            url = url + '&trim_user=' + trim_user
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def statuses_user_timeline(self, screen_name, since_id=None, max_id=None, count=None, trim_user=None, exclude_replies=None, contributor_details=None, include_rts=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + screen_name
        if since_id != None:
            url = url + '&since_id=' + since_id
        if max_id != None:
            url = url + '&max_id=' + max_id
        if count != None:
            url = url + '&count=' + count
        if max_id != None:
            url = url + '&max_id=' + max_id
        if trim_user != None:
            url = url + '&trim_user=' + trim_user
        if exclude_replies != None:
            url = url + '&exclude_replies=' + exclude_replies
        if contributor_details != None:
            url = url + '&contributor_details=' + contributor_details
        if include_rts != None:
            url = url + '&include_rts=' + include_rts
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def trends_available(self):
        url = 'https://api.twitter.com/1.1/trends/available.json'
        response = requests.get(url, headers=self.headers).json()
        return response

    def trends_closest(self, lat, long):
        url = 'https://api.twitter.com/1.1/trends/closest.json?lat=' + lat + '&long=' + long
        response = requests.get(url, headers=self.headers).json()
        return response

    def trends_place(self, id, exclude=None):
        url = 'https://api.twitter.com/1.1/trends/place.json?id=' + id
        if exclude != None:
            url = url + '&exclude=' + exclude
        response = requests.get(url, headers=self.headers).json()
        return response   

    def users_lookup(self, screen_name, include_entities=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/users/lookup.json'
        if len(screen_name) != 0:
            url = url + '?screen_name=' + ','.join(screen_name)
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def users_search(self, q, page=None, count=None, include_entities=None, tweet_mode=None):
        url = 'https://api.twitter.com/1.1/users/search.json?q=' + q
        if page != None:
            url = url + '&page=' + page
        if count != None:
            url = url + '&count=' + count
        if include_entities != None:
            url = url + '&include_entities=' + include_entities
        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    def user_show(self, screen_name = None, id = None, include_entities=None, tweet_mode=None):
        if screen_name:
            url = 'https://api.twitter.com/1.1/users/show.json?screen_name=' + screen_name
        elif id:
            url = 'https://api.twitter.com/1.1/users/show.json?id=' + id
        else:
            raise NotImplementedError('provide either screen name or id')

        if tweet_mode != None:
            url = url + '&tweet_mode=' + tweet_mode
        response = requests.get(url, headers=self.headers).json()
        return response

    ### Twitter API v2      ###
    ### OR                  ###
    ### Twitter API Private ###

    def user_tweets(self, screen_name=None, user_id=None):
        params = (
            ('userId', user_id),
        )
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                response = requests.get('https://api.twitter.com/2/timeline/profile/' + user_id + '.json', headers=self.headers, params=params).json()
        else:
            user_id = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screen_name, headers=self.headers).json()["id_str"]
            response = requests.get('https://api.twitter.com/2/timeline/profile/' + user_id + '.json', headers=self.headers, params=params).json()

        return response

    def trend(self):
        response = requests.get('https://twitter.com/i/api/2/guide.json', headers=self.headers).json()

        return response

    def searchbox(self, text):
        params = (
            ('q', text),
            ('src', 'search_box'),
        )
        response = requests.get('https://twitter.com/i/api/1.1/search/typeahead.json', headers=self.headers, params=params).json()

        return response

    def topic_search(self, text):
        params = (
            ('q', text),
            ('tweet_search_mode', 'extended'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def latest_search(self, text):
        params = (
            ('q', text),
            ('tweet_search_mode', 'live'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def image_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'image'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def video_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'video'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def user_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'user'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def screenname_available(self, id):
        params = (
            ('username', id),
        )
        response = requests.get('https://twitter.com/i/api/i/users/username_available.json', headers=self.headers, params=params).json()

        return response

    def get_status(self, tweetid):
        response = requests.get('https://api.twitter.com/2/timeline/conversation/' + tweetid + '.json', headers=self.headers).json()

        return response

    def shadowban_check(self, screen_name=None, user_id=None):
        if not screen_name == None:
            no_tweet = False
            protect = False

            suspend = False
            not_found = False

            search_ban = False
            search_suggestion_ban = False
            ghost_ban = False
            reply_deboosting = False

            adaptive = requests.get("https://api.twitter.com/2/search/adaptive.json?q=from:" + screen_name + "&count=20&spelling_corrections=0", headers=self.headers)
            typeahead = requests.get("https://api.twitter.com/1.1/search/typeahead.json?src=search_box&result_type=users&q=" + screen_name, headers=self.headers)
            show = requests.get("https://api.twitter.com/1.1/users/show.json?screen_name=" + screen_name, headers=self.headers)

            if "errors" in show.json():
                if show.json()["errors"][0]["code"] == 63:
                    suspend = True
                elif show.json()["errors"][0]["code"] == 50:
                    not_found = True

            else:
                if show.json()["protected"] == False:
                    if "status" in show.json():
                        profile = requests.get("https://api.twitter.com/2/timeline/profile/" + str(show.json()["id"]) +".json?include_tweet_replies=1&include_want_retweets=0&include_reply_count=1&count=1000", headers=self.headers)

                        if adaptive.json()['globalObjects']['tweets']:
                            pass
                        else:
                            search_ban = True

                        if typeahead.json()["num_results"] == 0:
                            search_suggestion_ban = True

                        for i in profile.json()["globalObjects"]["tweets"]:
                            for _ in profile.json()["globalObjects"]["tweets"][i]:
                                if _ == "in_reply_to_status_id_str":
                                    conversation = requests.get("https://api.twitter.com/2/timeline/conversation/" + str(profile.json()["globalObjects"]["tweets"][i]["in_reply_to_status_id_str"]) + ".json?include_reply_count=1&send_error_codes=true&count=20", headers=self.headers)
                                    if conversation.status_code == 404:
                                        ghost_ban = True
                                        reply_deboosting = True
                                    else:
                                        deboosting_l = []
                                        for i in conversation.json()["globalObjects"]["tweets"]:
                                            deboosting_l.append(conversation.json()["globalObjects"]["tweets"][i]["user_id_str"])
                                        if str(show.json()["id"]) in deboosting_l:
                                            pass
                                        else:
                                            reply_deboosting = True
                                    break
                            else:
                                continue
                            break

                    else:
                        no_tweet = True
                else:
                    protect = True

        elif not user_id == None:

            screen_name = requests.get('https://api.twitter.com/1.1/users/show.json?user_id=' + user_id, headers=self.headers).json()["screen_name"]

            no_tweet = False
            protect = False

            suspend = False
            not_found = False

            search_ban = False
            search_suggestion_ban = False
            ghost_ban = False
            reply_deboosting = False

            adaptive = requests.get("https://api.twitter.com/2/search/adaptive.json?q=from:" + screen_name + "&count=20&spelling_corrections=0", headers=self.headers)
            typeahead = requests.get("https://api.twitter.com/1.1/search/typeahead.json?src=search_box&result_type=users&q=" + screen_name, headers=self.headers)
            show = requests.get("https://api.twitter.com/1.1/users/show.json?screen_name=" + screen_name, headers=self.headers)

            if "errors" in show.json():
                if show.json()["errors"][0]["code"] == 63:
                    suspend = True
                elif show.json()["errors"][0]["code"] == 50:
                    not_found = True

            else:
                if show.json()["protected"] == False:
                    if "status" in show.json():
                        profile = requests.get("https://api.twitter.com/2/timeline/profile/" + str(show.json()["id"]) +".json?include_tweet_replies=1&include_want_retweets=0&include_reply_count=1&count=1000", headers=self.headers)

                        if adaptive.json()['globalObjects']['tweets']:
                            pass
                        else:
                            search_ban = True

                        if typeahead.json()["num_results"] == 0:
                            search_suggestion_ban = True

                        for i in profile.json()["globalObjects"]["tweets"]:
                            for _ in profile.json()["globalObjects"]["tweets"][i]:
                                if _ == "in_reply_to_status_id_str":
                                    conversation = requests.get("https://api.twitter.com/2/timeline/conversation/" + str(profile.json()["globalObjects"]["tweets"][i]["in_reply_to_status_id_str"]) + ".json?include_reply_count=1&send_error_codes=true&count=20", headers=self.headers)
                                    if conversation.status_code == 404:
                                        ghost_ban = True
                                        reply_deboosting = True
                                    else:
                                        deboosting_l = []
                                        for i in conversation.json()["globalObjects"]["tweets"]:
                                            deboosting_l.append(conversation.json()["globalObjects"]["tweets"][i]["user_id_str"])
                                        if str(show.json()["id"]) in deboosting_l:
                                            pass
                                        else:
                                            reply_deboosting = True
                                    break
                            else:
                                continue
                            break

                    else:
                        no_tweet = True
                else:
                    protect = True

        else:
            raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")

        return {'no_tweet':no_tweet, 'protect':protect, 'suspend':suspend, 'not_found':not_found, 'search_ban':search_ban, 'search_suggestion_ban':search_suggestion_ban, 'ghost_ban':ghost_ban, 'reply_deboosting':reply_deboosting}

###ログインありアカウント操作###

class API(Client):
    ua = UserAgent()

    def __init__(self, auth):

        self.headersss = {
            'origin': 'https://twitter.com',
            'cookie': 'auth_token=' + auth["auth_token"] + '; ct0=' + auth["ct0"],
            'User-Agent': API.ua.random
        }

        self.headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-csrf-token': auth["ct0"],
            'cookie': 'auth_token=' + auth["auth_token"] + '; ct0=' + auth["ct0"],
            'User-Agent': API.ua.random
        }

        self.headerss = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-csrf-token': auth["ct0"],
            'content-type': 'application/json',
            'cookie': 'auth_token=' + auth["auth_token"] + '; ct0=' + auth["ct0"],
            'User-Agent': API.ua.random
        }

    def Login(session_u, session_p):
        response = requests.get('https://twitter.com/account/begin_password_reset')
        soup = BeautifulSoup(response.text, "lxml")
        authenticity = soup.find(attrs={'name':'authenticity_token'}).get('value')

        headers = {
            'cookie': '_mb_tk=' + authenticity,
            'User-Agent': API.ua.random
        }
        
        data = {
          'redirect_after_login': '/',
          'remember_me': '1',
          'authenticity_token': authenticity,
          'session[username_or_email]': session_u,
          'session[password]': session_p
        }
        
        response = requests.post('https://twitter.com/sessions', headers=headers, data=data, allow_redirects=False)
        print(BeautifulSoup(response.text, "html.parser"))
        auth_token = response.cookies.get_dict()["auth_token"]

        response = requests.get('https://twitter.com/i/release_notes')
        ct0 = response.cookies.get_dict()["ct0"]

        return {'auth_token':auth_token, 'ct0':ct0}

    def generate_ct0(self):
        response = requests.get('https://twitter.com/i/release_notes')
        ct0 = response.cookies.get_dict()["ct0"]

        return ct0

    def generate_authenticity(self):
        response = requests.get('https://twitter.com/account/begin_password_reset')
        soup = BeautifulSoup(response.text, "lxml")
        authenticity_token = soup.find(attrs={'name':'authenticity_token'}).get('value')

        return authenticity_token

    def generate_token(self):
        headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'User-Agent': API.ua.random
        }
        response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers).json()

        return response

    def user_info(self, screen_name=None, user_id=None):
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                response = requests.get('https://api.twitter.com/1.1/users/show.json?user_id=' + user_id, headers=self.headers).json()
        else:
            response = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screen_name, headers=self.headers).json()

        return response

    def user_tweets(self, screen_name=None, user_id=None):
        params = (
            ('userId', user_id),
        )
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                response = requests.get('https://api.twitter.com/2/timeline/profile/' + user_id + '.json', headers=self.headers, params=params).json()
        else:
            user_id = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screen_name, headers=self.headers).json()["id_str"]
            response = requests.get('https://api.twitter.com/2/timeline/profile/' + user_id + '.json', headers=self.headers, params=params).json()

        return response

    def trend(self):
        response = requests.get('https://twitter.com/i/api/2/guide.json', headers=self.headers).json()

        return response

    def searchbox(self, text):
        params = (
            ('q', text),
            ('src', 'search_box'),
        )
        response = requests.get('https://twitter.com/i/api/1.1/search/typeahead.json', headers=self.headers, params=params).json()

        return response

    def topic_search(self, text):
        params = (
            ('q', text),
            ('tweet_search_mode', 'extended'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def latest_search(self, text):
        params = (
            ('q', text),
            ('tweet_search_mode', 'live'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def image_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'image'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def video_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'video'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def user_search(self, text):
        params = (
            ('q', text),
            ('tweet_mode', 'extended'),
            ('result_filter', 'user'),
        )
        response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=self.headers, params=params).json()

        return response

    def screenname_available(self, id):
        params = (
            ('username', id),
        )
        response = requests.get('https://twitter.com/i/api/i/users/username_available.json', headers=self.headers, params=params).json()

        return response

    def get_status(self, tweetid):
        response = requests.get('https://api.twitter.com/2/timeline/conversation/' + tweetid + '.json', headers=self.headers).json()

        return response


    def update_status(self, text, conversation_control=None, in_reply_to_status_id=None, card_uri=None):
         if in_reply_to_status_id == None:
             if conversation_control == None:
                 if card_uri == None:
                     data = {
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 1:
                 if card_uri == None:
                     data = {
                       'conversation_control': 'community',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                         'conversation_control': 'community',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 2:
                 if card_uri == None:
                     data = {
                       'conversation_control': 'by_invitation',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                         'conversation_control': 'by_invitation',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

         elif not in_reply_to_status_id == None:
             if conversation_control == None:
                 if card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'card_uri': card_uri,
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 1:
                 if card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'community',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'community',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

             elif conversation_control == 2:
                 if card_uri == None:
                     data = {
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'by_invitation',
                       'status': text
                     }
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()
                 elif not card_uri == None:
                     data = {
                       'card_uri': card_uri,
                       'auto_populate_reply_metadata': 'true',
                       'in_reply_to_status_id': in_reply_to_status_id,
                       'conversation_control': 'by_invitation',
                       'status': text
                     }
                     
                     response = requests.post('https://twitter.com/i/api/1.1/statuses/update.json', headers=self.headers, data=data).json()

         return response
    
    def get_dm(self):

        response = requests.get('https://twitter.com/i/api/1.1/dm/inbox_initial_state.json', headers=self.headers).json()

        return response
    
    def send_dm(self, text, screen_name=None, user_id=None):
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                data = {
                  'recipient_ids': user_id,
                  'text': text
                }

                response = requests.post('https://twitter.com/i/api/1.1/dm/new.json', headers=self.headers, data=data).json()

        else:
            response = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + screen_name, headers=self.headers).json()
            data = {
                'recipient_ids': response['id'],
                'text': text
            }

            response = requests.post('https://twitter.com/i/api/1.1/dm/new.json', headers=self.headers, data=data).json()

        return response
    
    def delete_dm(self, conversation_id_1=None, conversation_id_2=None):
        response = requests.post('post https://twitter.com/i/api/1.1/dm/conversation/' + int(conversation_id_1) + '-' + int(conversation_id_2) + '/delete.json', headers=self.headers).json()
        return response

    def destroy_status(self, id):
         data = {
           'id': id
         }
         response = requests.post('https://twitter.com/i/api/1.1/statuses/destroy.json', headers=self.headers, data=data).json()

         return response

    def create_favorite(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/favorites/create.json', headers=self.headers, data=data).json()

        return response

    def destroy_favorite(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/favorites/destroy.json', headers=self.headers, data=data).json()

        return response

    def retweet(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/statuses/retweet.json', headers=self.headers, data=data).json()

        return response

    def unretweet(self, id):
        data = {
          'id': id
        }
        response = requests.post('https://twitter.com/i/api/1.1/statuses/unretweet.json', headers=self.headers, data=data).json()

        return response

    def create_friendship(self, screen_name=None, user_id=None):
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                data = {
                  'id': user_id
                }

                response = requests.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=self.headers, data=data).json()

        else:
            data = {
              'screen_name': screen_name
            }

            response = requests.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=self.headers, data=data).json()

        return response

    def destroy_friendship(self, screen_name=None, user_id=None):
        if screen_name == None:
            if user_id == None:
                raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")
            else:
                data = {
                  'id': user_id
                }

                response = requests.post('https://twitter.com/i/api/1.1/friendships/destroy.json', headers=self.headers, data=data).json()

        else:
            data = {
              'screen_name': screen_name
            }

            response = requests.post('https://twitter.com/i/api/1.1/friendships/destroy.json', headers=self.headers, data=data).json()

        return response

    def notifications(self):
        response = requests.get('https://twitter.com/i/api/2/notifications/all.json', headers=self.headers).json()

        return response

    def pin_tweet(self, id):
        data = {
          'id': id
        }

        response = requests.post('https://twitter.com/i/api/1.1/account/pin_tweet.json', headers=self.headers, data=data).json()

        return response

    def unpin_tweet(self, id):
        data = {
          'id': id
        }

        response = requests.post('https://twitter.com/i/api/1.1/account/unpin_tweet.json', headers=self.headers, data=data).json()

        return response

    def change_id(self, id):
        data = {
          'screen_name': id
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        return response

    def private(self, protected):
        if not protected.lower() in ["true", "false"]:
            raise TwitterError("""Please enter "true" or "false".""")
        elif protected.lower() in ["true", "false"]:
            data = {
              'protected': protected
            }
            
            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        return response

    def gender(self, gender):
        if gender.lower() in ["female", "male"]:
            data = '{"preferences":{"gender_preferences":{"use_gender_for_personalization":true,"gender_override":{"type":"' + gender.lower() + '","value":"' + gender.lower() + '"}}}}'

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()
        else:
            data = '{"preferences":{"gender_preferences":{"use_gender_for_personalization":true,"gender_override":{"type":"custom","value":"' + gender.lower() + '"}}}}'

        return response

    def protect_password_reset(self, password, protect=None):
        if protect.lower() in ["true", "false"]:
            data = {
              'protect_password_reset': protect,
              'current_password': password
            }
            
            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def session_revoke(self, hashed_token):
        data = {
          'hashed_token': hashed_token
        }
        
        response = requests.post('https://twitter.com/i/api/account/sessions/revoke', headers=self.headers, data=data).json()

        return response

    def sessions_revoke_all(self):

        response = requests.post('https://twitter.com/i/api/account/sessions/revoke_all', headers=self.headers).json()

        return response

    def allow_media_tagging(self, allow_level):
        if allow_level.lower() in ["all", "following", "none"]:
            data = {
              'allow_media_tagging': allow_level.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "all" or "following" or "none".""")

        return response

    def nsfw(self, nsfw):
        if nsfw.lower() in ["true", "false"]:
            data = {
              'nsfw_user': nsfw.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def geo_enabled(self, geo):
        if geo.lower() in ["true", "false"]:
            data = {
              'geo_enabled': geo.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def geo_delete(self):
        response = requests.post('https://twitter.com/i/api/1.1/geo/delete_location_data.json', headers=self.headers).json()

        return response

    def display_sensitive_media(self, display):
        if display.lower() in ["true", "false"]:
            data = {
              'display_sensitive_media': display.lower()
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/settings.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("""Please enter "true" or "false".""")

        return response

    def twitter_interests(self):
        response = requests.get('https://twitter.com/i/api/1.1/account/personalization/twitter_interests.json', headers=self.headers).json()

        return response

    def set_explore(self, places):
        if places.lower() in ["true", "false"]:
            data = {
              'use_current_location': places.lower()
            }

            response = requests.post('https://twitter.com/i/api/2/guide/set_explore_settings.json', headers=self.headers, data=data).json()

        else:
            data = {
              'places': places
            }

            response = requests.post('https://twitter.com/i/api/2/guide/set_explore_settings.json', headers=self.headers, data=data).json()

        return response

    def topic_follow(self, id):
        data = '{"variables":"{\\"topicId\\":\\"' + id + '\\"}"}'

        response = requests.post('https://twitter.com/i/api/graphql/4cBaE5ehyzJ1xr5-AoT5cw/TopicFollow', headers=self.headerss, data=data).json()

        return response

    def topic_unfollow(self, id):
        data = '{"variables":"{\\"topicId\\":\\"' + id + '\\"}"}'

        response = requests.post('https://twitter.com/i/api/graphql/v4k95ijrXpxhwGdTWWNc9g/TopicUnfollow', headers=self.headerss, data=data).json()

        return response

    def followed_topics(self, id):
        params = (
            ('variables', '{"userId":"' + id + '"}'),
        )

        response = requests.get('https://twitter.com/i/api/graphql/sXXi7qCBNBIXxhMLXpMFgQ/FollowedTopics', headers=self.headerss, params=params).json()

        return response

    def not_interested_topics(self):
        response = requests.get('https://twitter.com/i/api/graphql/IynHqLeaa4Xm0TT7JuIZZg/NotInterestedTopics', headers=self.headerss).json()

        return response

    def recommendations(self):
        response = requests.get('https://twitter.com/i/api/1.1/users/recommendations.json', headers=self.headers).json()

        return response

    def lists_all(self, id):
        params = (
            ('variables', '{"userId":"' + id + '","withTweetResult":false,"withUserResult":false}'),
        )
        
        response = requests.get('https://twitter.com/i/api/graphql/zpuJN3UciLfyrdIK-6zuHA/CombinedLists', headers=self.headerss, params=params).json()

        return response

    def create_list(self, name, private="False", description=""):
        data = '{"variables":"{\\"isPrivate\\":' + private.lower() + ',\\"name\\":\\"' + name + '\\",\\"description\\":\\"' + description + '\\",\\"withUserResult\\":false}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/uUTfBUYah4ct184vDaV2KA/CreateList', headers=self.headerss, data=data).json()

        return response

    def destroy_list(self, id):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\"}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/UnN9Th1BDbeLjpgjGSpL3Q/DeleteList', headers=self.headerss, data=data).json()

        return response

    def update_list(self, id, name="", private="False", description=""):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\",\\"isPrivate\\":' + private.lower() + ',\\"description\\":\\"' + description + '\\",\\"name\\":\\"' + name + '\\",\\"withUserResult\\":false}"}'

        response = requests.post('https://twitter.com/i/api/graphql/9CCuAshk9gX5ceEMhc2H5A/UpdateList', headers=self.headerss, data=data).json()

        return response

    def add_list_member(self, id, user_id):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\",\\"userId\\":\\"' + user_id + '\\",\\"withUserResult\\":false}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/1PeyBdMyCv1GtFn10VNL-g/ListAddMember', headers=self.headerss, data=data).json()

        return response

    def remove_list_member(self, id, user_id):
        data = '{"variables":"{\\"listId\\":\\"' + id + '\\",\\"userId\\":\\"' + user_id + '\\",\\"withUserResult\\":false}"}'
        
        response = requests.post('https://twitter.com/i/api/graphql/DsE0uIywHZ52-Itoq2dhSw/ListRemoveMember', headers=self.headerss, data=data).json()

        return response

    def list_members(self, id):
        params = (
            ('variables', '{"listId":"' + id + '","withTweetResult":false,"withUserResult":false}'),
        )
        
        response = requests.get('https://twitter.com/i/api/graphql/l7oY9paKsUYC1IWil9PF_w/ListMembers', headers=self.headerss, params=params).json()

        return response

    def create_card(self, quantity, minutes, one="Hello", two="World", three="!", four="byPython"):
        if quantity == 2:
            data = {
              'card_data': '{"twitter:card":"poll2choice_text_only","twitter:api:api:endpoint":"1","twitter:long:duration_minutes":' + minutes + ',"twitter:string:choice1_label":"' + one + '","twitter:string:choice2_label":"' + two + '"}'
            }

            response = requests.post('https://caps.twitter.com/v2/cards/create.json', headers=self.headers, data=data).json()

        elif quantity == 3:
            data = {
              'card_data': '{"twitter:card":"poll3choice_text_only","twitter:api:api:endpoint":"1","twitter:long:duration_minutes":' + minutes + ',"twitter:string:choice1_label":"' + one + '","twitter:string:choice2_label":"' + two + '","twitter:string:choice3_label":"' + three + '"}'
            }

            response = requests.post('https://caps.twitter.com/v2/cards/create.json', headers=self.headers, data=data).json()

        elif quantity == 4:
            data = {
              'card_data': '{"twitter:card":"poll4choice_text_only","twitter:api:api:endpoint":"1","twitter:long:duration_minutes":' + minutes + ',"twitter:string:choice1_label":"' + one + '","twitter:string:choice2_label":"' + two + '","twitter:string:choice3_label":"' + three + '","twitter:string:choice4_label":"' + four + '"}'
            }

            response = requests.post('https://caps.twitter.com/v2/cards/create.json', headers=self.headers, data=data).json()

        else:
            raise TwitterError("Please specify the number of votes between 2 and 4.")

        return response

    def Twitter_Web_Client(self, text, place_id="", authenticity_token=None):
        if authenticity_token == None:
            response = requests.get('https://twitter.com/account/begin_password_reset')
            soup = BeautifulSoup(response.text, "lxml")
            authenticity_token = soup.find(attrs={'name':'authenticity_token'}).get('value')
            data = {
              'authenticity_token': authenticity_token,
              'batch_mode': 'off',
              'place_id': place_id,
              'status': text,
            }
            
            response = requests.post('https://twitter.com/i/tweet/create', headers=self.headersss, data=data).json()

        elif not authenticity_token == None:
            data = {
              'authenticity_token': authenticity_token,
              'batch_mode': 'off',
              'place_id': place_id,
              'status': text,
            }
            
            response = requests.post('https://twitter.com/i/tweet/create', headers=self.headersss, data=data).json()

        return response

    def add_bookmark(self, id):
        data = {
          'tweet_mode': 'extended',
          'tweet_id': id
        }

        response = requests.post('https://twitter.com/i/api/1.1/bookmark/entries/add.json', headers=self.headers, data=data).json()

        return response

    def mute_conversation(self, id):
        data = {
          'tweet_mode': 'extended',
          'tweet_id': id
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/mutes/conversations/create.json', headers=self.headers, data=data).json()

        return response

    def unmute_conversation(self, id):
        data = {
          'tweet_mode': 'extended',
          'tweet_id': id
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/mutes/conversations/destroy.json', headers=self.headers, data=data).json()

        return response

    def verify_password(self, password):
        data = {
          'password': password
        }
        
        response = requests.post('https://twitter.com/i/api/1.1/account/verify_password.json', headers=self.headers, data=data)

        return response.json() | response.cookies.get_dict()

    def account_data(self, verify=None, password=""):
        if verify == None:
            data = {
              'password': password
            }

            response = requests.post('https://twitter.com/i/api/1.1/account/verify_password.json', headers=self.headers, data=data)
            if "errors" in response.json():
                raise TwitterError(response.json()["errors"][0]["message"])
            elif response.json()["status"] == "ok":
                cookie = self.headers["cookie"] + '; _twitter_sess=' + response.cookies.get_dict()["_twitter_sess"]
                self.headers["cookie"] = cookie

                response = requests.get('https://twitter.com/i/api/1.1/account/personalization/p13n_data.json', headers=self.headers).json()

        elif not verify == None:
            cookie = self.headers["cookie"] + '; _twitter_sess=' + verify
            self.headers["cookie"] = cookie

            response = requests.get('https://twitter.com/i/api/1.1/account/personalization/p13n_data.json', headers=self.headers).json()

        return response

    def shadowban_check(self, screen_name=None, user_id=None):
        if not screen_name == None:
            no_tweet = False
            protect = False

            suspend = False
            not_found = False

            search_ban = False
            search_suggestion_ban = False
            ghost_ban = False
            reply_deboosting = False

            adaptive = requests.get("https://api.twitter.com/2/search/adaptive.json?q=from:" + screen_name + "&count=20&spelling_corrections=0", headers=self.headers)
            typeahead = requests.get("https://api.twitter.com/1.1/search/typeahead.json?src=search_box&result_type=users&q=" + screen_name, headers=self.headers)
            show = requests.get("https://api.twitter.com/1.1/users/show.json?screen_name=" + screen_name, headers=self.headers)

            if "errors" in show.json():
                if show.json()["errors"][0]["code"] == 63:
                    suspend = True
                elif show.json()["errors"][0]["code"] == 50:
                    not_found = True

            else:
                if show.json()["protected"] == False:
                    if "status" in show.json():
                        profile = requests.get("https://api.twitter.com/2/timeline/profile/" + str(show.json()["id"]) +".json?include_tweet_replies=1&include_want_retweets=0&include_reply_count=1&count=1000", headers=self.headers)

                        if adaptive.json()['globalObjects']['tweets']:
                            pass
                        else:
                            search_ban = True

                        if typeahead.json()["num_results"] == 0:
                            search_suggestion_ban = True

                        for i in profile.json()["globalObjects"]["tweets"]:
                            for _ in profile.json()["globalObjects"]["tweets"][i]:
                                if _ == "in_reply_to_status_id_str":
                                    conversation = requests.get("https://api.twitter.com/2/timeline/conversation/" + str(profile.json()["globalObjects"]["tweets"][i]["in_reply_to_status_id_str"]) + ".json?include_reply_count=1&send_error_codes=true&count=20", headers=self.headers)
                                    if conversation.status_code == 404:
                                        ghost_ban = True
                                        reply_deboosting = True
                                    else:
                                        deboosting_l = []
                                        for i in conversation.json()["globalObjects"]["tweets"]:
                                            deboosting_l.append(conversation.json()["globalObjects"]["tweets"][i]["user_id_str"])
                                        if str(show.json()["id"]) in deboosting_l:
                                            pass
                                        else:
                                            reply_deboosting = True
                                    break
                            else:
                                continue
                            break

                    else:
                        no_tweet = True
                else:
                    protect = True

        elif not user_id == None:

            screen_name = requests.get('https://api.twitter.com/1.1/users/show.json?user_id=' + user_id, headers=self.headers).json()["screen_name"]

            no_tweet = False
            protect = False

            suspend = False
            not_found = False

            search_ban = False
            search_suggestion_ban = False
            ghost_ban = False
            reply_deboosting = False

            adaptive = requests.get("https://api.twitter.com/2/search/adaptive.json?q=from:" + screen_name + "&count=20&spelling_corrections=0", headers=self.headers)
            typeahead = requests.get("https://api.twitter.com/1.1/search/typeahead.json?src=search_box&result_type=users&q=" + screen_name, headers=self.headers)
            show = requests.get("https://api.twitter.com/1.1/users/show.json?screen_name=" + screen_name, headers=self.headers)

            if "errors" in show.json():
                if show.json()["errors"][0]["code"] == 63:
                    suspend = True
                elif show.json()["errors"][0]["code"] == 50:
                    not_found = True

            else:
                if show.json()["protected"] == False:
                    if "status" in show.json():
                        profile = requests.get("https://api.twitter.com/2/timeline/profile/" + str(show.json()["id"]) +".json?include_tweet_replies=1&include_want_retweets=0&include_reply_count=1&count=1000", headers=self.headers)

                        if adaptive.json()['globalObjects']['tweets']:
                            pass
                        else:
                            search_ban = True

                        if typeahead.json()["num_results"] == 0:
                            search_suggestion_ban = True

                        for i in profile.json()["globalObjects"]["tweets"]:
                            for _ in profile.json()["globalObjects"]["tweets"][i]:
                                if _ == "in_reply_to_status_id_str":
                                    conversation = requests.get("https://api.twitter.com/2/timeline/conversation/" + str(profile.json()["globalObjects"]["tweets"][i]["in_reply_to_status_id_str"]) + ".json?include_reply_count=1&send_error_codes=true&count=20", headers=self.headers)
                                    if conversation.status_code == 404:
                                        ghost_ban = True
                                        reply_deboosting = True
                                    else:
                                        deboosting_l = []
                                        for i in conversation.json()["globalObjects"]["tweets"]:
                                            deboosting_l.append(conversation.json()["globalObjects"]["tweets"][i]["user_id_str"])
                                        if str(show.json()["id"]) in deboosting_l:
                                            pass
                                        else:
                                            reply_deboosting = True
                                    break
                            else:
                                continue
                            break

                    else:
                        no_tweet = True
                else:
                    protect = True

        else:
            raise TwitterError("Neither 'screen_name' nor 'user_id' was entered.")

        return {'no_tweet':no_tweet, 'protect':protect, 'suspend':suspend, 'not_found':not_found, 'search_ban':search_ban, 'search_suggestion_ban':search_suggestion_ban, 'ghost_ban':ghost_ban, 'reply_deboosting':reply_deboosting}

    def change_password(self, old, new):

        data = {
          'current_password': old,
          'password': new,
          'password_confirmation': new
        }

        response = requests.post('https://twitter.com/i/api/i/account/change_password.json', headers=self.headers, data=data).json()

        return response
