## 2. Authenticating with the API ##

# import requests

# Retrieving the /r/python subreddit's top posts for the past day
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)

# Retrieving the data as JSON 
python_top = response.json()



## 3. Getting the Most Upvoted Post ##

# Extracting the list containing all of the posts
python_top_articles = python_top["data"]["children"]

# Finding the post with the most upvotes.
most_upvotes = 0
for d in python_top_articles:
    upvotes = d["data"]["ups"]
    if upvotes > most_upvotes:
        most_upvotes = upvotes
        most_upvoted = d["data"]["id"]

## 4. Getting Post Comments ##

# Getting all of the comments on the /r/python subreddit's top post from the past day
response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

# Finding the most upvoted top-level comment in comments
# Comments is a list containing 2 elements: 0 -> original post, 1 -> comments for the original post
comments_list = comments[1]["data"]["children"]
max_upvotes = 0
for d in comments_list:
    upvotes = d["data"]["ups"]
    if upvotes > max_upvotes:
        max_upvotes = upvotes
        most_upvoted_comment = d["data"]["id"]

## 6. Upvoting a Comment ##

# Making a POST request to the /api/vote endpoint to upvote the most upvoted comment from the last point
payload = {"dir": 1, "id": "d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote", headers=headers, json=payload)
status = response.status_code