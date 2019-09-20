#!/usr/bin/python3
"""
How many subs
"""

import requests
import sys


def number_of_subscribers(subreddit):
    json_list = ('https://www.reddit.com/r/{}/about.json'.format(subreddit))

    req = requests.get(json_list, headers={'User-agent': 'Spencer'})

    if req.status_code == 301:
        return (0)

    sub_list = req.json().get('data', {}).get('subscribers')

    if sub_list is None:
        return (0)
    else:
        return (sub_list)
