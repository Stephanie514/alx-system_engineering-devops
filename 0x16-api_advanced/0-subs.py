#!/usr/bin/python3
"subscribers count"

import requests
import time


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    elif response.status_code != 200:
        return 0
    else:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
