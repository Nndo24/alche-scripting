#!/usr/bin/python3
"""Query the Reddit API and print the top 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ALX Reddit API project)"
    }
    params = {
        "limit": 10
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False,
        timeout=10
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
    except ValueError:
        print(None)
        return

    children = data.get("data", {}).get("children", [])

    for post in children[:10]:
        print(post.get("data", {}).get("title"))
