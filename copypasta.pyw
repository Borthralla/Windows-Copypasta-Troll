import requests
import json
import subprocess

url = "https://www.reddit.com/r/copypasta/random.json"

payload = ""
headers = {
    'User-agent': 'constantki'
    }

response = requests.request("GET", url, data=payload, headers=headers)

response_json = json.loads(response.text)

selftext = response_json[0]["data"]["children"][0]["data"]["selftext"]

subprocess.call("say " + selftext.replace("\n", ' '), creationflags=subprocess.CREATE_NO_WINDOW)