from kiosko import Kiosko

def mostrar_menu():
    print("\n===== MENU KIOSKO UNIVERSITARIO =====")
    print("1. Registrar nuevo producto")
    print("2. Modificar producto")
    print("3. Eliminar producto")
    print("4. Registrar venta")
    print("5. Reporte: top 3 más vendidos")
    print("6. Reporte: productos bajo stock mínimo")
    print("7. Reporte: ticket promedio y monto total")
    print("8. Guardar y salir")
    print("0. Salir sin guardar")

def principal():
    kiosko = Kiosko()
    kiosko.cargar_datos()  # desde datos.csv o crear demo

    while True:
        mostrar_menu()
        op = input("Seleccione una opción: ").strip()

        if op == "0":
            print("Saliendo sin guardar...")
            break
        elif op == "1":
            kiosko.registrar_producto()
        elif op == "2":
            kiosko.modificar_producto()
        elif op == "3":
            kiosko.eliminar_producto()
        elif op == "4":
            kiosko.registrar_venta()
        elif op == "5":
            kiosko.reporte_top3()
        elif op == "6":
            kiosko.reporte_bajo_stock()
        elif op == "7":
            kiosko.reporte_economico()
        elif op == "8":
            kiosko.guardar_datos()
            print("Datos guardados correctamente. Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if _name_ == "_main_":
    principal()
