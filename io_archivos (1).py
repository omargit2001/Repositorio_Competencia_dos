import csv
from kiosko import Producto

def leer_csv(ruta: str):
    productos = []
    try:
        with open(ruta, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=';')
            for fila in reader:
                productos.append(
                    Producto(
                        fila['codigo'],
                        fila['nombre'],
                        float(fila['precio']),
                        int(fila['stock']),
                        int(fila['stock_minimo']),
                        int(fila.get('vendidos_hoy', 0))
                    )
                )
        return productos
    except FileNotFoundError:
        return None

def escribir_csv(ruta: str, productos: list[Producto]):
    with open(ruta, "w", newline='', encoding="utf-8") as f:
        campos = ['codigo', 'nombre', 'precio', 'stock', 'stock_minimo', 'vendidos_hoy']
        writer = csv.DictWriter(f, fieldnames=campos, delimiter=';')
        writer.writeheader()
        for p in productos:
            writer.writerow(p.__dict__)
