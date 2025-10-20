def buscar_lineal(lista, codigo):
    for p in lista:
        if p.codigo == codigo:
            return p
    return None

def ordenar_burbuja(lista, clave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if getattr(lista[j], clave) > getattr(lista[j + 1], clave):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_seleccion(lista, clave):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if getattr(lista[j], clave) < getattr(lista[min_idx], clave):
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def busqueda_binaria(lista, codigo):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if lista[mid].codigo == codigo:
            return lista[mid]
        elif lista[mid].codigo < codigo:
            izq = mid + 1
        else:
            der = mid - 1
    return None
