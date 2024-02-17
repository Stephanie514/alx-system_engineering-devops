#!/usr/bin/python3
"""
This Prints titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
        print(None)
