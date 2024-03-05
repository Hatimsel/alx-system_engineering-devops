#!/usr/bin/python3
"""
Requests reddit api
"""
import requests
import sys


def top_ten(subreddit):
    """
    Takes one argument: subreddit
    Prints the titles of the first 10 hot posts
    """
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
                Chrome/119.0.0.0 Safari/537.36 (by/u/Hatim)"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    req = requests.get(url, allow_redirects=False, headers=headers)
    if req.status_code != 200:
        print(None)
        return
    for n in range(0, 11):
        js = req.json()['data']['children'][n]['data']['title']
        print(len(req.json()['data']['children']))
        # print(js)

top_ten(sys.argv[1])
