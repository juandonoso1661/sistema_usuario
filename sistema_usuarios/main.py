from usuario import Usuario

while True:

    print("""
==============================
    SISTEMA DE USUARIOS
==============================
1. Iniciar sesion
2. Salir
""")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        username = input("Usuario: ")
        contrasena = input("Contraseña: ")

        usuario = Usuario(username=username, contrasena=contrasena)

        datos = usuario.login()

        if datos:

            print("\nInicio de sesion exitoso")
            print("Bienvenido:", datos[1])
            print("Rol:", datos[2])

            # ==========================
            # MENU ADMIN
            # ==========================

            if datos[2].lower() == "admin":

                while True:

                    print("""
==============================
MENU ADMINISTRADOR
==============================
1. Registrar usuario
2. Listar usuarios
3. Buscar usuario
4. Modificar usuario
5. Eliminar usuario
6. Cerrar sesion
""")

                    opcion_admin = input("Seleccione una opcion: ")

                    # Registrar usuario
                    if opcion_admin == "1":

                        username = input("Username: ")
                        email = input("Email: ")
                        contrasena = input("Contraseña: ")

                        print("""
1. Admin
2. Usuario
""")

                        id_rol = int(input("Seleccione el rol: "))
                     
                        nuevo = Usuario(
                            username=username,
                            email=email,
                            contrasena=contrasena,
                            id_rol=id_rol
                        )

                        nuevo.crear_usuario()

                    # Listar usuarios
                    elif opcion_admin == "2":

                        Usuario().listar_usuarios()

                    # Buscar usuario
                    elif opcion_admin == "3":

                        id_usuario = int(input("Ingrese ID: "))

                        Usuario().buscar_usuario(id_usuario)

                    # Modificar usuario
                    elif opcion_admin == "4":

                        id_usuario = int(input("ID del usuario: "))
                        username = input("Nuevo username: ")
                        email = input("Nuevo email: ")
                        contrasena = input("Nueva contraseña: ")

                        print("""
1. Admin
2. Usuario
""")

                        id_rol = int(input("Nuevo rol: "))

                        modificar = Usuario(
                            id_usuario=id_usuario,
                            username=username,
                            email=email,
                            contrasena=contrasena,
                            id_rol=id_rol
                        )

                        modificar.modificar_usuario()

                    # Eliminar usuario
                    elif opcion_admin == "5":

                        id_usuario = int(input("ID a eliminar: "))

                        confirmar = input("¿Seguro? (S/N): ")

                        if confirmar.upper() == "S":

                            Usuario().eliminar_usuario(id_usuario)

                    # Cerrar sesión
                    elif opcion_admin == "6":

                        print("\nSesion cerrada.\n")
                        break

                    else:

                        print("Opcion invalida.")

            # ==========================
            # MENU USUARIO
            # ==========================

            else:

                while True:

                    print(f"""
==============================
BIENVENIDO
==============================

Usuario: {datos[1]}
Tipo: {datos[2]}

1. Cerrar sesion
""")

                    opcion_user = input("Seleccione una opcion: ")

                    if opcion_user == "1":

                        print("\nSesion cerrada.\n")
                        break

                    else:

                        print("Opcion invalida.")

        else:

            print("\nUsuario o contraseña incorrectos.\n")

    elif opcion == "2":

        print("Hasta luego.")
        break

    else:

        print("Opcion invalida.")