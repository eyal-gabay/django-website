import requests

csrf = requests.get("http://127.0.0.1:80/workspace").cookies["csrftoken"]

requests.post("http://127.0.0.1:80/workspace?name=e",
              files={'file': ('file.txt', open('try6.py', 'rb'))},
              cookies={"csrftoken": csrf},
              headers={"X-CSRFToken": csrf})

