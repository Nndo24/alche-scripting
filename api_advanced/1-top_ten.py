#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """Prints titles of top 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python:api_advanced:v1.0'}
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

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print("None")
