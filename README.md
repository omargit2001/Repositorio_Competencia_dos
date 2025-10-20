# Proyecto Integrador EC2 - Kiosko Universitario UCB

##  Descripción general
Este proyecto implementa un **mini-sistema de gestión para un kiosko universitario** utilizando Programación Orientada a Objetos (POO) en Python.  
El sistema permite administrar el inventario, registrar ventas, generar reportes y guardar/recuperar datos desde archivos CSV y binarios.

Está desarrollado en base a la estructura de un proyecto anterior de POO (estacionamiento) y cumple los requisitos del documento **Proyecto Integrador EC2 (UCB)**.

---

##  Estructura del proyecto

```
kiosko_ucb/
│
├── main.py                     # Programa principal (menú de consola)
├── kiosko.py                   # Clase principal Kiosko y clase Producto
├── io_archivos.py              # Lectura/escritura en CSV y binario
├── busquedas_ordenamientos.py  # Búsquedas lineal/binaria y ordenamientos
├── reportes.py                 # Reportes económicos y semanales
└── datos.csv                   # Archivo de datos inicial o generado
```

---

##  Ejecución

1. Descomprime el archivo `EC2_Kiosko_Torrez.zip`  
2. Abre una terminal dentro de la carpeta `kiosko_ucb`
3. Ejecuta el siguiente comando:

```bash
python3 main.py
```

>  Si no existe `datos.csv`, el programa generará automáticamente productos de ejemplo.

---

##  Funcionalidades principales

### 1. Gestión de inventario
- Registrar nuevos productos  
- Modificar datos (precio, nombre, stock)  
- Eliminar productos  
- Reabastecer o ajustar stock

### 2. Ventas
- Registrar venta validando stock disponible  
- Actualizar automáticamente los campos `stock` y `vendidos_hoy`

### 3. Búsquedas y ordenamientos
- **Búsqueda lineal** por código de producto  
- **Búsqueda binaria** (en lista ordenada por código)  
- **Ordenamientos:** burbuja y selección, aplicados según criterio (precio, stock, nombre)

### 4. Reportes
- Top 3 productos más vendidos del día  
- Productos bajo stock mínimo  
- Ticket promedio y total vendido  
- Reporte semanal (matriz 7x3 con ventas por día y franja horaria)

### 5. Persistencia de datos
- Carga y guardado automático en `datos.csv`
- Copia de respaldo binaria (`datos.bin`)
- Exportación selectiva de productos bajo stock (extensión posible)

---

##  Decisiones técnicas

- **Lenguaje:** Python 3  
- **Paradigma:** Programación Orientada a Objetos (POO)  
- **Diseño modular:** cada módulo tiene responsabilidad única  
- **Dataclasses:** para simplificar la definición de clases de datos (`Producto`)  
- **Persistencia:** CSV (texto) + Binario (`pickle`)  
- **Validaciones:** manejo básico de errores y entradas inválidas  

---

##  Extensiones posibles
- Comparativa de tiempos entre ordenamientos (`time.perf_counter`)  
- Log de operaciones (ventas, modificaciones, errores)  
- Exportar a `alertas.csv` los productos bajo stock mínimo  
- Filtros por rango de precios

---

##  Autor
**Omar Torrez**  
Proyecto integrador EC2 - Ingeniería de Sistemas  
Universidad Católica Boliviana “San Pablo”

---

© 2025 - Todos los derechos reservados.
