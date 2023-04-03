#!/usr/bin/python3

"""A python scripts that sends a post request to a url
and takes the url and sends to the email to check"""

if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    r = requests.post(url, data=data)
    print(f"Your email is: {email}")
