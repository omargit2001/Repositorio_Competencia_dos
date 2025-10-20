import pickle
from dataclasses import dataclass
from io_archivos import leer_csv, escribir_csv
from busquedas_ordenamientos import buscar_lineal
from reportes import Reportes

@dataclass
class Producto:
    codigo: str
    nombre: str
    precio: float
    stock: int
    stock_minimo: int
    vendidos_hoy: int = 0

class Kiosko:
    def __init__(self):
        self.productos: list[Producto] = []
        self.archivo_csv = "datos.csv"
        self.archivo_bin = "datos.bin"
        self.reporte = Reportes(self)

    def cargar_datos(self):
        datos = leer_csv(self.archivo_csv)
        if not datos:
            print("No se encontró archivo CSV. Creando productos demo...")
            self.crear_demo()
            self.guardar_datos()
        else:
            self.productos = datos
            print(f"Se cargaron {len(self.productos)} productos.")

    def guardar_datos(self):
        escribir_csv(self.archivo_csv, self.productos)
        with open(self.archivo_bin, "wb") as f:
            pickle.dump(self.productos, f)
        print("Datos guardados en CSV y binario.")

    def crear_demo(self):
        self.productos = [
            Producto("A1-001", "Regla", 6.5, 20, 5),
            Producto("B1-010", "Hojas", 8.0, 12, 4),
            Producto("C2-200", "Lapiz", 7.0, 25, 6),
            Producto("D3-005", "Borrador", 5.0, 15, 3),
            Producto("E5-300", "Tijera", 12.0, 10, 2),
        ]

    def registrar_producto(self):
        codigo = input("Código: ").strip()
        if self.buscar_producto(codigo):
            print("Ya existe un producto con ese código.")
            return
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        stock_min = int(input("Stock mínimo: "))
        nuevo = Producto(codigo, nombre, precio, stock, stock_min)
        self.productos.append(nuevo)
        print("Producto registrado correctamente.")

    def modificar_producto(self):
        codigo = input("Código del producto a modificar: ").strip()
        prod = self.buscar_producto(codigo)
        if not prod:
            print("Producto no encontrado.")
            return
        nombre = input(f"Nuevo nombre ({prod.nombre}): ").strip() or prod.nombre
        precio = input(f"Nuevo precio ({prod.precio}): ").strip()
        if precio: prod.precio = float(precio)
        stock = input(f"Nuevo stock ({prod.stock}): ").strip()
        if stock: prod.stock = int(stock)
        prod.nombre = nombre
        print("Producto actualizado.")

    def eliminar_producto(self):
        codigo = input("Código a eliminar: ").strip()
        prod = self.buscar_producto(codigo)
        if prod:
            self.productos.remove(prod)
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def registrar_venta(self):
        codigo = input("Código de producto: ").strip()
        prod = self.buscar_producto(codigo)
        if not prod:
            print("Producto no encontrado.")
            return
        cantidad = int(input("Cantidad vendida: "))
        if cantidad > prod.stock:
            print("No hay suficiente stock.")
            return
        prod.stock -= cantidad
        prod.vendidos_hoy += cantidad
        print(f"Venta registrada: {cantidad} × {prod.nombre}")

    def buscar_producto(self, codigo: str):
        return buscar_lineal(self.productos, codigo)

    def reporte_top3(self):
        self.reporte.mostrar_top3()

    def reporte_bajo_stock(self):
        self.reporte.mostrar_bajo_stock()

    def reporte_economico(self):
        self.reporte.mostrar_reporte_economico()

    def reporte_semanal(self):
        self.reporte.mostrar_reporte_semanal()
