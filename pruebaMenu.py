from multiprocessing import connection
from pickle import NONE

import os
import string
import pruebaConexion
import pruebaManager
import pruebaScripts
from colorama import Fore
from colorama import Style


def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    print ('')
    print ("1.SetCursor Opcion 1")
    print ("2.Crear Tabla 2")
    print ("3.Mostrar Tablas 3")
    print ("4.Borrar Tabla 4")
    print ("5.Crear Tabla con NOMBRE 5")
    print ('--------------------')
    print ('9.Limpiar pantalla')
    print ("10. Salir")
    print ('')
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    
    if opcion == 1:  
        print ('--')      
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


    elif opcion == 2:
       
        try:
        #crear tabla en base dblocal
            print('CREANDO TABLA EN dblocal')
            pruebaManager.EjecutarScript(pruebaConexion.dbLocal , cursorDBEjemplo , pruebaScripts.crear_TABLA_MATRICULA_NOMINAL)
            print('CREADA')
        except:
            print(f"{Fore.RED}{Style.BRIGHT}...ERROR en CREACÍON de tabla ...{Style.RESET_ALL}")

    elif opcion == 3:
        
        try:
        #mostrar tablas de dblocal
            print('MOSTRANDO TABLA/S DE dblocal')
            pruebaManager.MostrarTablaBD(pruebaConexion.dbLocal, cursorDBEjemplo)

        except:
            print(f"{Fore.RED}{Style.BRIGHT}...NO HAY TABLAS ...{Style.RESET_ALL}")

    
    elif opcion == 4:

        try:
        #eliminar tabla de base dblocal 
            print('BORRANDO TABLA DE dblocal')
            pruebaManager.EjecutarScript(pruebaConexion.dbLocal , cursorDBEjemplo , pruebaScripts.drop_TABLA_MATRICULA_NOMINAL_SiExiste)
            print('ELIMINADA')
        except:

            print(f"{Fore.RED}{Style.BRIGHT}...ERROR en eliminacion de tabla ...{Style.RESET_ALL}")

    elif opcion == 5:

        print ('Como se va a llamar la tabla? ')
        tablaNombre = input('introduce nombre tabla: ')
        pruebaScripts.crearTablaN(pruebaConexion.dbLocal, cursorDBEjemplo, pruebaScripts.crearTablaN  )

    elif opcion == 9:
        os.system ("cls")
    elif opcion == 10:    
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")