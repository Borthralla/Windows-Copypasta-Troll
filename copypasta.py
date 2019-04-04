import requests
import json
import os

url = "https://www.reddit.com/r/copypasta/random.json"

payload = ""
headers = {
    'User-agent': 'philbert'
    }

response = requests.request("GET", url, data=payload, headers=headers)

response_json = json.loads(response.text)

selftext = response_json[0]["data"]["children"][0]["data"]["selftext"]

os.system("say " + selftext.replace("\n", ' '))