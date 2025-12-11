class Car:
    # Este es el plano para un Coche

    def __init__(self, color, brand, num_wheels=4):
        # Este es un método especial llamado el "constructor".
        # Es como la línea de montaje inicial para un coche nuevo.
        # 'self' se refiere al objeto coche específico que se está creando.
        self.color = color         # Establece el atributo de color para este coche
        self.brand = brand         # Establece el atributo de marca para este coche
        self.num_wheels = num_wheels # Establece el número de ruedas (por defecto a 4)

    def accelerate(self):
        # Este es un método (comportamiento) para un objeto Coche
        print(f"¡El coche {self.color} {self.brand} está acelerando!")

    def brake(self):
        # Otro método
        print(f"El coche {self.color} {self.brand} está frenando.")

# Creando un objeto (un coche específico) a partir de la clase Coche
my_red_car = Car("rojo", "Toyota")
johns_blue_car = Car("azul", "Honda")
my_red_car.accelerate()
my_red_car.brake()

# Accediendo a los atributos
print(f"Color de mi coche: {my_red_car.color}")
print(f"Marca del coche de Juan: {johns_blue_car.brand}")

# Estableciendo (modificando) un atributo
my_red_car.color = "amarillo"
print(f"Nuevo color de mi coche: {my_red_car.color}")