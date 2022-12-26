import random
import time
import string
import sys
import wordlista
import secrets

print('\033[1;34m==\33[m'*60)
print("""
\033[0;32mEsse programa utiliza de algumas funções nativas do Python\033[m
\033[0;32mpara gerar uma senha com base em uma pseudo aleatoridade!\033[m
\033[0;32mEscolha uma das opções abaixo para gerar a sua senha:\033[m
\033[1;34m[ 1 ] - Senhas alfa númericas\033[m 
\033[1;34m[ 2 ] - Senhas diceware\033[m""")
print('\033[1;34m==\33[m'*60)

while True:
    try:
        senha = int(input('\033[1;34mDigite qual a senha que deseja gerar!\033[m: '))
        if senha == 1 or senha == 2:
            # Gera senhas alfanúmericas
            if senha == 1:
                print('\033[1;31mRecomendamos senhas com mais de 12 caracteres para maior segurança!\033[m')
                pwd_length = int(input('\033[1;36mQuantos caracteres deseja na senha\033[m: '))
                print('\033[1;36mGerando senha com {} caracteres!\033[m'.format(pwd_length))
                chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
                pwd_safe = ''
                time.sleep(1.5)
                for l in range(pwd_length):
                    pwd_safe += random.choice(chars)
                print('\033[0;49;31mA senha gerada foi\033[m: \033[0;32m{}\033[m'.format(pwd_safe))
                print('\n')
                print('\033[1;34m==\33[m' * 60)

            #Fim da geração de senha alfa númerica!
            # Gera senhas diceware
            elif senha == 2:
                f = open('lista.txt', 'r')
                conteudo = f.readlines()
                DICE_COUNT = 5
                dice_rolls = []
                word_list = []
                print('\033[1;36mGerando senha diceware!\33[m')
                passphase = int(input('\033[1;31mDigite quantas palavras terá sua senha(Recomendamos minimo de 6):\33[m '))
                print('\033[1;36mGerando senha Diceware... \33[m')
                time.sleep(1.5)
                for _ in range(passphase):
                    dice = ''.join(str(secrets.randbelow(6)+ 1 ) for _ in range (DICE_COUNT))
                    dice_rolls.append(dice)
                for i in dice_rolls:
                    for k, v in wordlista.wordlist.items():
                        if i == k:
                           word_list.append(v)
                print('\n {:=^90} \n'.format('\033[0;49;31mSenha gerada\033[m:'))
                for i in word_list:
                    print(i.lower().replace('a','4').replace('e','3').replace('o','0'), end=' ')
                final = ' '.join(word_list)
                print('\n {:=^90} \n'.format(' ').replace(' ',''))

            print('\033[1;31mDeseja gerar outra senha?\33[m')
            resposta = str(input(' ')).strip().lower()
            if resposta == 'sim':
                print('\033[1;31mRecomeçando...\33[m')
            elif resposta == 'não' or resposta == 'nao':
                sys.exit('Finalizando o programa!')
        else:
            print('\033[1;31mOpção digitada é inválida!\33[m')

    except:
        print("\033[1;31m{:=^90}\33[m".format("Valor informado não interpretado!!\33[m"))
        sys.exit('{:=^90}'.format('Finalizando o programa!'))
