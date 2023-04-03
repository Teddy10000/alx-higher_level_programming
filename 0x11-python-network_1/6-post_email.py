#!/usr/bin/python3
import sys
import requests

"""A python scripts that sends a post request to a url """

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    r = requests.post(url, data=data)
    print(f"Your email is: {email}")
