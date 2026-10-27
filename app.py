
# Nombre: Eric Railef Mansilla
# Aplicacion API-REST

import requests

# API de productos de DummyJSON
BASE_URL = "https://dummyjson.com/products"


def mostrar_respuesta(respuesta):
    # Mostrar el codigo HTTP y los datos recibidos
    print("Codigo HTTP", respuesta.status_code)

    if respuesta.text:
        print("Respuesta JSON:")
        print(respuesta.json())
    else:
        print("la respuesta no tiene datos")


# =============================
# 1. GET: CONSULTAR UN PRODUCTO
# =============================

respuesta = requests.get(
    f"{BASE_URL}/3001",
    timeout=10
)

mostrar_respuesta(respuesta)

if respuesta.ok:
    producto = respuesta.json()
    print("Producto", producto["title"])
    print("Precio", producto["price"])
    print("Categoria", producto["category"])


# ===========================
# 2. POST: CREAR UN PRODUCTO
# ===========================

print("\n POST --- crear un producto ---")

nuevo_producto = {
    "title": "Teclado mecanico gamer",
    "price": 90000,
    "description": "Teclado para juegos",
    "category": "electronics"
}

respuesta = requests.post(
    f"{BASE_URL}/add",
    json=nuevo_producto,
    timeout=10
)

mostrar_respuesta(respuesta)




# ===========================
# 3. PUT: ACTUALIZAR UN PRODUCTO
# ===========================

print("\n --- PUT: Actualizar un producto ---")

producto_actualizado = {
    "title": "Notebook para desarrollar",
    "price": 590000,
    "description": "notebook para programar",
    "category": "laptops"
}

respuesta = requests.put(
    f"{BASE_URL}/1",
    json=producto_actualizado,
    timeout=10
)

mostrar_respuesta(respuesta)
