import json

# Convertir dict a JSON 1
with open('data1.json', 'w') as f:
    json.dump({"name": "Alice"}, f)

# Convertir dict a JSON 2
# Serializar a JSON
json_string = json.dumps({"name": "Alice"})

# Deserializar desde JSON
data = json.loads(json_string)

# Guardar en archivo
with open("data2.json", "w") as f:
    json.dump(data, f, indent=4)

# Leer archivo JSON
with open('data2.json') as f:
    data = json.load(f)
    print(data['name'])