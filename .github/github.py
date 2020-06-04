# form login buat buka github
import getpass
import webbrowser
stop = False

user = input("username : ")
pas = getpass.getpass("password : ")

if user == 'prana' and pas == '1004':
    webbrowser.open('https://github.com/prana10')
else:
    print('login failed')
    stop = True