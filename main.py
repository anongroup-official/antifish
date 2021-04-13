import urllib.request, urllib.parse, urllib.error
import os
import time
import threading
from colorama import Fore, Back, Style


def cls():
	os.system('clear')
def banner():

	print(Fore.GREEN + '''
	   ___          _    _ ______  _       _
	  / _ \\        | |  (_)|  ___|(_)     | |
	 / /_\\ \\ _ __  | |_  _ | |_    _  ___ | |__
	 |  _  || '_ \\ | __|| ||  _|  | |/ __|| '_ \\
	 | | | || | | || |_ | || |    | |\\__ \\| | | |
	 \\_| |_/|_| |_| \\__||_|\\_|    |_||___/|_| |_|



	  _____     _____
	 / __  \\   |  _  |
	 `' / /'   | |/' |
	   / /     |  /| |
	 ./ /___ _ \\ |_/ /
	 \\_____/(_) \\___/

	''')
	print(Fore.CYAN + "Coded by @anongroup && morally sponsored by @wannadeauth (telegram)")
	print('--------------------------------------------------------\n\n')
cls()

banner()
print(Fore.MAGENTA + ' Example: ' + Fore.WHITE + 'http://example.com/\n\n')


a = input(Fore.YELLOW + "Site: " + Fore.WHITE)
b = 0

if a[-1] != '/':
	name_file = a.replace("https://", "").replace("http://", "")
	a += '/'
	
else:
	
	name_file = a[:-1].replace("https://", "").replace("http://", "")

ok = 0
file = open('files.txt', 'r').readlines()


for line in file:
	f = line[:-1]


	try:
		urllib.request.urlretrieve(a + f + '.txt', 'core/{}.txt'.format(name_file))
		ok = 1
	except urllib.error.HTTPError:
		print(Fore.RED + 'Текстовой документ ' + f + ' не найден')
		
	try:
		urllib.request.urlretrieve(a + f + '.txt', 'core/{}.txt'.format(name_file))
		ok = 1
	except urllib.error.HTTPError:
		print(Fore.RED + 'Дата файл  ' + f + ' не найден')

	try:
		urllib.request.urlretrieve(a + f + '.log', 'core/{}.txt'.format(name_file))
		ok = 1
	except urllib.error.HTTPError:
		print(Fore.RED + 'Лог ' + f + ' не найден')

	try:
		urllib.request.urlretrieve(a + f + '.lst', 'core/{}.txt'.format(name_file))
		ok = 1
	except urllib.error.HTTPError:
		print(Fore.RED + 'Лист ' + f + ' не найден')
	try:
		urllib.request.urlretrieve(a + f + '.db', 'core/{}.db'.format(name_file))
		ok = 2
	except urllib.error.HTTPError:
		print(Fore.RED + 'База данных ' + f + ' не найдена')


	if ok == 1:
		b = ok
		print(Fore.GREEN + 'Успешно взломали фишинг!!! Файл: ' + line + "\n")
		print(Fore.GREEN + 'Выводим содержание файла: \n\n' + Fore.WHITE)
		print(Fore.YELLOW + '----------------------------------------------------------------\n\n' + Fore.WHITE)
		os.system('cat core/{}.txt'.format(name_file))
		print(Fore.YELLOW + '\n\n----------------------------------------------------------------\n')
		input(Fore.MAGENTA + 'Продолжаем искать?')	
		ok = 0
		print(Fore.CYAN + 'Сохранено в core/{}.txt'.format(name_file))
		print(Fore.BLUE + '\nПродолжаем искать... \n')
	elif ok == 2:
		b = ok

if b == 1:
	cls()
	banner()
	print(Fore.GREEN + 'Выводим содержание файла: \n\n' + Fore.WHITE)
	print(Fore.YELLOW + '----------------------------------------------------------------\n\n' + Fore.WHITE)
	os.system('cat core/{}.txt'.format(name_file))
	print(Fore.YELLOW + '\n\n----------------------------------------------------------------')
	input(Fore.GREEN + '\nУкраденная информация ^^^')

elif b == 2:
	cls()
	banner()
	print(Fore.GREEN + 'База данных сохранена в "core/{}.db"'.format(name_file))
else:
	print(Fore.BLUE + 'Ничего не найдено' + Fore.WHITE)
