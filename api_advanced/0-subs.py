#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit (without the 'r/' prefix).
    
    Returns:
    int: The number of subscribers if the subreddit exists, otherwise 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'laptop:Mysubsapi/1.0.0 (by /u/NewsSuper8309)'}
    
    # Making the request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    print(number_of_subscribers("python"))

