1 #!usr/bin/python3
  2 """A script that fetches the alx intranet/status"""
  3
  4 import urllib.request
  5
  6 if __name__ == '__main__':
  7
  8         request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
  9
 10         with urllib.request.urlopen(request) as response:
 11             message = response.read()
 12             print(format(message))
 13             print(f"Body response:")
 14             print(f"\t -type: {format(type(message))}")
 15             print(f"\t - content: {message}")
 16             print(f"\t - utf8 content: {message.decode('utf-8')}")
