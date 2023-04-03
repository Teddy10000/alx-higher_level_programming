#!/usr/bin/python3
import sys
import requests

"""A python scripts that sends a request
to the url and displays the body response"""

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    status_code = r.status_code
    if status_code >= 400:
        print(f"Error code: {status_code}")
