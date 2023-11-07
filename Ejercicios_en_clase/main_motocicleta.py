from Motocicleta import Motocicleta

moto1 = Motocicleta(
    color="Azul",
    matricula="GOD777",
    combustible_litros=10,
    numero_ruedas=2,
    marca="BMW",
    modelo="M2",
    fecha_fabricacion="2023-24-10",
    velocidad_punta=130,
    peso=180
)
moto2 = Motocicleta(
    color="Azul",
    matricula="OWO123",
    combustible_litros=10,
    numero_ruedas=2,
    marca="BMW",
    modelo="M3",
    fecha_fabricacion="2023-24-10",
    velocidad_punta=130,
    peso=200
)
# Añadir el atributo "precio" desde fuera de la clase para una de las motocicletas
moto1.precio = 12000
moto2.precio = None
print(f"Precio de moto1: {moto1.precio}")

# Prueba los métodos de arranque y detención con ambas motocicletas
moto1.arrancar()
moto1.arrancar()
moto1.detener()
moto1.detener()

print(f"El precio de la motocicleta {moto1.marca} - {moto1.modelo} es de ${moto1.precio}.")

print(f"Consultar precio de moto1: {moto1.consultar_precio()}")
print(f"Consultar precio de moto2: {moto2.consultar_precio()}")

#Repondiendo a la pregunda del trabajo, la moto uno se había definido un precio y largo el precio con el metodo, en cambio la moto2 está vacio, es decir, el precio todavía no está definido.