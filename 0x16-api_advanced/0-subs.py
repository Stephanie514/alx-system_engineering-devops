#!/usr/bin/python3
"""
Get the number of subscribers for a given subreddit.
"""

import requests

REDDIT_API_URL = "https://www.reddit.com/r/{}/about.json"
HEADERS = {'User-Agent': 'Mozilla/5.0'}


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    """
    url = REDDIT_API_URL.format(subreddit)

    try:
        response = requests.get(url, headers=HEADERS, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        return data['data']['subscribers']

    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0


subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
