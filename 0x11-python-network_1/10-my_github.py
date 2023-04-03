#!/usr/bin/python3
"""This is a python that sends a request to github using
your credentials uses the Github API to display id by trying to get in
"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
