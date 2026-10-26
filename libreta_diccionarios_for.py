"""Libreta de contactos aplicando bucle for y validando llaves"""

# Diccionario anidado de contactos donde el nombre es la clave principal (key)

contactos = {
    "Papa Juan Pablo II": {"Telefono": "3795551", "Lema": "Totus tuus"},
    "Papa Benedicto XVI": {"Telefono": "3795552", "Lema": "Cooperatores veritatis"},
    "Papa Francisco": {"Telefono": "3795553", "Lema": "Miserando atque eligendo"},
    "Papa Leon XIV": {"Telefono": "3795554", "Lema": "In Illo uno unum"},
}

# Lista de las opciones del menú

menu = [
    ["1. Ver todos los contactos"],
    ["2. Agregar un nuevo contacto"],
    ["3. Buscar un contacto"],
    ["4. Salir"],
]

while True:
    # reorrido en el bucle for para mostrar al usuario las opciones del menú
    print("\n" + "*" * 35 + "\n" + "*" * 35)
    print("\n" + "*** " + "Elija una de las siguientes opciones del menú" + " ***")

    for opcion in menu:
        print(opcion)

    # Petición al usuario de selección de una opción del menú

    opcion = input("Selecciona una opción (1-4): ").strip()

    # Respuesta a la opción seleccionada por el usuario
    match opcion:
        case "1":  # Mostrará todos los Papas que están en el diccionario de contactos
            print("\n--- LISTA DE CONTACTOS ---")
            for i, (Papa, datos) in enumerate(contactos.items(), start=1):
                print(
                    f"{i}. Papa: {Papa}, Telefono: {datos['Telefono']}, Lema: {datos['Lema']}"
                )
        case "2":
            print("\n--- AGREGAR NUEVO CONTACTO PAPAL ---")
            nuevo_papa = input("Ingresa el nombre: ").strip().title()

            # Validar que el nombre no quede vacío
            if not nuevo_papa:
                print("⚠️ El nombre del Papa no puede estar vacío.")

            nuevo_telefono = input("Ingresa el teléfono: ").strip()

            # Validar que el teléfono contenga solo números
            if not nuevo_telefono.isdigit():
                print("Teléfono inválido. Solo se admiten números.")

            nuevo_lema = input(
                "Ingresa el lema, el lema puede quedar en blanco: "
            ).strip()
            contactos[nuevo_papa] = {"Telefono": nuevo_telefono, "Lema": nuevo_lema}

        case "3":
            # Pidiendo al usuario el nombre del Papa a buscar
            print("\n¡BUSQUEDA PAPAL!")
            buscar = input("Ingresa el nombre del Papa a buscar ").strip().title()
            encontrado = False

            # Recoriendo el diccionario externo con for para comparar nombres
            for papa, datos in contactos.items():
                nombre_papal = papa
                telefono_papal = datos["Telefono"]
                lema_papal = datos["Lema"]
                if buscar in nombre_papal.title():
                    print(
                        f"Encontrado: {nombre_papal} -> Teléfono: {telefono_papal} -> Lema: {lema_papal}"
                    )
                    encontrado = True
                    break  # Detiene la búsqueda al encontrar la primera coincidencia

            if not encontrado:
                print("No se encontró ningún Papa con ese nombre.")

        case "4":
            print("\n ¡Gracias por usar la libreta de contactos!")
            break
        case _:
            break
