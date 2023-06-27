from termcolor import colored, cprint
import os
import requests
import json
os.system('color')
response = requests.get("https://leetcode-stats-api.herokuapp.com/diegolara93345")
text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
print(response.json()["totalSolved"])
n = 1
while n == 1:
    h = 3
