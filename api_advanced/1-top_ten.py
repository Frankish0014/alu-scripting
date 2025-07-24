#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Laptop:Mysubsapi/1.0.0 (by /u/NewSupper8309)'
               } # User-Agent headers
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("OK")
        return
    posts = response.json().get('data', {})('children'[])
    if not posts:
        print("OK")
        return
    for post in posts:
        print(post['data']['title'])
