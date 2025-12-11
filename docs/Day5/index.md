---
title: Día 5 Web Scraping con Beautiful Soup y Selenium
layout: default
nav_order: 6
has_children: false
nav_exclude: false
---

# Día 5. Web Scraping. 🕷️ Beautiful Soup y Selenium
{: .no_toc }

¡Bienvenido al Día 5! Hoy aprenderás a extraer datos de sitios web usando Python. Empezaremos con Beautiful Soup para páginas estáticas, y luego pasaremos a Selenium para sitios dinámicos e interactivos. ¡Al final, podrás recolectar datos de la web para tus propios proyectos!

---

<details open markdown="block">
  <summary>
    Índice de contenidos
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 🌱 ¿Qué es el Web Scraping?
El web scraping es el proceso de recopilar información de sitios web de forma automática. Es útil para recopilar datos que no están disponibles a través de una API.

- **Beautiful Soup**: Analiza documentos HTML y XML. Ideal para páginas estáticas.
- **Selenium**: Automatiza navegadores. Útil para sitios dinámicos que requieren interacción (clics, escritura, etc.).

---

## 🥣 Conceptos básicos de Beautiful Soup <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Para analizar y navegar por HTML/XML con Python
Requiere: beautifulsoup4 y un analizador como lxml o el analizador html.parser integrado de Python.

### 🧩 ¿Qué puedes hacer con Beautiful soup?
Aquí hay un desglose de sus capacidades principales:

* **Analizar HTML y XML:** Beautiful Soup toma contenido HTML o XML sin procesar y lo transforma en un "árbol de análisis" navegable hecho de objetos de Python. Este árbol simplifica el acceso y la manipulación de partes específicas del documento.

* **Navegar por el árbol de análisis:** Puedes moverte fácilmente a través de la estructura HTML/XML:
    * **Por nombre de etiqueta:** Encuentra elementos como `<div>`, `<a>` o `<p>`.
    * **Por atributos:** Localiza elementos según su `id`, `class`, `href` o cualquier otro atributo.
    * **Por contenido de texto:** Busca palabras o frases específicas dentro de los elementos.
    * **Usando relaciones:** Viaja hacia arriba (padre), hacia abajo (hijos, descendientes) o hacia los lados (hermanos) en el árbol.

* **Buscar elementos específicos:** Beautiful Soup ofrece métodos potentes como `find()` (para obtener la primera coincidencia) y `find_all()` (para obtener todas las coincidencias) para localizar los datos exactos que estás buscando. Puedes combinar estos con varios filtros (nombres de etiquetas, atributos, selectores CSS, expresiones regulares o incluso funciones personalizadas) para una selección precisa.

* **Extraer datos:** Una vez que has encontrado los elementos que quieres, puedes extraer fácilmente:
    * **Contenido de texto:** Obtén el texto visible dentro de una etiqueta (p. ej., `soup.title.string`).
    * **Valores de atributos:** Accede a los valores de atributos como `href` de una etiqueta `<a>` o `src` de una etiqueta `<img>`.

* **Manejar HTML mal formado:** Una de las fortalezas de Beautiful Soup es su capacidad para lidiar con "sopa de etiquetas"—HTML mal estructurado o incompleto. Intenta darle sentido y construir un árbol de análisis utilizable.

* **Integrarse con otras bibliotecas:**
    * **Requests:** A menudo se usa con la biblioteca `requests` para obtener el contenido HTML de una URL antes de que Beautiful Soup lo analice.
    * **Selenium:** Para sitios web dinámicos que dependen en gran medida de JavaScript para el renderizado, puedes usar Selenium (una herramienta de automatización de navegador) para cargar la página y luego pasar el HTML renderizado a Beautiful Soup para su análisis.
    * **Pandas:** Los datos extraídos se pueden estructurar y almacenar fácilmente en DataFrames de Pandas para un análisis posterior o para exportarlos a formatos como CSV o Excel.

---

### 🧰 Usos Comunes de Beautiful Soup

Beautiful Soup se utiliza principalmente para:

* **Web Scraping:** Este es su propósito principal. Puedes usarlo para:
    * Recopilar información de productos (nombres, precios, descripciones) de sitios de comercio electrónico.
    * Extraer artículos de noticias, publicaciones de blogs o trabajos de investigación.
    * Recopilar listados de trabajo o datos inmobiliarios.
    * Realizar análisis de sentimientos raspando reseñas o comentarios.
* **Minería de Datos:** Convertir datos web no estructurados en conjuntos de datos organizados para su análisis.
* **Agregación de Contenido:** Crear herramientas que extraen contenido de múltiples fuentes en línea a una ubicación centralizada.

En resumen, Beautiful Soup permite a los desarrolladores de Python interactuar programáticamente con el contenido web, lo que lo convierte en una herramienta esencial para cualquiera que busque extraer y trabajar con datos de Internet.

### 📦 Instalar los paquetes necesarios
```bash
pip install beautifulsoup4 requests lxml
```

### 📄 Ejemplo: Raspado de un archivo HTML local
Supongamos que tienes un archivo llamado `website.html`:

```python
from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
```

### 🧼 Limpieza de HTML
```python
clean_text = soup.get_text(strip=True)
```

### 🔍 Encontrar Elementos
Puedes buscar por etiquetas, clases, ids y más:

```python
# Encontrar la primera etiqueta <a>
anchor = soup.find("a")
print(anchor)

# Encontrar todas las etiquetas <a>
all_anchors = soup.find_all("a")
for tag in all_anchors:
    # .getText() obtiene el texto visible dentro de la etiqueta
    print(tag.getText())
    # .get() recupera el valor de un atributo (p. ej., href)
    print(tag.get("href"))
```

#### Buscar por atributos (id, clase, etc.)
```python
# Encontrar por id
heading = soup.find(name="h1", id="name")

# Encontrar por clase (nota: usa class_ porque 'class' es una palabra reservada)
section = soup.find(name="h3", class_="heading")

# Encontrar todos los elementos con una clase específica
items = soup.find_all(class_="item")
```

#### Buscar usando selectores CSS
```python
# Usa .select() para selectores CSS
links = soup.select("a.storylink")  # Todas las etiquetas <a> con la clase 'storylink'
ids = soup.select("#main")          # Elemento con id 'main'
classes = soup.select(".heading")   # Todos los elementos con la clase 'heading'
```

### 🌳 Navegando por el Árbol
```python
tag.name         # Nombre de la etiqueta
tag.attrs        # Atributos de la etiqueta como dict
tag['href']      # Atributo específico

tag.text         # Todo el texto dentro de la etiqueta (recursivo)
tag.string       # Solo la cadena directa
tag.parent
tag.children      # Generador de hijos
tag.contents      # Lista de hijos
tag.next_sibling
tag.previous_sibling

```


### 🔗 Navegando y Siguiendo Enlaces
Puedes extraer y seguir enlaces combinando `.get("href")` con requests:

```python
for tag in soup.find_all("a"):
    link = tag.get("href")
    if link and link.startswith("http"):
        print("Siguiendo:", link)
        # Puedes obtener la página enlazada con requests.get(link)
```

Para más referencias, sigue la <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">documentación</a>


---

## 🌐 Raspado de Sitios Web en Vivo <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Para raspar un sitio web en vivo, usa la biblioteca `requests` para obtener la página:

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# Obtener todos los títulos de los artículos
titles = soup.find_all("a", class_="storylink")
for title in titles:
    print(title.getText())
```

---

## ⚖️ ¿Es Legal el Web Scraping? <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Solo raspa datos públicos.
- Respeta el archivo robots.txt y los términos del sitio web.
- No sobrecargues los servidores (agrega retrasos si raspas muchas páginas).
- Usa los datos raspados de manera responsable.

---

## 🤖 Selenium para Sitios Web Dinámicos <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Algunos sitios cargan contenido con JavaScript o requieren interacción. Selenium te permite controlar un navegador real para manejar estos casos.

A diferencia de Beautiful Soup, que se limita a raspar datos, Selenium permite la interacción con las páginas web, como escribir, hacer clic y desplazarse. Permite la automatización de acciones continuas y flujos de trabajo completos de un trabajo o tarea en particular. Conduce eficazmente un navegador para realizar acciones como un usuario humano.

Selenium puede automatizar casi cualquier cosa que un humano pueda hacer en un sitio web, como rellenar formularios, transferir información o jugar juegos basados en la web.

### 🚗 Introducción a Selenium WebDriver

* **Qué es:** Selenium WebDriver es una conocida herramienta de automatización y prueba para desarrolladores web.
* **Por qué usarlo (en lugar de Beautiful Soup):** A diferencia de Beautiful Soup, que se limita a raspar datos, Selenium permite la interacción con las páginas web, como escribir, hacer clic y desplazarse. Permite la automatización de acciones continuas y flujos de trabajo completos de un trabajo o tarea en particular. Conduce eficazmente un navegador para realizar acciones como un usuario humano.
* **Capacidades:** Selenium puede automatizar casi cualquier cosa que un humano pueda hacer en un sitio web, como rellenar formularios, transferir información o jugar juegos basados en la web.

### 🔧 Instalación y Configuración de Selenium

1.  **Instalar el navegador Chrome:** Aunque Selenium funciona con otros navegadores como Firefox o Safari, se recomienda Chrome por su consistencia y el uso de las Herramientas de Desarrollo de Chrome. Descarga el controlador de Chrome desde [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) y colócalo en tu RUTA.
2.  **Instalar el paquete de Selenium:**
    * Importa `selenium` en tu archivo de Python (p. ej., `main.py`).
    * Instala el paquete usando la opción de bombilla proporcionada en tu IDE.
```bash
pip install selenium
```
3.  **Importar el Módulo WebDriver:** Cambia la declaración de importación a `from selenium import webdriver`.
4.  **Crear una Instancia de Driver:** Inicializa un objeto de controlador de Chrome: `driver = webdriver.Chrome()`.
    * **Chromedriver:** Actúa como un puente entre el código de Selenium y el navegador Chrome, diciéndole a Selenium cómo interactuar con el navegador. Existen diferentes controladores para diferentes navegadores (p. ej., Safari, Firefox).
5.  **Control del Navegador:**
    * `driver.close()`: Cierra la pestaña activa.
    * `driver.quit()`: Cierra todo el navegador. Se prefiere usar `quit()` después de completar las tareas para asegurar una instancia de navegador nueva para futuras ejecuciones.

### 🔎 Ejemplo: Abrir una Página y Encontrar un Elemento
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time_module

# Iniciar el navegador
browser = webdriver.Chrome()
browser.get("https://www.python.org")

# Encontrar elementos
event_times = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = browser.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for time, name in zip(event_times, event_names):
    print(time.text, name.text)

# Esperar 3 segundos antes de cerrar
time_module.sleep(3)

browser.quit()
```

### 🔍 Encontrar y Seleccionar Elementos en un Sitio Web

**Localización de Elementos:**

Selenium ofrece varias estrategias para encontrar elementos HTML en una página web. Una vez que has identificado un elemento con la herramienta de inspección del navegador, puedes copiar su Xpath u otro y usarlo como identificador con:

* **Método `find_element()`:** Se usa para encontrar un solo elemento.
* **Clase `By`:** Importante para especificar la estrategia de localización (p. ej., `By.CLASS_NAME`, `By.ID`, `By.NAME`, `By.LINK_TEXT`).
* **Ejemplos:**
    * **Por Nombre de Clase:** Para obtener el precio de un artículo en Amazon, podrías encontrar elementos con clases como "a-price-whole" (para los dólares) y "a-price-fraction" (para los centavos).
    * **Acceder al Contenido de Texto:** Después de encontrar un elemento, usa `.text` para recuperar el contenido de texto dentro de ese elemento HTML.
    * **Por Nombre:** Útil para campos de entrada de formularios.
    * **Por Texto del Enlace:** Específicamente para hacer clic en enlaces por su texto visible.
* **Método `find_elements()`:** Por cada método `find_element()`, hay un homólogo `find_elements()` que devuelve una lista de todos los elementos coincidentes.
* **Inspeccionar Elementos:** Usa las Herramientas de Desarrollo de Chrome (clic derecho -> Inspeccionar) para examinar la estructura HTML e identificar IDs, nombres de clase u otros atributos de los elementos.

### 🖱️ Automatización de Interacciones (Escribir y Hacer Clic)

* **Hacer Clic en Elementos:**
    * Después de identificar un elemento, usa el método `.click()` en el objeto del elemento.
    * Selenium puede hacer clic en enlaces basándose en su `LINK_TEXT`.
* **Escribir en Campos de Entrada:**
    * Primero, encuentra el elemento del campo de entrada.
    * Usa el método `.send_keys()` en el objeto del elemento, pasando la cadena que quieres escribir.
* **Enviar Teclas Especiales:** Para enviar teclas como `Enter` o `Return`, importa la clase `Keys` desde `selenium.webdriver.common.keys`.


---

## 📝 Desafío: Raspar los Próximos Eventos de Python <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Usa Selenium para abrir [python.org](https://www.python.org/)
- Extrae la fecha y el nombre de los próximos 5 eventos
- Guárdalos en un diccionario como:

```python
events = {
    0: {"time": "2025-06-11", "name": "PyCon"},
    1: {"time": "2025-06-18", "name": "DjangoCon"},
    # ...
}
```

---

## 🚀 Resumen <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Usa Beautiful Soup para el raspado de HTML estático
- Usa Selenium para sitios dinámicos e interactivos
- Respeta siempre las reglas y la ética del sitio web

Ahora tienes las herramientas para recopilar datos de casi cualquier sitio web. ¡Feliz raspado!
