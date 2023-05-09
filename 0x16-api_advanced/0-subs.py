#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    If an invalid subreddit is given, the function should return 0

    :arg subreddit: subreddit to search
    :return: number of subscribers or 0 if subreddit is invalid
    """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132\
               Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
