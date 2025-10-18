import crud_base

db = crud_base.crud_base()

class crud_docente:
    def consultar(self, buscar=""):
        if buscar:
            sql = f"""
                SELECT d.*, COUNT(m.idMateria) as materias_asignadas
                FROM docentes d 
                LEFT JOIN materias m ON d.idDocente = m.idDocente
                WHERE d.nombre LIKE '%{buscar}%' 
                OR d.codigo LIKE '%{buscar}%'
                GROUP BY d.idDocente
                ORDER BY d.nombre
            """
        else:
            sql = """
                SELECT d.*, COUNT(m.idMateria) as materias_asignadas
                FROM docentes d 
                LEFT JOIN materias m ON d.idDocente = m.idDocente
                GROUP BY d.idDocente
                ORDER BY d.nombre
            """
        
        return db.consultar(sql)
    
    def administrar(self, datos):
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO docentes (codigo, nombre, direccion, telefono, email, dui, escalafon)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                datos['codigo'],
                datos['nombre'],
                datos['direccion'],
                datos['telefono'],
                datos['email'],
                datos['dui'],
                datos['escalafon']
            )
        
        elif datos['accion'] == "modificar":
            sql = """
                UPDATE docentes 
                SET codigo=%s, nombre=%s, direccion=%s, telefono=%s, email=%s, dui=%s, escalafon=%s
                WHERE idDocente=%s
            """
            valores = (
                datos['codigo'],
                datos['nombre'],
                datos['direccion'],
                datos['telefono'],
                datos['email'],
                datos['dui'],
                datos['escalafon'],
                datos['idDocente']
            )
        
        elif datos['accion'] == "eliminar":
            sql = "DELETE FROM docentes WHERE idDocente=%s"
            valores = (datos['idDocente'],)
        
        return db.ejecutar(sql, valores)