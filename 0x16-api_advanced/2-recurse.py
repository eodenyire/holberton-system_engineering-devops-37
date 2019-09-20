#!/usr/bin/python3
"""
Write a recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
       returns a list containing the titles
    """
    try:
        j_list = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        usern = {'User-Agent': 'Trollolol'}
        my_list = requests.get(j_list, headers=usern, params={'after': after})
        r_sub = my_list.json().get('data').get('children')
        afters = my_list.json()['data'].get('after')
        for i in r_sub:
            hot_list.append(i['data'].get('title'))
        if afters is not None:
            recurse(subreddit, hot_list, afters)
        return hot_list
    except:
        return None
