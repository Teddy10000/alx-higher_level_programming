#!/usr/bin/python3
import requests
import sys

"""A python code that fetches status using requests"""
url = sys.argv[1]
if __name__ == "__main__":
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
