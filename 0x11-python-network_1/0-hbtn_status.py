 #!usr/bin/python3

"""
A script that fetches the alx intranet/status
"""

import urllib

if __name__ == '__main__':
    
          requests = urllib.request.Request("https://alx-intranet.hbtn.io/status")

          with urllib.request.urlopen(requests) as response:
             message = response.read()
             print(format(message))
             print(f"Body response:")
             print(f"\t -type: {format(type(message))}")
             print(f"\t - content: {message}")
             print(f"\t - utf8 content: {message.decode('utf-8')}")
