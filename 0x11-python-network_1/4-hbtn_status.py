#!/usr/bin/python3

"""A python code that fetches status using requests
   and displays the result and the text of the content
"""

if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("\t - type: {}".format(type(r.text)))
    print("\t - content: {}".format(r.text))

