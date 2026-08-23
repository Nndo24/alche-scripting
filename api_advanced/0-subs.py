#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns total subscribers for a subreddit, or 0 if invalid."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': '0x15-api_advanced:v1.0.0 (by /u/student_dev)'
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            return 0

        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except Exception:
        return 0
