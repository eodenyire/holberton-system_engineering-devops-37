#!/usr/bin/python3
"""
Write a recursive function.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):

    try:
        json_list = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        user = {'User-Agent': 'Trollolol'}
        my_list = requests.get(json_list, headers=user, params={'after': after})
        r_sub = my_list.json().get('data').get('children')
        s_sub = my_list.json()['data'].get('after')
        for data in r_sub:
            hot_list.append(i['data'].get('title'))
        if s_sub is not None:
            recurse(subreddit, hot_list, s_sub)
        return hot_list
    except:
        return None
