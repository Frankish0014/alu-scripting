# Reddit API Subscriber Count

## Overview

This project includes a function that queries the Reddit API to return the number of subscribers for a given subreddit. The function handles invalid subreddit names by returning 0.

## Task 0: How Many Subs?

### Requirements

- **Function Prototype**: `def number_of_subscribers(subreddit)`
- The function should return the total number of subscribers for the specified subreddit.
- If an invalid subreddit is provided, the function should return 0.
- Ensure that you do not follow redirects when checking for valid subreddits.
- No authentication is necessary for most features of the Reddit API.
- To avoid errors related to "Too Many Requests," set a custom User-Agent in your requests
