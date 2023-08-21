def registrar_usuario(usuarios):
    usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    usuarios[usuario] = contrasena
    print("Usuario registrado con éxito.")


def verificar_acceso(usuarios):
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("Acceso concedido.")
    else:
        print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")

def main():
    usuarios = {}  

    while True:
        print("1. Registrar nuevo usuario")
        print("2. Verificar acceso")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            verificar_acceso(usuarios)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()