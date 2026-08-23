#!/usr/bin/python3
"""
Contains top_ten function to query Reddit API for hot post titles.
"""
import requests


def top_ten(subreddit):
    """Prints titles of top 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/111.0.0.0 Safari/537.36'
    }
    params = {'limit': 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            print("None")
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            print("None")
            return

        for post in children:
            print(post.get('data', {}).get('title'))
    except Exception:
        print("None")
