import csv, pickle
from dataclasses import dataclass

@dataclass
class Producto:
    codigo: str
    nombre: str
    precio: float
    stock: int
    stock_minimo: int
    vendidos_hoy: int = 0


class Kiosko:
    def _init_(self):
        self.productos: list[Producto] = []
        self.archivo_csv = "datos.csv"
        self.archivo_bin = "datos.bin"


    def cargar_datos(self):
        try:
            with open(self.archivo_csv, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=';')
                for fila in reader:
                    self.productos.append(Producto(
                        fila['codigo'], fila['nombre'], float(fila['precio']),
                        int(fila['stock']), int(fila['stock_minimo'])
                    ))
            print(f"{len(self.productos)} productos cargados desde CSV.")
        except FileNotFoundError:
            print("No se encontró datos.csv, creando productos de ejemplo...")
            self.crear_demo()
            self.guardar_datos()

    def guardar_datos(self):
        with open(self.archivo_csv, "w", newline='', encoding="utf-8") as f:
            campos = ['codigo','nombre','precio','stock','stock_minimo','vendidos_hoy']
            writer = csv.DictWriter(f, fieldnames=campos, delimiter=';')
            writer.writeheader()
            for p in self.productos:
                writer.writerow(p._dict_)
        with open(self.archivo_bin, "wb") as f:
            pickle.dump(self.productos, f)
        print("Datos guardados en CSV y binario.")

    def crear_demo(self):
        self.productos = [
            Producto("A1-001","Regla",6.5,20,5),
            Producto("B1-010","Hojas",8.0,12,4),
            Producto("C2-200","Lapiz",7.0,25,6),
            Producto("D3-005","Borrador",5.0,15,3),
            Producto("E5-300","Tijera",12.0,10,2)
        ]

 
    def registrar_producto(self):
        codigo = input("Código: ").strip()
        if self.buscar_producto(codigo):
            print("Error: ya existe un producto con ese código.")
            return
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        stock_min = int(input("Stock mínimo: "))
        nuevo = Producto(codigo, nombre, precio, stock, stock_min)
        self.productos.append(nuevo)
        print(f"Producto {nombre} agregado correctamente.")

    def modificar_producto(self):
        codigo = input("Código del producto a modificar: ").strip()
        prod = self.buscar_producto(codigo)
        if not prod:
            print("Producto no encontrado.")
            return
        print("Deje vacío si no desea modificar el valor.")
        nombre = input(f"Nuevo nombre ({prod.nombre}): ").strip() or prod.nombre
        precio = input(f"Nuevo precio ({prod.precio}): ").strip()
        if precio: prod.precio = float(precio)
        stock = input(f"Nuevo stock ({prod.stock}): ").strip()
        if stock: prod.stock = int(stock)
        prod.nombre = nombre
        print("Producto actualizado correctamente.")

    def eliminar_producto(self):
        codigo = input("Código del producto a eliminar: ").strip()
        prod = self.buscar_producto(codigo)
        if not prod:
            print("Producto no encontrado.")
            return
        self.productos.remove(prod)
        print(f"Producto {codigo} eliminado.")

    def registrar_venta(self):
        codigo = input("Código del producto vendido: ").strip()
        prod = self.buscar_producto(codigo)
        if not prod:
            print("Producto no encontrado.")
            return
        cantidad = int(input("Cantidad vendida: "))
        if cantidad > prod.stock:
            print("Error: no hay suficiente stock.")
            return
        prod.stock -= cantidad
        prod.vendidos_hoy += cantidad
        print(f"Venta registrada: {cantidad} × {prod.nombre} (${prod.precio}).")

    
    def buscar_producto(self, codigo: str):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None


    def reporte_top3(self):
        print("\n=== Top 3 más vendidos ===")
        top = sorted(self.productos, key=lambda p: p.vendidos_hoy, reverse=True)[:3]
        for p in top:
            print(f"{p.nombre}: {p.vendidos_hoy} unidades")

    def reporte_bajo_stock(self):
        print("\n=== Productos bajo stock mínimo ===")
        bajos = [p for p in self.productos if p.stock <= p.stock_minimo]
        if not bajos:
            print("Ningún producto bajo stock.")
        for p in bajos:
            print(f"{p.nombre} (Stock: {p.stock}, Mínimo: {p.stock_minimo})")

    def reporte_economico(self):
        total = sum(p.vendidos_hoy * p.precio for p in self.productos)
        vendidos = sum(p.vendidos_hoy for p in self.productos)
        ticket_promedio = total / vendidos if vendidos else 0
        print("\n=== Reporte Económico ===")
        print(f"Total vendido: ${total:.2f}")
        print(f"Ticket promedio: ${ticket_promedio:.2f}")
