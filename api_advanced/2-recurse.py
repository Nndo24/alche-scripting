#!/usr/bin/python3
"""
Recursively queries the Reddit API to return a list of all hot article titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing titles of all hot articles for a given subreddit,
    or None if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:api_advanced_project:v1.0.0 (by /u/student_dev)'
    }
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children and after is None:
            return None

        for child in children:
            hot_list.append(child.get('data', {}).get('title'))

        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
