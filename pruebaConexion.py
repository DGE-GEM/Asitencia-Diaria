import mysql.connector
from colorama import Fore
from colorama import Style

mydb = mysql.connector.connect

try:
  print("...iniciando conector a DB dbejemplo...")
  dbejemplo = mydb(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="asistencia diaria"
  )
except :
  print(f"{Fore.RED}{Style.BRIGHT}...ERROR en LibConexiones.py --> en el conector dbejemplo reviselo...{Style.RESET_ALL}")
else :
  print(f"{Fore.GREEN}{Style.BRIGHT}...conector OK...{Style.RESET_ALL}")  