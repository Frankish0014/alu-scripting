#!/usr/bin/python3

import sys
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    :param subreddit: The name of the subreddit (without the 'r/' prefix).
    :return: The number of subscribers or None if the subreddit does not exist.
    
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'laptop:Mysubsapi/1.0.0 (by /u/NewsSuper8309)'}
    response = requests.get(url, headers=headers)
    sub = response['data']['subscribers']
    
    if response.status_code !=200:
        return sub
    return 0

if __name__ == "_main__":
    number_of_subscribers("python")
