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
        print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (pruebaManager.py --> SetCursor(db))... cursor no seteado para {db.database}{Style.RESET_ALL}")
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

def MostrarTablaBD(db, cursor):
    print(f"...Tabla/s de {db.database} : ")
    cursor.execute("Show tables;")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

# verifica que la tabla exista dentro de la base de datos seleccionada
# devuelve un cursor y True o False en caso de que la tabla exista
""" def VerificarTabla(db , tabla):
    # verifica la existencia de una tabla dentro de una base de datos
    # que pasamos por parámteros
    # necesito el resultado para poder verificar que sea el valor que estoy buscando
    resultado = ""
    # un cursor para ejecutar el script
    cursor = ""
    # si se verifica que está, se devolverá true
    verifyOK = False
    try :
        print(f"{Fore.YELLOW}{Style.BRIGHT}...tratando de acceder a la tabla {tabla} de la base de datos {db.database}...{Style.RESET_ALL}")        
        cursor = SetCursor(db)        
        # compongo el nombre de la base de datos
        dbName = "'" + db.database + "'"
        # compongo el nombre de la tabla
        tableName = "'" + tabla + "'"
        # tengo el script para ejecutar contra la base de datos
        script = "SHOW TABLES LIKE " + tableName        
        # ejecuto el script
        cursor.execute("Show tables;")
        # ya tengo el resultado
        resultado = cursor.fetchall()
    except :
        # si el resultado es vacío, es porque la tabla no existe
        if str(resultado == ""):
            print(f"{Fore.RED}{Style.BRIGHT}...ERROR en (pruebaManager.py --> VerificarTabla(db , tabla)) no se pudo acceder a la TABLA {tabla}...{Style.RESET_ALL}")
            verifyOK = False
            cursor = None
    else :
        # si el resultado trae el nombre de la tabla que estoy buscando, entonces es porque existe la tabla
        if str(resultado[0]) == str("(" + tableName + ",)"):
            print(f"{Fore.GREEN}{Style.BRIGHT}...todo OK con la TABLA {tabla}...{Style.RESET_ALL}")
            verifyOK = True
    return cursor , verifyOK """