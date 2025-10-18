from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
from urllib.parse import urlparse, parse_qs
import json 
import crud_base
import crud_alumno
import crud_docente
import crud_materia
import crud_nota

port = 3000

# Inicializar CRUDs
crudLogin = crud_base.crud_login()
crudAlumno = crud_alumno.crud_alumno()
crudDocente = crud_docente.crud_docente()
crudMateria = crud_materia.crud_materia()
crudNota = crud_nota.crud_nota()

class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        url_parseada = urlparse(self.path)
        path = url_parseada.path
        parametros = parse_qs(url_parseada.query)

        # Redirigir raíz al login
        if self.path == "/":
            self.path = "/modulos/login.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        # API: Login
        if path == "/api/login":
            usuario = parametros.get('usuario', [''])[0]
            clave = parametros.get('clave', [''])[0]
            resultado = crudLogin.verificar(usuario, clave)
            self._send_json_response(resultado)
            return
        
        # API: Alumnos
        if path == "/api/alumnos":
            buscar = parametros.get('buscar', [''])[0]
            alumnos = crudAlumno.consultar(buscar)
            self._send_json_response(alumnos)
            return
        
        # API: Docentes
        if path == "/api/docentes":
            buscar = parametros.get('buscar', [''])[0]
            docentes = crudDocente.consultar(buscar)
            self._send_json_response(docentes)
            return
        
        # API: Materias
        if path == "/api/materias":
            buscar = parametros.get('buscar', [''])[0]
            materias = crudMateria.consultar(buscar)
            self._send_json_response(materias)
            return
        
        # API: Notas por alumno
        if path == "/api/notas":
            idAlumno = parametros.get('idAlumno', [0])[0]
            notas = crudNota.consultar_por_alumno(idAlumno)
            self._send_json_response(notas)
            return
        
        # API: Todas las notas
        if path == "/api/todas_notas":
            notas = crudNota.consultar_todas()
            self._send_json_response(notas)
            return
        
        # Servir archivos estáticos
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        longitud = int(self.headers['Content-Length'])
        datos = self.rfile.read(longitud)
        datos = datos.decode("utf-8")
        datos = parse.unquote(datos)
        datos = json.loads(datos)
        
        # Manejar login
        if self.path == "/api/login":
            resp = crudLogin.verificar(datos['usuario'], datos['clave'])
        
        # Manejar CRUD de alumnos
        elif self.path == "/api/alumnos":
            resp = {"msg": crudAlumno.administrar(datos)}
        
        # Manejar CRUD de docentes
        elif self.path == "/api/docentes":
            resp = {"msg": crudDocente.administrar(datos)}
        
        # Manejar CRUD de materias
        elif self.path == "/api/materias":
            resp = {"msg": crudMateria.administrar(datos)}
        
        # Manejar CRUD de notas
        elif self.path == "/api/notas":
            resp = {"msg": crudNota.administrar(datos)}
        
        else:
            resp = {"status": "error", "msg": "Ruta no encontrada"}
        
        self._send_json_response(resp)
    
    def _send_json_response(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

print("=" * 60)
print("SISTEMA ACADÉMICO UGB - Servidor ejecutándose")
print("Puerto:", port)
print("URL: http://localhost:3000")
print("Usuario: admin | Contraseña: admin123")
print("=" * 60)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()