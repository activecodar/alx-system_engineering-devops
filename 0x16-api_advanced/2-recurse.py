#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    Args:
        after:
        subreddit:
        hot_list:

    Returns:
        None
    """
    if hot_list is None:
        hot_list = []
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(URL, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    for post in data.get('children'):
        hot_list.append(post.get('data').get('title'))
    if data.get('after') is None:
        return hot_list
    return recurse(subreddit, hot_list, data.get('after'))
