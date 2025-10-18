import crud_base

db = crud_base.crud_base()

class crud_alumno:
    def consultar(self, buscar=""):
        if buscar:
            sql = f"""
                SELECT * FROM alumnos 
                WHERE nombre LIKE '%{buscar}%' 
                OR codigo LIKE '%{buscar}%'
                ORDER BY nombre
            """
        else:
            sql = "SELECT * FROM alumnos ORDER BY nombre"
        
        return db.consultar(sql)
    
    def administrar(self, datos):
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO alumnos (codigo, nombre, direccion, telefono, email, dui)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (
                datos['codigo'],
                datos['nombre'],
                datos['direccion'],
                datos['telefono'],
                datos['email'],
                datos['dui']
            )
        
        elif datos['accion'] == "modificar":
            sql = """
                UPDATE alumnos 
                SET codigo=%s, nombre=%s, direccion=%s, telefono=%s, email=%s, dui=%s
                WHERE idAlumno=%s
            """
            valores = (
                datos['codigo'],
                datos['nombre'],
                datos['direccion'],
                datos['telefono'],
                datos['email'],
                datos['dui'],
                datos['idAlumno']
            )
        
        elif datos['accion'] == "eliminar":
            sql = "DELETE FROM alumnos WHERE idAlumno=%s"
            valores = (datos['idAlumno'],)
        
        return db.ejecutar(sql, valores)