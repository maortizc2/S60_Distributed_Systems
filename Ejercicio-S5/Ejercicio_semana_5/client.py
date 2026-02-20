import urllib.request
import urllib.parse
import json

HOST = "http://localhost:8000"


# -------- VERSION GET ----------
def calcular_get(operacion, a, b):
    params = urllib.parse.urlencode({
        "operacion": operacion,
        "a": a,
        "b": b
    })

    url = f"{HOST}/?{params}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        print("GET Resultado:", data["resultado"])


# -------- VERSION POST ----------
def calcular_post(operacion, a, b):
    url = HOST

    data = json.dumps({
        "operacion": operacion,
        "a": a,
        "b": b
    }).encode()

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        print("POST Resultado:", data["resultado"])


if __name__ == "__main__":
    #calcular_get("sumar", 10, 5)
    calcular_post("multiplicar", 4, 3)
    #calcular_get("dividir", 10, 5)
    calcular_post("restar", 20, 8)
