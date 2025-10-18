import crud_base
from decimal import Decimal

db = crud_base.crud_base()

class crud_nota:
    def consultar_por_alumno(self, idAlumno):
        sql = f"""
            SELECT n.*, m.nombre as materia_nombre, m.codigo as materia_codigo,
                   d.nombre as docente_nombre
            FROM notas n
            JOIN materias m ON n.idMateria = m.idMateria
            LEFT JOIN docentes d ON m.idDocente = d.idDocente
            WHERE n.idAlumno = {idAlumno}
            ORDER BY m.nombre
        """
        resultado = db.consultar(sql)
        
        # Convertir Decimales a float
        notas = []
        for nota in resultado:
            nota_dict = {}
            for key, value in nota.items():
                if isinstance(value, Decimal):
                    nota_dict[key] = float(value)
                else:
                    nota_dict[key] = value
            notas.append(nota_dict)
        
        return notas
    
    def consultar_todas(self):
        sql = """
            SELECT n.*, a.nombre as alumno_nombre, a.codigo as alumno_codigo,
                   m.nombre as materia_nombre, m.codigo as materia_codigo
            FROM notas n
            JOIN alumnos a ON n.idAlumno = a.idAlumno
            JOIN materias m ON n.idMateria = m.idMateria
            ORDER BY a.nombre, m.nombre
        """
        resultado = db.consultar(sql)
        
        # Convertir Decimales a float
        notas = []
        for nota in resultado:
            nota_dict = {}
            for key, value in nota.items():
                if isinstance(value, Decimal):
                    nota_dict[key] = float(value)
                else:
                    nota_dict[key] = value
            notas.append(nota_dict)
        
        return notas
    
    def administrar(self, datos):
        # Calcular promedios de cada computo
        computo1 = (float(datos.get('lab1_c1', 0)) + float(datos.get('lab2_c1', 0)) + float(datos.get('parcial_c1', 0))) / 3
        computo2 = (float(datos.get('lab1_c2', 0)) + float(datos.get('lab2_c2', 0)) + float(datos.get('parcial_c2', 0))) / 3
        computo3 = (float(datos.get('lab1_c3', 0)) + float(datos.get('lab2_c3', 0)) + float(datos.get('parcial_c3', 0))) / 3
        
        # Calcular promedio final
        promedio_final = (computo1 + computo2 + computo3) / 3
        
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO notas (idAlumno, idMateria, 
                lab1_c1, lab2_c1, parcial_c1, computo1,
                lab1_c2, lab2_c2, parcial_c2, computo2,
                lab1_c3, lab2_c3, parcial_c3, computo3,
                promedio_final, ciclo, anio)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                datos['idAlumno'],
                datos['idMateria'],
                datos.get('lab1_c1', 0), datos.get('lab2_c1', 0), datos.get('parcial_c1', 0), computo1,
                datos.get('lab1_c2', 0), datos.get('lab2_c2', 0), datos.get('parcial_c2', 0), computo2,
                datos.get('lab1_c3', 0), datos.get('lab2_c3', 0), datos.get('parcial_c3', 0), computo3,
                promedio_final,
                datos['ciclo'],
                datos['anio']
            )
        
        elif datos['accion'] == "modificar":
            sql = """
                UPDATE notas 
                SET lab1_c1=%s, lab2_c1=%s, parcial_c1=%s, computo1=%s,
                    lab1_c2=%s, lab2_c2=%s, parcial_c2=%s, computo2=%s,
                    lab1_c3=%s, lab2_c3=%s, parcial_c3=%s, computo3=%s,
                    promedio_final=%s, ciclo=%s, anio=%s
                WHERE idNota=%s
            """
            valores = (
                datos.get('lab1_c1', 0), datos.get('lab2_c1', 0), datos.get('parcial_c1', 0), computo1,
                datos.get('lab1_c2', 0), datos.get('lab2_c2', 0), datos.get('parcial_c2', 0), computo2,
                datos.get('lab1_c3', 0), datos.get('lab2_c3', 0), datos.get('parcial_c3', 0), computo3,
                promedio_final,
                datos['ciclo'],
                datos['anio'],
                datos['idNota']
            )
        
        elif datos['accion'] == "eliminar":
            sql = "DELETE FROM notas WHERE idNota=%s"
            valores = (datos['idNota'],)
        
        return db.ejecutar(sql, valores)