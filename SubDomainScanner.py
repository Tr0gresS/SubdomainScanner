import requests
from colorama import Fore, init
import os

init()
class SubdomainScanner(object):
    def __init__(self):
        print(Fore.BLUE+"""

 ___________        _____                                 
/  ___| ___ \      /  ___|                                
\ `--.| |_/ /______\ `--.  ___ __ _ _ __  _ __   ___ _ __ 
 `--. \ ___ \______|`--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
/\__/ / |_/ /      /\__/ / (_| (_| | | | | | | |  __/ |   
\____/\____/       \____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                                   
                                                                                     
        """, Fore.RESET)
        print(Fore.LIGHTYELLOW_EX+"[-] Url Adresi exp(https://www.google.com) : ", end=""+Fore.RESET)
        self.url = input()
        print(Fore.LIGHTYELLOW_EX+"[-] Wordlist dosya adı yada yolu : ", end=""+Fore.RESET)
        self.wordlist = input()
        print("\n")


    def FindDomain(self, url):
        try:
            return (url.split("//www.")[1].split("/")[0])
        except IndexError:
            try:
                return (url.split("//")[1].split("/")[0])
            except IndexError:
                return False

    def ScannerSB(self):
        if os.path.isfile(self.wordlist):
            with open(self.wordlist, "r", encoding="utf-8") as f:
                cursor = f.read().splitlines()
                for _ in cursor:
                    try:
                        self.T_url = f"{self.url.split('//')[0]}//{_}.{self.FindDomain(self.url)}"
                        self.req = requests.get(self.T_url)
                    except requests.ConnectionError:
                        ...
                    else:

                        print(Fore.GREEN+"[-] Subdomain Bulundu : ", Fore.LIGHTRED_EX+"[ "+self.T_url+" ]"+Fore.RESET)

        else:
            print(Fore.RED+"Dosya Yolu Hatalı")


if __name__ == "__main__":
    S = SubdomainScanner()
    S.ScannerSB()
