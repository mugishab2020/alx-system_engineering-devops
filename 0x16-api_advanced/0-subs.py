#!/usr/bin/python3
"""Quering Reddit"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive no of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    head = {'User-Agent': 'user Agent 1.0'}
    response = requests.get(url, headers=head, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        count = data.get('subscribers', 0)
        return count
    else:
        return 0
