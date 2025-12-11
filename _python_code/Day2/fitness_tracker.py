import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter

# ---------- CLASES ----------

class LogEntry:
    def __init__(self, date):
        self.date = date

class Workout(LogEntry):
    def __init__(self, date, workout_type, duration, calories):
        super().__init__(date)
        self.workout_type = workout_type
        self.duration = duration
        self.calories = calories

class Meal(LogEntry):
    def __init__(self, date, meal_type, food, calories):
        super().__init__(date)
        self.meal_type = meal_type
        self.food = food
        self.calories = calories

# ---------- RUTAS DE ARCHIVOS ----------

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
WORKOUTS_FILE = os.path.join(DATA_DIR, 'workouts.csv')
MEALS_FILE = os.path.join(DATA_DIR, 'meals.csv')

# ---------- LEER CSV MANUALMENTE ----------

def read_workouts_manual(file_path):
    workouts = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Omitir encabezado
        for row in reader:
            date = row[0].strip()
            workout_type = row[1].strip()
            duration = int(row[2].strip())
            calories = int(row[3].strip())
            workouts.append(Workout(date, workout_type, duration, calories))
    return workouts

# ---------- USANDO PANDAS ----------

def load_and_clean_data():
    df_workouts = pd.read_csv(WORKOUTS_FILE)
    df_meals = pd.read_csv(MEALS_FILE)

    df_workouts['date'] = pd.to_datetime(df_workouts['date'])
    df_meals['date'] = pd.to_datetime(df_meals['date'])

    # Rellenar cualquier valor faltante en los datos de entrenamiento con ceros (p. ej., duraciones o calorías faltantes)
    df_workouts.fillna(0, inplace=True)
    # Rellenar cualquier valor faltante en los datos de comidas con "Desconocido" (p. ej., descripciones de alimentos faltantes)
    df_meals.fillna("Unknown", inplace=True)

    return df_workouts, df_meals

# ---------- ANÁLISIS ----------

def summarize_data(df_workouts, df_meals):
    workout_summary = df_workouts.groupby('date')['calories_burned'].sum().reset_index()
    meal_summary = df_meals.groupby('date')['calories'].sum().reset_index()

    combined = pd.merge(workout_summary, meal_summary, on='date', how='outer').fillna(0)
    combined['net_calories'] = combined['calories'] - combined['calories_burned']
    return combined

# ---------- VISUALIZACIÓN ----------

def plot_fitness_trends(combined_df):
    # Crear una nueva figura con el tamaño especificado (ancho: 16 pulgadas, alto: 10 pulgadas)
    # Esto crea un gráfico más grande que es más fácil de leer y analizar
    plt.figure(figsize=(16, 10)) 
    
    # Trazar las calorías consumidas con marcadores circulares
    plt.plot(combined_df['date'], combined_df['calories'], label="Calorías Consumidas", marker='o')
    
    # Trazar las calorías quemadas con marcadores x para una distinción visual
    plt.plot(combined_df['date'], combined_df['calories_burned'], label="Calorías Quemadas", marker='x')
    
    # Trazar las calorías netas (consumidas - quemadas) con un estilo de línea discontinua
    # Esto muestra el balance calórico de cada día
    plt.plot(combined_df['date'], combined_df['net_calories'], label="Calorías Netas", linestyle='--')

    # Calcular y trazar una media móvil de 2 días de las calorías netas
    # Esto suaviza las fluctuaciones diarias y muestra la tendencia general
    rolling = combined_df['net_calories'].rolling(window=2).mean()
    plt.plot(combined_df['date'], rolling, label="Media Móvil (Neta)", linestyle='dotted')

    # Añadir etiquetas de eje con un tamaño de fuente aumentado para una mejor legibilidad
    plt.xlabel('Fecha', fontsize=14)
    plt.ylabel('Calorías', fontsize=14)
    
    # Formatear el eje x para mostrar las fechas en formato AAAA-MM-DD
    # Esto asegura una representación de fecha consistente en el gráfico
    date_format = DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(date_format)
    
    # Rotar las etiquetas del eje x 45 grados para evitar la superposición y aumentar el tamaño de la fuente
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.title('Resumen del Seguimiento de Fitness', fontsize=16) # Añadir un título descriptivo al gráfico con una fuente más grande
    
    plt.legend() # Añadir una leyenda para identificar cada línea en el gráfico
    
    plt.grid(True) # Añadir una cuadrícula para facilitar la lectura de los valores del gráfico
    
    plt.tight_layout() # Ajustar el diseño para asegurar que todos los elementos encajen sin superponerse
    
    plt.show() # Mostrar el gráfico completado


# ---------- FUNCIÓN PRINCIPAL ----------

def main():
    print("Cargando datos...")
    df_workouts, df_meals = load_and_clean_data()

    print("\nResumiendo datos...")
    combined = summarize_data(df_workouts, df_meals)
    print(combined)

    print("\nTrazando resultados...")
    plot_fitness_trends(combined)

if __name__ == "__main__":
    main()
