from termcolor import colored
import os
import requests

os.system('color')
print(colored("Welcome", "blue", attrs=["bold","dark"]))
print("Enter your leetcode username")
username = input()
try:
    response = requests.get(f"https://leetcode-stats-api.herokuapp.com/{username}")
    print("Your current total solved leetcode problems are:",colored(response.json()["totalSolved"], "cyan", attrs=["bold","dark"]))
    print("Your current total easy solved leetcode problems are:",colored(response.json()["easySolved"], "cyan", attrs=["bold","dark"]))
    print("Your current total medium solved leetcode problems are:",colored(response.json()["mediumSolved"], "cyan", attrs=["bold","dark"]))
    print("Your current total hard solved leetcode problems are:",colored(response.json()["hardSolved"], "cyan", attrs=["bold","dark"]))
    print("Your current ranking is",colored(response.json()["ranking"], "cyan"))
except:
    print(colored("ERROR INCORRECT USERNAME", "red", attrs=["bold","dark","underline"]))
# print(response.json())  

while True: 
    k=1
