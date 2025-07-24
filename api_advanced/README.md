# Reddit API Project

## Overview

This project includes functions that interact with the Reddit API to retrieve various types of information related to subreddits. The primary functionalities include fetching the number of subscribers for a given subreddit, retrieving the titles of the hottest posts, and counting specific keywords in post titles.

## Table of Contents

1. [Task 0: How Many Subs?](#task-0-how-many-subs)
2. [Task 1: Top Ten](#task-1-top-ten)
3. [Task 2: Recurse it!](#task-2-recurse-it)
4. [Task 3: Count it!](#task-3-count-it)
5. [Repository Information](#repository-information)
6. [License](#license)

## Task 0: How Many Subs?

### Requirements

- **Function Prototype**: `def number_of_subscribers(subreddit)`
- The function should return the total number of subscribers for the specified subreddit.
- If an invalid subreddit is provided, the function should return 0.
- Ensure that you do not follow redirects when checking for valid subreddits.
- No authentication is necessary for most features of the Reddit API.
- To avoid errors related to "Too Many Requests," set a custom User-Agent in your requests.
