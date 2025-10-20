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
VIDEO
https://www.icloud.com/attachment/?u=https%3A%2F%2Fcvws.icloud-content.com%2FB%2FAWwp4XINlIkWvp9cQDPOh4Zj1mSTAZYqOi8tI60VuTTvjLdK2PM3601N%2F%24%7Bf%7D%3Fo%3DAkedt3GTtYReloa564j5aIeOHo3TGA3GxA0DxZj7Ibpx%26v%3D1%26x%3D3%26a%3DCAogskDmOLZEdhgRQMDLKoZP8HHDCwWpF7XTj6ons6c4dJ8SehCk2u3_nzMYpOro06kzIgEAKgkC6AMA_ymSdoFSBGPWZJNaBDfrTU1qJ7zzqG1EigpRFgMs2QZbtlQwvCecKguqY8biMtpfnGCty8glYFzzN3InLNG01A_gcmX9X4Kgz8l5dGqeYsveHhSK9zclNHYCgaDmKCURdMLz%26e%3D1763528291%26fl%3D%26r%3DF643FFDA-9C2D-4B66-920A-E9F5C67DE480-1%26k%3D%24%7Buk%7D%26ckc%3Dcom.apple.largeattachment%26ckz%3D3478BCBB-F99E-4888-84BF-2118022C241B%26p%3D147%26s%3DfQDktQtcKCNHMPtTCzZa1lPeH0Q&uk=62QXke_4NQBYvS0e-RMwoA&f=7844F84A-5E51-421F-AB46-9E4F573D2A86.mov&sz=262780694

© 2025 - Todos los derechos reservados.
