from termcolor import colored, cprint
import os
import requests
import json
os.system('color')

response = requests.get("https://leetcode-stats-api.herokuapp.com/diegolara93345")
print(response.json())
print("Your current total solved leetcode problems are:",colored(response.json()["totalSolved"], "red"))
print("Your current total easy solved leetcode problems are:",colored(response.json()["easySolved"], "red"))
print("Your current total medium solved leetcode problems are:",colored(response.json()["mediumSolved"], "red"))
print("Your current total hard solved leetcode problems are:",colored(response.json()["hardSolved"], "red"))
print("Your current ranking is",colored(response.json()["ranking"], "red"))
n = 1
while n == 1:
    h = 3
