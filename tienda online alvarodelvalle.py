# lista de articulos
articulos = []  # lista de articulos

# articulos iniciales
articulo1 = {"id": 1, "nombre": "raton", "precio": 12.5, "stock": 20, "activo": True}
articulo2 = {"id": 2, "nombre": "alfombrilla", "precio": 5.5, "stock": 345, "activo": True}
articulo3 = {"id": 3, "nombre": "teclado", "precio": 30.5, "stock": 10, "activo": True}
articulo4 = {"id": 4, "nombre": "monitor", "precio": 112.5, "stock": 5, "activo": True}

# anadir articulos a la lista
articulos.append(articulo1)
articulos.append(articulo2)
articulos.append(articulo3)
articulos.append(articulo4)

def mostrar_menu():
    menu = """
1. Crear articulo
2. Listar articulos
3. Buscar articulo por id
4. Actualizar articulo
5. Eliminar articulo
6. Alternar activo/inactivo
7. Salir
"""
    print(menu)
    opcion = input("Seleccione una opcion: ")
    return opcion

def crear_articulo():
    print("---Crear nuevo articulo---")
    nombre = input("Ingrese el nombre del articulo: ")
    precio = float(input("Ingrese el precio del articulo: "))
    stock = int(input("Ingrese la cantidad en stock: "))
    if len(articulos) == 0:
        id_articulo = 1
    else:
        id_articulo = articulos[-1]["id"] + 1
    activo = True
    articulo = {"id": id_articulo, "nombre": nombre, "precio": precio, "stock": stock, "activo": activo}
    articulos.append(articulo)
    print(f"Articulo '{nombre}' anadido correctamente")

def listar_articulos():
    if not articulos:
        print("No hay articulos para mostrar")
        return
    for articulo in articulos:
        estado = "activo" if articulo["activo"] else "inactivo"
        print("ID:", articulo["id"], "Nombre:", articulo["nombre"], "Precio:", articulo["precio"],
              "Stock:", articulo["stock"], "Estado:", estado)

def buscar_articulo():
    id_buscar = int(input("Ingrese el ID del articulo a buscar: "))
    encontrado = False
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            estado = "activo" if articulo["activo"] else "inactivo"
            print("ID:", articulo["id"])
            print("Nombre:", articulo["nombre"])
            print("Precio:", articulo["precio"])
            print("Stock:", articulo["stock"])
            print("Estado:", estado)
            encontrado = True
    if not encontrado:
        print("Articulo no encontrado")

def actualizar_articulo():
    id_buscar = int(input("Ingrese el ID del articulo que desea actualizar: "))
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            if nuevo_nombre != "":
                articulo["nombre"] = nuevo_nombre
            nuevo_precio = input("Introduce nuevo precio: ")
            if nuevo_precio != "":
                articulo["precio"] = float(nuevo_precio)
            nuevo_stock = input("Introduce el stock nuevo del producto: ")
            if nuevo_stock != "":
                articulo["stock"] = int(nuevo_stock)
            print("Articulo actualizado correctamente")
            return
    print("Articulo no encontrado")

def eliminar_articulo():
    id_buscar = int(input("Ingrese el ID del articulo que desea eliminar: "))
    encontrado = False
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            articulo["activo"] = False
            encontrado = True
            print("Articulo eliminado correctamente")
            return
    if not encontrado:
        print("Articulo no encontrado")

def activo_inactivo():
    id_buscar = int(input("Ingrese el ID del articulo para alternar activo o inactivo: "))
    encontrado = False
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            if articulo["activo"]:
                articulo["activo"] = False
                estado = "inactivo"
            else:
                articulo["activo"] = True
                estado = "activo"
            print(f"Estado del articulo cambiado a {estado}")
            encontrado = True
    if not encontrado:
        print("Articulo no encontrado")

def salir():
    print("Saliendo del programa, hasta luego")

def menu_articulos():
    opcion = ""
    while opcion != "7":
        opcion = mostrar_menu()
        match opcion:
            case "1":
                crear_articulo()
            case "2":
                listar_articulos()
            case "3":
                buscar_articulo()
            case "4":
                actualizar_articulo()
            case "5":
                eliminar_articulo()
            case "6":
                activo_inactivo()
            case "7":
                salir()
            case _:
                print("Opcion no valida")

# menu_articulos() # comentar si vas a iniciar desde menu principal

# lista de usuarios
usuarios = []

# usuarios iniciales
usuario1 = {"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": True}
usuario2 = {"id": 2, "nombre": "Luis", "email": "luis@example.com", "activo": True}
usuario3 = {"id": 3, "nombre": "Marta", "email": "marta@example.com", "activo": True}
usuario4 = {"id": 4, "nombre": "Carlos", "email": "carlos@example.com", "activo": True}

# anadir usuarios a la lista
usuarios.append(usuario1)
usuarios.append(usuario2)
usuarios.append(usuario3)
usuarios.append(usuario4)

def mostrar_menu_usuarios():
    menu = """
USUARIOS
1. Crear usuario
2. Listar usuarios
3. Buscar usuario por id
4. Actualizar usuario
5. Eliminar usuario
6. Alternar activo/inactivo
7. Volver
"""
    print(menu)
    opcion = input("Seleccione una opcion: ")
    return opcion

def crear_usuario():
    print("---Crear nuevo usuario---")
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el email del usuario: ")
    if "@" not in email or "." not in email:
        print("Email no valido")
        return
    if len(usuarios) == 0:
        id_usuario = 1
    else:
        id_usuario = usuarios[-1]["id"] + 1
    activo = True
    usuario = {"id": id_usuario, "nombre": nombre, "email": email, "activo": activo}
    usuarios.append(usuario)
    print(f"Usuario '{nombre}' anadido correctamente")

def listar_usuarios():
    if not usuarios:
        print("No hay usuarios para mostrar")
        return
    for usuario in usuarios:
        estado = "activo" if usuario["activo"] else "inactivo"
        print("ID:", usuario["id"], "Nombre:", usuario["nombre"], "Email:", usuario["email"], "Estado:", estado)

def buscar_usuario():
    id_buscar = int(input("Ingrese el ID del usuario a buscar: "))
    encontrado = False
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            estado = "activo" if usuario["activo"] else "inactivo"
            print("ID:", usuario["id"])
            print("Nombre:", usuario["nombre"])
            print("Email:", usuario["email"])
            print("Estado:", estado)
            encontrado = True
    if not encontrado:
        print("Usuario no encontrado")

def actualizar_usuario():
    id_buscar = int(input("Ingrese el ID del usuario que desea actualizar: "))
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            if nuevo_nombre != "":
                usuario["nombre"] = nuevo_nombre
            nuevo_email = input("Introduce el nuevo email: ")
            if nuevo_email != "":
                if "@" in nuevo_email and "." in nuevo_email:
                    usuario["email"] = nuevo_email
                else:
                    print("Email no valido")
            print("Usuario actualizado correctamente")
            return
    print("Usuario no encontrado")

def eliminar_usuario():
    id_buscar = int(input("Ingrese el ID del usuario que desea eliminar: "))
    encontrado = False
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            usuario["activo"] = False
            encontrado = True
            print("Usuario eliminado correctamente")
            return
    if not encontrado:
        print("Usuario no encontrado")

def alternar_activo_usuario():
    id_buscar = int(input("Ingrese el ID del usuario para alternar activo/inactivo: "))
    encontrado = False
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            if usuario["activo"]:
                usuario["activo"] = False
                estado = "inactivo"
            else:
                usuario["activo"] = True
                estado = "activo"
            print(f"Estado del usuario cambiado a {estado}")
            encontrado = True
    if not encontrado:
        print("Usuario no encontrado")

def menu_usuarios():
    opcion = ""
    while opcion != "7":
        opcion = mostrar_menu_usuarios()
        match opcion:
            case "1":
                crear_usuario()
            case "2":
                listar_usuarios()
            case "3":
                buscar_usuario()
            case "4":
                actualizar_usuario()
            case "5":
                eliminar_usuario()
            case "6":
                alternar_activo_usuario()
            case "7":
                print("Volviendo al menu principal, hasta pronto!")
            case _:
                print("Opcion no valida")

# menu_usuarios() # comentar si vas a iniciar desde menu principal


#-- ejercicio 3

ventas = []  # lista de ventas
carrito_actual = []  # [(articulo_id, cantidad)]
usuario_activo = None  # id del usuario que está comprando

def buscar_articulo_por_id(id_buscar):
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            return articulo
    return None

def buscar_usuario_por_id(id_buscar):
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            return usuario
    return None

def seleccionar_usuario_activo():
    global usuario_activo
    listar_usuarios()
    try:
        id_usuario = int(input("Ingrese el ID del usuario que realizará la compra: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    usuario = buscar_usuario_por_id(id_usuario)
    if usuario and usuario["activo"]:
        usuario_activo = id_usuario
        print(f"Usuario activo establecido: {usuario['nombre']}")
    else:
        print("Usuario no encontrado o inactivo.")

def anadir_al_carrito():
    global carrito_actual
    if usuario_activo is None:
        print("Debe seleccionar un usuario activo antes de añadir artículos.")
        return
    try:
        id_articulo = int(input("Ingrese el ID del artículo a añadir: "))
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Debe ingresar valores numéricos válidos.")
        return
    articulo = buscar_articulo_por_id(id_articulo)
    if not articulo or not articulo["activo"]:
        print("Artículo no encontrado o inactivo.")
        return
    if cantidad < 1:
        print("La cantidad debe ser al menos 1.")
        return
    if cantidad > articulo["stock"]:
        print("No hay suficiente stock disponible.")
        return
    for i, (art_id, cant) in enumerate(carrito_actual):
        if art_id == id_articulo:
            carrito_actual[i] = (art_id, cant + cantidad)
            print("Cantidad actualizada en el carrito.")
            return
    carrito_actual.append((id_articulo, cantidad))
    print(f"Artículo '{articulo['nombre']}' añadido al carrito.")

def quitar_del_carrito():
    global carrito_actual
    if not carrito_actual:
        print("El carrito está vacío.")
        return
    try:
        id_articulo = int(input("Ingrese el ID del artículo a quitar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    for item in carrito_actual:
        if item[0] == id_articulo:
            carrito_actual.remove(item)
            print("Artículo eliminado del carrito.")
            return
    print("Ese artículo no está en el carrito.")

def calcular_total_carrito():
    total = 0
    for (art_id, cantidad) in carrito_actual:
        articulo = buscar_articulo_por_id(art_id)
        if articulo:
            total += articulo["precio"] * cantidad
    return total

def ver_carrito():
    if not carrito_actual:
        print("El carrito está vacío.")
        return
    print("\n--- CARRITO ACTUAL ---")
    total = 0
    for (art_id, cantidad) in carrito_actual:
        articulo = buscar_articulo_por_id(art_id)
        if articulo:
            subtotal = articulo["precio"] * cantidad
            total += subtotal
            print(f"ID: {art_id} | {articulo['nombre']} | Cant: {cantidad} | Precio: {articulo['precio']}€ | Subtotal: {subtotal}€")
    print(f"TOTAL: {total}€\n")

def confirmar_compra():
    global carrito_actual, ventas
    if usuario_activo is None:
        print("Debe seleccionar un usuario activo antes de confirmar una compra.")
        return
    if not carrito_actual:
        print("El carrito está vacío.")
        return
    for art_id, cantidad in carrito_actual:
        articulo = buscar_articulo_por_id(art_id)
        if not articulo or not articulo["activo"]:
            print(f"El artículo con ID {art_id} no existe o está inactivo. Cancelando compra.")
            return
        if articulo["stock"] < cantidad:
            print(f"No hay suficiente stock para '{articulo['nombre']}'. Cancelando compra.")
            return
    total = calcular_total_carrito()
    items = []
    for art_id, cantidad in carrito_actual:
        articulo = buscar_articulo_por_id(art_id)
        articulo["stock"] -= cantidad
        items.append((art_id, cantidad, articulo["precio"]))
    id_venta = len(ventas) + 1
    venta = {
        "id_venta": id_venta,
        "usuario_id": usuario_activo,
        "items": items,
        "total": total
    }
    ventas.append(venta)
    carrito_actual = []
    print(f"Compra confirmada. Total: {total}€. Venta registrada con ID {id_venta}.")

def historial_ventas_por_usuario():
    try:
        id_usuario = int(input("Ingrese el ID del usuario: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    ventas_usuario = [v for v in ventas if v["usuario_id"] == id_usuario]
    if not ventas_usuario:
        print("No hay ventas registradas para este usuario.")
        return
    print(f"\n--- HISTORIAL DE VENTAS (Usuario ID {id_usuario}) ---")
    for venta in ventas_usuario:
        print(f"Venta ID: {venta['id_venta']} | Total: {venta['total']}€")
        for (art_id, cant, precio) in venta["items"]:
            articulo = buscar_articulo_por_id(art_id)
            nombre = articulo["nombre"] if articulo else "Desconocido"
            print(f"   - {nombre} (x{cant}) @ {precio}€")
    print("-----------------------------------------------")

def vaciar_carrito():
    global carrito_actual
    carrito_actual = []
    print("Carrito vaciado correctamente.")

def menu_ventas():
    opcion = ""
    while opcion != "8":
        print("""
VENTAS / CARRITO
1. Seleccionar usuario activo
2. Añadir artículo al carrito
3. Quitar artículo del carrito
4. Ver carrito (detalle y total)
5. Confirmar compra
6. Historial de ventas por usuario
7. Vaciar carrito
8. Volver
""")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1": seleccionar_usuario_activo()
            case "2": anadir_al_carrito()
            case "3": quitar_del_carrito()
            case "4": ver_carrito()
            case "5": confirmar_compra()
            case "6": historial_ventas_por_usuario()
            case "7": vaciar_carrito()
            case "8": print("Volviendo al menú principal...")
            case _: print("Opción no válida.")
