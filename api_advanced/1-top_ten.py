#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """Prints top 10 hot post titles for a given subreddit, or None if invalid."""
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent/1.0'}
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

        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print("None")
EOF
