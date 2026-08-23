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
    headers = {
        'User-Agent': 'linux:api_advanced_project:v1.0.0 (by /u/student_dev)'
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
