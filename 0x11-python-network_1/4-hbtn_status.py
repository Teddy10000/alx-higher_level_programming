#!/usr/bin/python3
import sys
import requests

"""A python code that fetches status using requests"""
url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    r = requests.get(url)
    print("Body response:")
    print("\t - type: {}".format(type(r.text)))
    print("\t - content: {}".format(r.text))
