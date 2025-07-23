#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Returns the titles of the top ten hot posts for a given subreddit.
    
    :param subreddit: The name of the subreddit (without the 'r/' prefix).
    :return: A list of titles of the top ten hot posts or None if the subreddit does not exist.
    
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'laptop:Mysubsapi/1.0.0 (by /u/NewsSuper8309)'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    
    return [post['data']['title'] for post in posts]
