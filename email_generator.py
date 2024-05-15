import requests
import string
import random
import colorama
from colorama import Fore
from bs4 import BeautifulSoup

er = Fore.RED
done = Fore.GREEN
nevim = Fore.YELLOW
blue = Fore.LIGHTBLUE_EX
ascii_color = Fore.LIGHTMAGENTA_EX

def generate_real_email():
    number = int(input(f"{blue}[/] {nevim}How many emails to generate: "))
    emails = []
    for i in range(number):
        response = requests.get("https://generator.email/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            email = soup.find('span', {'id': "email_ch_text"}).text.strip()
            emails.append(email)
            print(f"{done}[+] {nevim}Generated email:{blue} " + email)
        else:
            print(f"{er}[-] ERROR")
    return emails

def generate_fake_email():
    domain = input(f"{blue}[/] {nevim}Domain of fake emails: ")
    e = int(input(f"{blue}[/] {nevim}How many fake emails to generate: "))
    for i in range(e):
        fake_email = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print(f"{done}[+] {nevim}Generated email:{blue} {fake_email}{domain}")

ascii = r'''
made by https://github.com/epickejclovek/
                   _ _                      
                  (_) |                     
  ____ ____   ____ _| |    ____  ____ ____  
 / _  )    \ / _  | | |   / _  |/ _  )  _ \ 
( (/ /| | | ( ( | | | |  ( ( | ( (/ /| | | |
 \____)_|_|_|\_||_|_|_|   \_|| |\____)_| |_|
                         (_____|                                                     
1. Real email generator
2. Fake email generator
'''
print(ascii_color + ascii)

def hm():
    choice = input(f"{blue}[/] {nevim}Choice: ")
    if choice == "1":
        generate_real_email()
    elif choice == "2":
        generate_fake_email()
    else:
        print(f"{er}[-] {blue}Wrong choice!")
        hm()

hm()
