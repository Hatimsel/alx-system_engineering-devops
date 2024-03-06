#!/usr/bin/python3
"""
Requests reddit api
"""
import requests


def count_words(subreddit, word_list, after='', words=None):
    if words is None:
        words = {word.lower(): 0 for word in word_list}

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/119.0.0.0 Safari/537.36 (by/u/Hatim)"}
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url_params = f"?limit=100&after={after}"
    url = base_url + url_params

    req = requests.get(url, allow_redirects=False, headers=headers)
    if req.status_code != 200:
        return None

    data = req.json()['data']
    after = data.get('after', None)
    children = data.get('children', [])

    for child in children:
        title = child['data']['title'].lower()
        for word in words:
            if word in title:
                words[word] += 1

    if after:
        count_words(subreddit, word_list, after, words)

    else:
        sorted_dict = sorted(words.items(), key=lambda x: x[1], reverse=True)
        for word, number_of_occurrences in sorted_dict:
            print(f"{word}: {number_of_occurrences}")

