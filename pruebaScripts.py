drop_TABLA_MATRICULA_NOMINAL_SiExiste = """DROP TABLE IF EXISTS TABLA_MATRICULA_NOMINAL"""

crear_TABLA_MATRICULA_NOMINAL = """CREATE TABLE IF NOT EXISTS TABLA_MATRICULA_NOMINAL 
                                (Alumno_ID INT(10), 
                                DNI INT(10),
                                Apellido_Alumno VARCHAR(100),
                                Nombre_Alumno VARCHAR(100),
                                Sexo VARCHAR(45),
                                Fecha_Nacimiento DATE,
                                Edad INT(10),
                                Curso VARCHAR(45),
                                División VARCHAR(45),
                                Turno CHAR(25),
                                Modalidad VARCHAR(45),
                                Nivel VARCHAR(50),
                                Gestión VARCHAR(45),
                                Supervisión VARCHAR(150),
                                Escuela_ID INT(10),
                                CUE INT(7),
                                subcue INT(2),
                                Número_escuela VARCHAR(6),
                                Anexo INT(10),
                                Número_Anexo VARCHAR(10),
                                Nombre_Escuela VARCHAR(120),
                                Departamento VARCHAR(45),
                                Localidad VARCHAR(45),
                                zona VARCHAR(20),
                                AMBITO VARCHAR(60),
                                Regional VARCHAR(45),
                                latitud FLOAT(45),
                                longitud FLOAT(45))"""



def crearTablaN(tablaNombre):
    var = 'tablaNombre'
    CrearTablaNueva = """CREATE TABLE """ + var + """
                    (
                    id INT AUTO_INCREMENT PRIMARY KEY
                    
                    )"""

    print(CrearTablaNueva)