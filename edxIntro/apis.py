# API - 3rd party services
# pretend you are a browser from where you can request data via API calls / requests
# http request librar: docs.python-requests.org
# pip install requests
# json library: docs.python.org/3/library/json.html

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# limit response to 2
response = requests.get("https://itunes.apple.com/search?entity=song&limit2&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])


