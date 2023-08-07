#Ferramenta de ping em Python simples no Linux/Termux
#Colors Red, Green and , Blue >>> RGB
# Suporte www.wiki/python.org

import os, colorama
from colorama import *

r = '\033[7;49;31m'
rf = '\033[49;31m'
g = '\033[49;92m'
b = '\033[49;34m'
w = '\033[0;49;37m'

print (f'{r}Ocean Corporation >> ms.ping')
p = "ping"
s = input(f'{rf}[+]{w} Insira o alvo:\n>>{Fore.RED} ')
print (f'{Fore.GREEN}')
x = p + ' ' + s
os.system(x)

print (f'{r}SevenXtz{w}')
