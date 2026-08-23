#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses titles of all hot articles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Parses titles of hot articles recursively and prints keyword occurrences.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

    if subreddit is None or not isinstance(subreddit, str):
        return

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
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title_words = child.get('data', {}).get('title', '').split()
            for word in title_words:
                clean_word = word.lower()
                if clean_word in counts:
                    counts[clean_word] += 1

        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, counts)

        filtered = {k: v for k, v in counts.items() if v > 0}
        if not filtered:
            return

        sorted_counts = sorted(
            filtered.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    except Exception:
        return
