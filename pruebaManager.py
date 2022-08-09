import mysql.connector

# Set cursor para cada base
def SetCursor(db):
    print("...poniendo el cursor en base : ", db.database)
    cursor = db.cursor()
    return cursor

def CrearTabla(db , cursor , queryCrear):
    print(f"...creando tabla en base de datos {db.database}")
    cursor.execute(queryCrear)
    db.commit()