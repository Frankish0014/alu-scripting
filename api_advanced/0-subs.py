#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    :param subreddit: The name of the subreddit (without the 'r/' prefix).
    :return: The number of subscribers if the subreddit exists, otherwise 0.
    
    This function queries the Reddit API and handles invalid subreddit names
    by returning 0. It does not follow redirects.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'laptop:Mysubsapi/1.0.0 (by /u/NewsSuper8309)'}
    
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    print(number_of_subscribers("python"))
