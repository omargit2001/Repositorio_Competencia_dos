class Reportes:
    def __init__(self, kiosko):
        self.kiosko = kiosko
        self.ventas_semana = [[0]*3 for _ in range(7)]

    def mostrar_top3(self):
        print("\n=== Top 3 más vendidos ===")
        top = sorted(self.kiosko.productos, key=lambda p: p.vendidos_hoy, reverse=True)[:3]
        for p in top:
            print(f"{p.nombre} — {p.vendidos_hoy} unidades")

    def mostrar_bajo_stock(self):
        print("\n=== Productos bajo stock mínimo ===")
        bajos = [p for p in self.kiosko.productos if p.stock <= p.stock_minimo]
        if not bajos:
            print("Todos los productos están con stock suficiente.")
        for p in bajos:
            print(f"{p.nombre} (Stock {p.stock} / Mínimo {p.stock_minimo})")

    def mostrar_reporte_economico(self):
        total = sum(p.vendidos_hoy * p.precio for p in self.kiosko.productos)
        vendidos = sum(p.vendidos_hoy for p in self.kiosko.productos)
        promedio = total / vendidos if vendidos else 0
        print("\n=== Reporte Económico del Día ===")
        print(f"Total vendido: Bs {total:.2f}")
        print(f"Ticket promedio: Bs {promedio:.2f}")

    def mostrar_reporte_semanal(self):
        print("\n=== Reporte Semanal de Ventas ===")
        for dia in range(7):
            print(f"Día {dia+1}: {self.ventas_semana[dia]}")
