from random import choice
import string
import os

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def banner():
    os.system("clear")
    print (colors.fg.green + '''
         _____  _____  _   _  _   _   ___   _____ 
        /  ___||  ___|| \ | || | | | / _ \ /  ___|
        \ `--. | |__  |  \| || |_| |/ /_\ \\ `--. 
        /\__/ /| |___ | |\  || | | || | | |/\__/ /
        \____/ \____/ \_| \_/\_| |_/\_| |_/\____/ 

    ''')

def create_passwords(tamanho,opcao):
    senha = ""

    opcoes = {
        "1" : string.ascii_letters,
        "2" : string.digits,
        "3" : string.ascii_letters + string.digits,
        "4" : string.ascii_letters + string.digits + string.punctuation
    }

    value = opcoes[opcao]

    for i in range(tamanho):
        senha += choice(value)  
    return senha

if __name__ == '__main__':
    banner()
    repetions = int(input(colors.fg.blue + "Quantas repetições deseja => "))
    tamanho = int(input(colors.fg.blue + "Qual o tamanho da senha você deseja => "))
    opcao = input('''
        1 - Senha só com letras \n
        2 - Senha só com números \n
        3 - Senha com letras e números \n
        4 - Senha com letras números e caracteres especiais 
        Digite a opção:
    ''')
    repetions_min = 1

    if repetions == 0:
        quit(colors.fg.red + "Têm colocar acima de 1 repetições")

    while repetions >= repetions_min:
        print(colors.fg.red +  f"Senha {repetions} => " + create_passwords(tamanho,opcao))

        repetions -=1
