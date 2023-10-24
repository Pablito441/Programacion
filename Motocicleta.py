class Motocicleta:

    status = 'nueva'
    motor = False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso

    def arrancar(self):
        if self.motor == False:
            self.motor = True
            print("El motor ha arrancado.")
        else:
            print("El motor ya estaba en marcha.")

    def detener(self):
        if self.motor == True:
            self.motor = False
            print("El motor se ha detenido.")
        else:
            print("El motor ya estaba detenido.")

    def consultar_precio(self):
        if self.precio is not None:
            return self.precio
        else:
            return "El precio aún no está definido."


