import urllib.request as request
import urllib.parse as parse
import sys
import urllib.error as HTTPError

"""A Python code that takes in a url and displays
 the body of the response in decoded utf-8"""

if __name__ == "__main__":
    if sys.argv:
        url = sys.argv[1]

        try:
            requ = request.Request(url)
            with request.urlopen(requ) as response:
                message = response.read()
                print(message.decode('utf-8'))

        except HTTPError as e:
            print("Error code: {}".format(e.code))
