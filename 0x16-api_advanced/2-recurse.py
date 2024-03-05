#!/usr/bin/python3
"""
Requests reddit api
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Takes two parameters
    Call itself recursively
    Returns all the list of hot articles
    """
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
                Chrome/119.0.0.0 Safari/537.36 (by/u/Hatim)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    req = requests.get(url, allow_redirects=False, headers=headers)
    data = req.json()['data']
    after = data.get('after', None)
    children = data.get('children', [])
    for child in children:
        hot_list.append(child['data']['title'])

    if after:
        recurse(subreddit, hot_list, after)

    return host_list
