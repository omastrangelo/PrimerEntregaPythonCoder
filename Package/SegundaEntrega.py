class Cliente:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Edad: {self.edad}")

    def realizar_compra(self, producto):
        print(f"{self.nombre} ha comprado {producto}")

# Crea objeto de la clase Cliente
cliente1 = Cliente("Juan", "Perez", "juan@example.com", 30)
cliente2 = Cliente("Maria", "Gomez", "maria@example.com", 25)

print(cliente1) 
cliente1.mostrar_informacion()
cliente1.realizar_compra("Camisa")

print(cliente2)
cliente2.mostrar_informacion()
cliente2.realizar_compra("Zapatos")
