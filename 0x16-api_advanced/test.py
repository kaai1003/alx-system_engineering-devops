#!/usr/bin/python3
"""test script"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://www.reddit.com/r/{}/about.json".format(sys.argv[1])
    r = requests.get(url, allow_redirects=False)
    print(r.status_code)
    dt = r.json()['data']
    print(dt.get("subscribers"))