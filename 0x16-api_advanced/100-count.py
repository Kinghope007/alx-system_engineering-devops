#!/usr/bin/python3
"""
A module containing a recursive function for counting occurrences of keywords in hot articles from a subreddit.
"""
import requests

BASE_URL = 'https://www.reddit.com'


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles, and counts the occurrences
    of given keywords.
    """
    if counts is None:
        counts = {}

    api_headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62')
    }
    url = f'{BASE_URL}/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(
        url, headers=api_headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            if children:
                for child in children:
                    title = child['data']['title'].lower()
                    for word in word_list:
                        word = word.lower()
                        if f' {word} ' in f' {title} ':
                            counts[word] = counts.get(word, 0) + 1
                after = data.get('after')
                if after:
                    return count_words(subreddit, word_list, after, counts)

    if counts:
        sorted_counts = sorted(
            counts.items(), key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        print(None)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
