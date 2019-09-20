#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
       prints the titles of the first 10 hot posts listed for a given subreddit
    """
    try:
        json_list = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        user = {'User-Agent': 'Trollolol'}
        my_list = requests.get(json_list, headers=user, params={'limit': 10})
        r_sub = my_list.json().get('data').get('children')
        for data in r_sub:
            print(data.get('data').get('title'))
    except:
        print(None)
