import pruebaConexion
from colorama import Fore
from colorama import Style


def SetCursor(db):
    print(f"{Fore.YELLOW}{Style.BRIGHT}...poniendo el cursor en base :  {db.database}{Style.RESET_ALL}")
    # defino una variable que contendrá el cursor
    cursor = ""
    try :
        print(f"{Fore.YELLOW}...seteando cursor en la base de datos {db.database}..!{Style.RESET_ALL}")
        # ejecuto un cursor
        cursor = db.cursor()
    except :
        # si hay error en el cursor
        print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (LibDBManager2.py --> SetCursor(db))... cursor no seteado para {db.database}{Style.RESET_ALL}")
    else :
        # en caso de no haber error, se devuelve un cursor
        print(f"{Fore.GREEN}{Style.BRIGHT}...CURSOR OK para la base {db.database}{Style.RESET_ALL}")
    return cursor

# verificar que la base de datos existe, en caso de que así sea devuelve un cursor (puntero) 
# y True o False en caso de que no se pudo conectar
def VerificarBD(db):
    # cuando hago la consulta para sabes si la base de datos existe, necesito guardarla en algun lugar
    resultado = ""
    # voy a devolver un cursor para cuando encuentr la base
    cursor = ""
    # devuelvo true o false por si se pudo conectar
    verifyOK = False
    # verifica que la base de datos seleccionada esté en el servidor
    try :
        print(f"{Fore.YELLOW}{Style.BRIGHT}...tratando de acceder a la base de datos {db.database}...{Style.RESET_ALL}")
        # seteo un cursor para esa base
        cursor = SetCursor(db)
        # me fijo si la base existe,..
        cursor.execute("SHOW DATABASES LIKE " + "'" + db.database + "'")
        # en caso de que exista, me va a traer un resultado
        resultado = cursor.fetchall()
    except :        
        # si el resiltado que trae no coincide con el nombre de la base de datos 
        # que he declarado en el módulo de la conexión, entonces se verifica un error
        # y devuelve false para la verificacion
        if str(resultado[0]) != str("('" + db.database + "'),"):
            print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (LibDBManager2.py --> VerificarBD(db)) no se pudo acceder a la base de datos {db.database}...{Style.RESET_ALL}")
            verifyOK = False
            cursor = None
    else :
        # en caso de que haya encontrado la base que necesesito conectarme,..
        # devuelve un mensaje y me dice que la verificación es True
        if str(resultado[0]) == str("('" + db.database + "',)"):
            print(f"{Fore.GREEN}{Style.BRIGHT}...todo OK con la base de datos {db.database}...{Style.RESET_ALL}")
            verifyOK = True
    # devuelvo la verificación True o False y el cursor
    return cursor , verifyOK      


def EjecutarScript(db , cursor , queryParajecutar):
    print(f"...ejecutando un script en la base {db.database}")
    cursor.execute(queryParajecutar)
    db.commit()

def CrearTablaEnBD(db , cursor , queryCrear):
    print(f"...creando tabla en base de datos {db.database}")
    cursor.execute(queryCrear)
    db.commit()
    return True

def MostrarTablaBD(db, cursor, queryconsulta):
    print(f"...mostrando tabla {db.database} ")
    cursor.execute(queryconsulta)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)