from usuario import Usuario

while True:

    print("\n==============================")
    print("    SISTEMA DE USUARIOS")
    print("==============================")
    print("1. Iniciar sesion")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        username = input("Usuario: ")
        contrasena = input("Contraseña: ")

        usuario = Usuario(
            username=username,
            contrasena=contrasena
        )

        datos = usuario.login()

        if datos:

            print("\nInicio de sesion exitoso")
            print(f"Bienvenido: {datos[1]}")
            print(f"Rol: {datos[2]}")

        else:

            print("\nUsuario o contraseña incorrectos.")

    elif opcion == "2":
        print("Hasta luego.")
        break

    else:
        print("Opcion invalida.")