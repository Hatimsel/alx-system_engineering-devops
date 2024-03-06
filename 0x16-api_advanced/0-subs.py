#!/usr/bin/python3
"""
Requests reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
    Takes one argument: subreddit
    Returns the number of subscribers
    """
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
                Chrome/119.0.0.0 Safari/537.36 (by/u/Hatim)"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    req = requests.get(url, allow_redirects=False, headers=headers)
    if req.status_code == 404:
        return 0
    js = req.json()
    js_data = js.get('data')
    subscribers = js_data.get('subscribers')
    return subscribers
