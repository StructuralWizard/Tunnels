import requests

# Punto final de la API de GitHub para obtener repositorios de usuario
url = "https://api.github.com/users/octocat/repos"

# Encabezados personalizados
headers = {
    "User-Agent": "MyPythonApp/1.0",
    "Accept": "application/vnd.github.v3+json"
}

# Realizar la solicitud GET
response = requests.get(url, headers=headers)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    # Imprimir los 3 primeros repositorios con nombre y URL
    for repo in data[:3]:
        print(f"Nombre: {repo['name']} - URL: {repo['html_url']}")
else:
    print("La solicitud falló con el código de estado:", response.status_code)
