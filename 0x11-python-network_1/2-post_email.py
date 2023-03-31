#!/usr/bin/python3
"""
This task takes in a url and an email in the request body
encoded and sends as parameter
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    import sys
    value = {'email': argv[2]}
    data = parse.urlencode(value).encode('utf-8')
    resp = request.Request(sys.argv[1], data)
    with request.urlopen(resp) as response:
        print(response.read().decode('utf-8'))
