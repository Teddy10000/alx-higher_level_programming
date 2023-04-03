#!/usr/bin/python3

"""This is a python that searches for repo's in github
   and the various commits made by the user and the repo
"""

if __name__ == "__main__":
    import sys
    import requests
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    req = requests.get(url)
    json_commits = req.json()
    try:
        for i in range(10):
            print(f"{json_commits[i].get('sha')}:{json_commits.get('commit').get('author').get('name')}")
    except IndexError:
        pass
