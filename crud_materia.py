import crud_base

db = crud_base.crud_base()

class crud_materia:
    def consultar(self, buscar=""):
        if buscar:
            sql = f"""
                SELECT m.*, d.nombre as docente_nombre
                FROM materias m 
                LEFT JOIN docentes d ON m.idDocente = d.idDocente
                WHERE m.nombre LIKE '%{buscar}%' 
                OR m.codigo LIKE '%{buscar}%'
                OR d.nombre LIKE '%{buscar}%'
                ORDER BY m.nombre
            """
        else:
            sql = """
                SELECT m.*, d.nombre as docente_nombre
                FROM materias m 
                LEFT JOIN docentes d ON m.idDocente = d.idDocente
                ORDER BY m.nombre
            """
        
        return db.consultar(sql)
    
    def administrar(self, datos):
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO materias (codigo, nombre, idDocente, horario, aula)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (
                datos['codigo'],
                datos['nombre'],
                datos['idDocente'],
                datos['horario'],
                datos['aula']
            )
        
        elif datos['accion'] == "modificar":
            sql = """
                UPDATE materias 
                SET codigo=%s, nombre=%s, idDocente=%s, horario=%s, aula=%s
                WHERE idMateria=%s
            """
            valores = (
                datos['codigo'],
                datos['nombre'],
                datos['idDocente'],
                datos['horario'],
                datos['aula'],
                datos['idMateria']
            )
        
        elif datos['accion'] == "eliminar":
            sql = "DELETE FROM materias WHERE idMateria=%s"
            valores = (datos['idMateria'],)
        
        return db.ejecutar(sql, valores)