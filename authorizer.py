from colorama import Fore
from colr import color
import tls_client
import os
import pystyle
import random


banner = F"""
                              _______________    __  ___      ___    ____
                             /_  __/ ____/   |  /  |/  /     /   |  /  _/
                              / / / __/ / /| | / /|_/ /_____/ /| |  / /  
                             / / / /___/ ___ |/ /  / /_____/ ___ |_/ /   
                            /_/ /_____/_/  |_/_/  /_/     /_/  |_/___/  

        """
a = [pystyle.Colors.green_to_white]
os.system("cls")
spl = banner.split("\n")
cho = random.choice(a)
for x in spl:
    print(" "  + pystyle.Colorate.Horizontal(cho, x)) 

auth_url = input ("Auth Bot Url-")

import requests, threading, time, ctypes
from colorama import Fore

count = 0 ; genStartTime = time.time()

def title():
  ctypes.windll.kernel32.SetConsoleTitleW(f'Team-Ai | Authorized: {count} Speed : {round(count / ((time.time() - genStartTime) / 60))}/m')

def get_headers(tk):
    headers = {
                "accept": "*/*",
                # "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "authorization": tk,
                "referer": "https://discord.com/channels/@me",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDA3Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYxODQyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }
    return headers


def authorize(token):
  session = tls_client.Session(client_identifier='chrome_112')
  global count
  while True:
    try:
      headers = get_headers(token)
      r = session.post(auth_url, headers=headers, json={"authorize": "true"})
      # print(r.text)
      if r.status_code in (200, 201, 204):
        if 'location' in r.text:
          location = r.json()['location']
          requests.get(location)
          print(count, Fore.MAGENTA ,f"[Success]:{Fore.LIGHTWHITE_EX} Successfully Authorized:", token[:22])
          count += 1
          title()

          break
        else:
          print(Fore.LIGHTRED_EX ,f"[ERROR]:{Fore.LIGHTWHITE_EX} Failed to Authorize:", token, r.text)
          break
      else:
        print(Fore.RED ,f"[ERROR]:{Fore.LIGHTWHITE_EX} Failed to Authorize:", token, r.text)
        break
    except Exception as e:
      print(Fore.YELLOW ,f"[ERROR]:{Fore.LIGHTWHITE_EX} Failed to Authorize:", token, e)
      if "connection" in str(e):
        time.sleep(0.5)
        continue
      else:
        break
      # return

_f = open("tokens.txt", "r").readlines()

for token in _f:
  token = token.strip()
  token = token.split(":")[2]
  time.sleep(0.01)
  threading.Thread(target=authorize, args=(token,)).start()
