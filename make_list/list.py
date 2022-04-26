import random , os
from termcolor import *
import sys
import string

os.system('cls||clear')
banner = """

░██╗░░░░░░░██╗███████╗██████╗░░░░░░██╗░█████╗░███████╗
░██║░░██╗░░██║██╔════╝██╔══██╗░░░░░██║██╔══██╗██╔════╝
░╚██╗████╗██╔╝█████╗░░██████╦╝░░░░░██║██║░░██║█████╗░░
░░████╔═████║░██╔══╝░░██╔══██╗██╗░░██║██║░░██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗██████╦╝╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░░╚════╝░░╚════╝░╚══════╝┛
"""
print (colored(banner,"green"))

##############################################################
# methods
##############################################################
def only_words():
    try:
        letters = string.ascii_lowercase
        words = input('How many words do you want ? \n')
        many_letters = input('How many letters do you want ? \n')
        file = input('enter file name : \n')
        for count in range(int(words)):
            try:
                character = ''.join(random.choice(letters) for i in range(int(many_letters)))
                print(f'[+] Creating word {count} [+]')
                with open(f'{file}.txt','a') as list :
                    print(character, file=list)
            except KeyboardInterrupt:
                print('done')
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()


def only_numbers():
    try:
        words = input('How many numbers do you want ? \n')
        many_letters = input('How many letters do you want ? \n')
        file = input('enter file name : \n')
        for count in range(int(words)):
            try:
                numbers = '1234567890'
                character = ''.join(random.choice(numbers) for i in range(int(many_letters)))
                print(f'[+] Creating word {count} [+]')
                with open(f'{file}.txt','a') as list :
                    print(character, file=list)
            except KeyboardInterrupt:
                print('done')
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()


def words_with_numbers():
    try:
        letters = string.ascii_lowercase
        words = input('How many words do you want ? \n')
        many_letters = input('How many letters do you want ? \n')
        file = input('enter file name : \n')
        for count in range(int(words)):
            try:
                numbers = '1234567890'
                character = ''.join(random.choice(letters + numbers) for i in range(int(many_letters)))
                print(f'[+] Creating word {count} [+]')
                with open(f'{file}.txt','a') as list :
                    print(character, file=list)
            except KeyboardInterrupt:
                print('done')
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()

def words_with_numbers_and_symbols():
    try:
        letters = string.ascii_lowercase
        words = input('How many words do you want ? \n')
        many_letters = input('How many letters do you want ? \n')
        file = input('enter file name : \n')
        for count in range(int(words)):
            try:
                numbers = '1234567890'
                symbols = '/,.<>][}{() *&^%$#+_=-!~;:\\'
                character = ''.join(random.choice(letters + numbers + symbols) for i in range(int(many_letters)))
                print(f'[+] Creating word {count} [+]')
                with open(f'{file}.txt','a') as list :
                    print(character, file=list)
            except KeyboardInterrupt:
                print('done')
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()
##############################################################


try:
    banner = """
    1- make list only words
    2- make list only numbers
    3- make list words with numbers
    4- make list words with numbers and symbols
    """
    print(banner)
    start = int(input('Choose number : \n'))
    if start == 1:
        only_words()
    if start == 2:
        only_numbers()
    if start == 3:
        words_with_numbers()
    if start == 4:
        words_with_numbers_and_symbols()
    else:
        print('enter correct number')
except KeyboardInterrupt:
    sys.exit()