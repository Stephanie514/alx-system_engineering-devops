#!/usr/bin/python3
"""
Module for count_words function
"""
import requests


def count_words(subreddit, search_words, new_after='', word_count={}):
    """
    This writes a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords
    """

    search_words = list(map(lambda x: x.lower(), search_words))

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={'User-Agent': 'Custom'},
        params={'after': new_after},
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    try:
        data = response.json().get('data', None)
        if data is None:
            return
    except ValueError:
        return

    children = data.get('children', [])

    for post in children:
        title = post.get('data', {}).get('title', '')
        for search_word in search_words:
            for word in title.lower().split():
                if search_word == word:
                    word_count[search_word] = word_count.get(search_word, 0) + 1

    new_after = data.get('after', None)

    if new_after is None:
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda x: x[1],
                                   reverse=True)

        for word, count in sorted_word_count:
            if count != 0:
                print(f"{word}: {count}")

        return

    return count_words(subreddit, search_words, new_after, word_count)


count_words('your_subreddit', ['word1', 'word2'])
