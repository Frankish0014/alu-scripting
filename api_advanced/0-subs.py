#!/usr/bin/python3
"""
function to query the 'Reddit API' and return the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
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
