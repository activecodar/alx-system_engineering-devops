#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)
"""
import requests


def count_words(subreddit, word_list, after=None, counter=None):
    """
    Recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces)
    Args:
        counter:
        after:
        subreddit:
        word_list:

    Returns:
        None
    """
    if counter is None:
        counter = {}
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(URL, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        for post in data.get('children'):
            title = post.get('data').get('title')
            words = title.lower().split()
            for word in words:
                word = word.strip('.,!_')
                if word in word_list:
                    if word in counter:
                        counter[word] += 1
                    else:
                        counter[word] = 1
        if data.get('after') is not None:
            count_words(subreddit, word_list, data['after'], counter)
        else:
            sorted_counter = sorted(counter.items(),
                                    key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counter:
                print('{}: {}'.format(word, count))
    else:
        print(None)
