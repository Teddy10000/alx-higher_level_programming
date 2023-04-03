#!/usr/bin/python3


"""A python scripts that sends a request
to the url and displays the body response of the json body if it changes
"""

if __name__ == "__main__":
    import sys
    import requests
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    req = requests.post(url, data=data)

    try:
        json_data = req.json()
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
