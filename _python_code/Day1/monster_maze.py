import random

# Constantes
ROOMS = ["Salón", "Cocina", "Biblioteca", "Mazmorra", "Jardín"]
ITEMS = ["espada", "poción", "escudo"]
MONSTERS = ["Goblin", "Trol", "Esqueleto"]

# Variable global
found_key = False

def print_welcome():
    """Imprime el mensaje de bienvenida con arte ASCII."""
    print("""
    🧟‍♂️ LABERINTO DE MONSTRUOS 🧟‍♀️
    ¡Escapa del laberinto, derrota a los monstruos y encuentra la llave!
    """)  # Manipulación e impresión de cadenas

def create_player(name):
    """Devuelve un nuevo diccionario de jugador."""
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": random.choice(ROOMS)  # Módulo random
    }

def describe_room(room):
    """Describe la habitación actual."""
    print(f"\nAhora estás en la {room}.")
    if random.random() < 0.4:  # Declaración condicional
        item = random.choice(ITEMS)
        print(f"¡Has encontrado un {item}!")
        return item
    return None

def encounter_monster(player):
    """Encuentro aleatorio con un monstruo con posibilidad de luchar."""
    if random.random() < 0.3:
        monster = random.choice(MONSTERS)
        print(f"\n⚔️ ¡Aparece un {monster} salvaje!")
        if "espada" in player["inventory"]:
            print("¡Lo derrotas con tu espada!")
        else:
            player["health"] -= 20
            print("¡No tienes espada! ¡Has resultado herido!")
            print(f"Salud: {player['health']}")
            if player["health"] <= 0:
                print("💀 Has muerto. Fin del juego.")
                exit()

def move_to_new_room(player):
    """Mueve al jugador a una nueva habitación aleatoria."""
    previous = player["location"]
    player["location"] = random.choice([r for r in ROOMS if r != previous])

def check_for_key(player):
    """Comprueba si el jugador encuentra la llave."""
    global found_key
    if not found_key and random.random() < 0.2:
        found_key = True
        print("🔑 ¡Has encontrado la llave mágica!")
        player["inventory"].append("llave mágica")

def game_loop(player):
    """Bucle principal del juego usando recursividad."""
    if found_key:
        print(f"\n🎉 ¡Felicidades, {player['name']}! ¡Has escapado del laberinto!")
        return # Termina el juego si se encuentra la llave

    item = describe_room(player["location"])
    if item:
        player["inventory"].append(item)
    
    encounter_monster(player)
    check_for_key(player)

    # Bucle while y formateo de cadenas con f-strings
    while True:
        choice = input("\n¿Quieres moverte a otra habitación? (sí/no): ").lower()
        if choice in ["sí", "si", "s"]:
            move_to_new_room(player)
            game_loop(player)  # Recursividad
            break
        elif choice in ["no", "n"]:
            print("🛌 Has elegido descansar. Fin del juego.")
            break
        else:
            print("Por favor, responde sí o no.")

# Programa principal
def main():
    """Inicia el juego."""
    print_welcome()
    name = input("Introduce tu nombre, aventurero: ")
    player = create_player(name)  # Función con entradas/salidas
    game_loop(player)

if __name__ == "__main__":
    main()
