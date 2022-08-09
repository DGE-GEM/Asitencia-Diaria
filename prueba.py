import mysql.connector
import pruebaScripts
from colorama import Fore
from colorama import Style


mydb = mysql.connector.connect


  print("...iniciando conector a DB dbejemplo...")
  
  dbejemplo = mydb(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="asistencia diaria"
  )
   


 