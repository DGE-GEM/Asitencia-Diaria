import mysql.connector
from colorama import Fore
from colorama import Style

mydb = mysql.connector.connect

try:
  print("...iniciando conector a DB GEM...")
  gem = mydb(
    host="gemdbrep1.mendoza.gob.ar",
    user="rruiz",
    password="TXE&b1t&za",
    database="gem"
)
except:
  print(f"{Fore.RED}{Style.BRIGHT}...ERROR en LibConexiones.py --> en el conector de GEM reviselo...{Style.RESET_ALL}")
else :
  print(f"{Fore.GREEN}{Style.BRIGHT}...conector GEM OK...{Style.RESET_ALL}") 


try:
  print("...iniciando conector a DB dbejemplo...")
  dbLocal = mydb(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="asistencia diaria"
  )
except :
  print(f"{Fore.RED}{Style.BRIGHT}...ERROR en LibConexiones.py --> en el conector dbejemplo reviselo...{Style.RESET_ALL}")
else :
  print(f"{Fore.GREEN}{Style.BRIGHT}...conector OK...{Style.RESET_ALL}")  

print('...fin..!!')