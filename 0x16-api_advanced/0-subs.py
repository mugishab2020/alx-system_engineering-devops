#!/usr/bin/python3
"""Quering Reddit"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive no of subscribers"""

    headers = {"User-Agent": "Edson/1.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        try:

            data = response.json()
            subscribers = len(data)
            return (subscribers)
        except (KeyError, ValueError):
            return (0)

    else:
        return (0)