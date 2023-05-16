#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after=None, count_dict={}):
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    params = {"limit": "100", "after": after}
    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print("Invalid subreddit or no posts found.")
        return
    
    data = response.json()
    posts = data["data"]["children"]
    
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            keyword = word.lower()
            if keyword in title and not title.startswith(keyword + '.') and not title.startswith(keyword + '!') and not title.startswith(keyword + '_'):
                count_dict[keyword] = count_dict.get(keyword, 0) + 1

    after = data["data"]["after"]
    
    if after is not None:
        count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

# Example usage:
count_words("python", ["Python", "reddit", "java"])

