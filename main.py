import zipfile

from tqdm import tqdm 
from colorama import*

init(autoreset=True)

class Colors:
    GREEN = f"{Style.BRIGHT}{Fore.GREEN}"
    RED = f"{Style.BRIGHT}{Fore.GREEN}"
    YELLOW = f"{Style.BRIGHT}{Fore.GREEN}"
    MAGENTA = f"{Style.BRIGHT}{Fore.GREEN}"
C = Colors()

def crack_password(password_list, zip_file):
    # tracking line no. at which password is found
    obj = zipfile.ZipFile(zip_file)
    idx = 0
 
    # open file in read byte mode only as "rockyou.txt"
    # file contains some special characters and hence
    # UnicodeDecodeError will be generated
    for line in tqdm(password_list, colour='magenta'):
        for word in line.split():
            try:
                idx += 1
                obj.extractall(pwd=word)
                print(f"{C.GREEN}[ Password: {word.decode()} ]")
                return True
            except:
                continue
    print(f"{C.RED}[ Password Not Found in WORDLIST ! ]")
    return False
 
 
password_file = input("[ Path to rockyou.txt or wordlist ]: ")
zip_file = input("[ Path to ZIP file ]: ")


# count of number of words present in file
wordlist = open(f"{password_file}", 'rb').readlines()
 
print(f"{C.YELLOW}[ Passwords to test: {len(wordlist):,} ]")
 
crack_password(wordlist, zip_file)
