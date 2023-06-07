#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Set the custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent'}

    # Send a GET request to the Reddit API
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Extract the number of subscribers from the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Invalid subreddit, return 0
        return 0

