#!/usr/bin/python3
"""A script to take in a URL,
And display the value of a X-Request-Id variable found in the header ofthe response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
