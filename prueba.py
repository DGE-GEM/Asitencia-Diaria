from multiprocessing import connection
from pickle import NONE

import pruebaConexion
import pruebaManager
import pruebaScripts
from colorama import Fore
from colorama import Style



try :
    # verificar base dblocal
    cursorDBEjemplo , verifyOk = pruebaManager.VerificarBD(pruebaConexion.dbLocal)    
    # OBLIGATORIO ESTO PARA PODE EJECUTAR CONSULTAS MUY GRANDES..!!!
    cursorDBEjemplo.execute('SET GLOBAL max_allowed_packet = 6710886400')
    cursorDBEjemplo.execute('SET GLOBAL connect_timeout = 360000')
    
    # verificar base GEM
    cursorGEM , verifyOkGEM = pruebaManager.VerificarBD(pruebaConexion.gem)
except :    
    print(f"{Fore.RED}{Style.BRIGHT}...ERROR en prueba de verificación de prueba.py ...{Style.RESET_ALL}")

#BORRAR TABLA de DBLOCAL
try:
    #eliminar tabla de base dblocal 
    print('BORRANDO TABLA DE dblocal')
    pruebaManager.EjecutarScript(pruebaConexion.dbLocal , cursorDBEjemplo , pruebaScripts.drop_TABLA_MATRICULA_NOMINAL_SiExiste)
    print('ELIMINADA')
except:
    print(f"{Fore.RED}{Style.BRIGHT}...ERROR en eliminacion de tabla ...{Style.RESET_ALL}")

#CREAR TABLA de DBLOCAL
""" try:
    #crear tabla en base dblocal
    print('CREANDO TABLA EN dblocal')
    pruebaManager.EjecutarScript(pruebaConexion.dbLocal , cursorDBEjemplo , pruebaScripts.crear_TABLA_MATRICULA_NOMINAL)
    print('CREADA')
except:
    print(f"{Fore.RED}{Style.BRIGHT}...ERROR en CREACÍON de tabla ...{Style.RESET_ALL}") """

#VERIFICAR TABLA de DBLOCAL (no esta funcionando)
""" try:
    #Verificar tablas
    print('...Verificando si existe tabla...')
    pruebaManager.VerificarTabla(pruebaConexion.dbLocal, cursorDBEjemplo)
except:
    print(f"{Fore.RED}{Style.BRIGHT}...NO HAY TABLAS para VERIFICAR ...{Style.RESET_ALL}")  """

#MOSTRAR TABLAS de DBLOCAL
try:
    #mostrar tablas de dblocal
    print('MOSTRANDO TABLA/S DE dblocal')
    pruebaManager.MostrarTablaBD(pruebaConexion.dbLocal, cursorDBEjemplo)

except:
     print(f"{Fore.RED}{Style.BRIGHT}...NO HAY TABLAS ...{Style.RESET_ALL}")


