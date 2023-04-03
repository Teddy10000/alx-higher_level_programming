#!/usr/bin/python3

"""A python code that fetches status using requests
    and checks the header if it is an X-request-ID
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
