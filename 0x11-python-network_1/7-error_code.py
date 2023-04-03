#!/usr/bin/python3

"""A python scripts that sends a request
to the url and displays the body response and checks the status
"""

if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    r = requests.get(url)
    status_code = r.status_code
    if status_code >= 400:
        print(f"Error code: {status_code}")
