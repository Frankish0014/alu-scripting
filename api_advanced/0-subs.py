#!/usr/bin/python3

"""
This module provides a function to retrieve the number of subscribers 
for a given subreddit from Reddit's API.

Function:
- number_of_subscribers(subreddit): Returns the number of subscribers 
  for the specified subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    :param subreddit: The name of the subreddit (without the 'r/' prefix).
    :return: The number of subscribers if the subreddit exists, otherwise 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'laptop:Mysubsapi/1.0.0 (by /u/NewsSuper8309)'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        sub = response.json()['data']['subscribers']
        return sub
    else:
        return 0
  
if __name__ == "__main__":
    print(number_of_subscribers("python"))
