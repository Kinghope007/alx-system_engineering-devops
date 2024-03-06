#!/usr/bin/python3
'''
A module containing a recursive function for querying the Reddit API.
'''
import requests

BASE_URL = 'https://www.reddit.com'


def recurse(subreddit, hot_list=[], after=None):
    '''
    Queries the Reddit API recursively and returns a list containing the titles
    of all hot articles for a given subreddit.
    '''
    api_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    url = f'{BASE_URL}/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=api_headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            if children:
                hot_list.extend([child['data']['title'] for child in children])
                after = data.get('after')
                if after:
                    return recurse(subreddit, hot_list, after)
            return hot_list
    return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
