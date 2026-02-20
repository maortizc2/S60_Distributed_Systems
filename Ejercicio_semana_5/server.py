from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json

HOST = "localhost"
PORT = 8000


class CalculatorHandler(BaseHTTPRequestHandler):

    def calcular(self, operacion, a, b):
        if operacion == "sumar":
            return a + b
        elif operacion == "restar":
            return a - b
        elif operacion == "multiplicar":
            return a * b
        elif operacion == "dividir":
            if b == 0:
                return "Error: división por cero"
            return a / b
        else:
            return "Operación inválida"

    # -------- VERSION GET ----------
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)

        try:
            operacion = params["operacion"][0]
            a = float(params["a"][0])
            b = float(params["b"][0])

            resultado = self.calcular(operacion, a, b)

        except Exception as e:
            resultado = f"Error: {str(e)}"

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps({"resultado": resultado}).encode())

    # -------- VERSION POST ----------
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)

            operacion = data["operacion"]
            a = float(data["a"])
            b = float(data["b"])

            resultado = self.calcular(operacion, a, b)

        except Exception as e:
            resultado = f"Error: {str(e)}"

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps({"resultado": resultado}).encode())


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), CalculatorHandler)
    print(f"Servidor corriendo en http://{HOST}:{PORT}")
    server.serve_forever()
