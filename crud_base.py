import mysql.connector
from mysql.connector import Error

class crud_base:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_academico_ugb'
            )
        except Error as e:
            print(f"Error de conexión: {e}")
            self.conexion = None
    
    def consultar(self, sql):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(sql)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Error as e:
            print(f"Error en consulta: {e}")
            return []
    
    def ejecutar(self, sql, datos):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, datos)
            self.conexion.commit()
            cursor.close()
            return "ok"
        except Error as e:
            print(f"Error al ejecutar: {e}")
            return str(e)

class crud_login(crud_base):
    def verificar(self, usuario, clave):
        try:
            resultado = self.consultar(
                f"SELECT * FROM login WHERE usuario='{usuario}' AND clave='{clave}'"
            )
            
            if len(resultado) > 0:
                return {
                    "status": "ok",
                    "rol": resultado[0]['rol'],
                    "usuario": resultado[0]['usuario']
                }
            else:
                return {
                    "status": "error",
                    "msg": "Usuario o contraseña incorrectos"
                }
        except Exception as e:
            return {
                "status": "error",
                "msg": f"Error en la base de datos: {str(e)}"
            }