# https://www.hackinscience.org/exercises/doing-http-requests

import requests

try:
    r = requests.get("https://api.github.com/users/python")
    print(r.content)
except Exception as e:
    print("No internet connectivity.")