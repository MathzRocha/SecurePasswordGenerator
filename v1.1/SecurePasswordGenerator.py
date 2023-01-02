import random
import time
import string
import sys
import wordlista
import secrets

print('=='*20)
print('{:^40}'.format('Secure Password Generator'))
print('=='*20)
print("""
\033[31mChoose one of the options below\033[m
\033[31m[ A ] - Alphanumeric Passwords\033[m
\033[31m[ D ] - Diceware Passwords\033[m""")
print('=='*20)
while True:
    opc = ' '
    while opc not in 'AD':
        opc = str(input('\033[31mChone a one options [(A)lphanumeric Passwords or (D)iceware Passwords:\033[m ')).strip().upper()[0]
    if opc == 'A':
        print('==' * 20)
        print('{:^40}'.format('\033[31mYou choouse Alphanumeric Passwords!\033[m'))
        print('=='*20)
        pwd_length = int(input('\033[31mHow many characters do you want in the password:\033[m '))
        print(f'\033[31mGenerating password with {pwd_length} characters\033[m')
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
        safe_pwd = ' '
        time.sleep(1.5)
        for p in range(pwd_length):
            safe_pwd += random.choice(chars)
        print(f'\033[34mYour generated password was\033[m \033[31m{safe_pwd}\033[m')
        print('\n')
    elif opc == 'D':
        DICE_COUNT = 5
        dice_rolls = []
        word_list = []
        print('==' * 20)
        print('{:^40}'.format('\033[31mYou choouse Diceware Password!\033[m'))
        print('==' * 20)
        passphase = int(input('\033[31mEnter how many words your password will have (we recommend a minimum of 6):\033[m '))
        print('\033[31mGenerating diceware password...\033[m')
        time.sleep(1.5)
        for _ in range(passphase):
            dice = ''.join(str(secrets.randbelow(6) + 1) for _ in range(DICE_COUNT))
            dice_rolls.append(dice)
        for i in dice_rolls:
            for k, v in wordlista.wordlist.items():
                if i == k:
                    word_list.append(v)
        print('{:=^90}'.format('Generated password is:'))
        for i in word_list:
            print(f'\033[31m{i}\033[m'.lower().replace('a', '4').replace('e', '3').replace('o', '0'), end=' ')
        final = ' '.join(word_list)
        print('\n {:=^90} \n'.format(' ').replace(' ', ''))
    new = str(input('\033[34mDo you want to generate a new password? [(Y)es or (N)ot]:\033[m ')).strip().upper()[0]
    while opc not in 'AD':
        opc = str(input('\033[34mChoose a one options [A or D]:\033[m ')).strip().upper()[0]
    if new == 'N':
        break
print('\033[31m{:^40}\033[m'.format('Finished Program!'))