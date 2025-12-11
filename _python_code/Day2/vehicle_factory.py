class Vehicle: # Plano general
    def __init__(self, num_ruedas, velocidad_maxima):
        self.num_ruedas = num_ruedas
        self.velocidad_maxima = velocidad_maxima

    def move(self):
        print("El vehículo se está moviendo.")

class Car(Vehicle): # Coche hereda de Vehículo
    def __init__(self, color, marca):
        super().__init__(4, 200) # Llama al constructor del padre (Vehículo)
        self.color = color
        self.marca = marca

    def accelerate(self): # Coche tiene su propio método específico
        print(f"¡El coche {self.color} {self.marca} está acelerando!")

class Motorcycle(Vehicle): # Motocicleta también hereda de Vehículo
    def __init__(self, cilindrada):
        super().__init__(2, 180) # Llama al constructor del padre (Vehículo)
        self.cilindrada = cilindrada

    def wheelie(self):
        print(f"¡La motocicleta está haciendo un caballito!")

my_car = Car("verde", "BMW")
my_car.move() # Coche puede usar el método de movimiento del Vehículo
my_car.accelerate()

my_motorcycle = Motorcycle("1000cc")
my_motorcycle.move()
my_motorcycle.wheelie()