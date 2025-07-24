#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """
    Returns the titles of the top ten hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'laptop:Mysubsapi/1.0.0 (by /u/NewsSuper8309)'
               } # User-Agent
    response = requests.get(url, headers=headers)   
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    return [post['data']['title'] for post in posts]
