import requests
import json
import subprocess
import os

url = "https://www.reddit.com/r/copypasta/random.json"

payload = ""
headers = {
    'User-agent': 'constantki'
    }

response = requests.request("GET", url, data=payload, headers=headers)

response_json = json.loads(response.text)

selftext = response_json[0]["data"]["children"][0]["data"]["selftext"]


path = os.path.abspath(__file__)[0:-13]


subprocess.call( path + "\\say.exe " + selftext.replace("\n", ' '), creationflags=subprocess.CREATE_NO_WINDOW)