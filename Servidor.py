from http.server import HTTPServer, BaseHTTPRequestHandler
port =3000

class miServidor(BaseHTTPRequestHandler):
    def do_GET(Self):
        if Self.path=="/":
            Self.path="/index.html"
            return BaseHTTPRequestHandler.do_GET(Self) 


print("Servidor corriendo en el puerto 3000")
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()