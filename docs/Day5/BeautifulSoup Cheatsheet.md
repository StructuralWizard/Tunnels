Hoja de Referencia de BeautifulSoup
BeautifulSoup es una biblioteca de Python para analizar documentos HTML y XML. Crea un árbol de análisis para las páginas analizadas que se puede utilizar para extraer datos de HTML, lo cual es útil para el web scraping.

1. Instalación
Si no tienes instalado BeautifulSoup, puedes instalarlo usando pip:

pip install beautifulsoup4
pip install lxml # Opcional, pero recomendado para un análisis más rápido

2. Análisis Básico
Para empezar, necesitas importar BeautifulSoup y proporcionarle el contenido HTML/XML.

from bs4 import BeautifulSoup

# Contenido HTML de muestra
html_doc = """
<html><head><title>Mi Documento</title></head>
<body>
    <p class="title"><b>El Título del Documento</b></p>

    <a href="http://example.com/one" class="external-link" id="link1">Enlace Uno</a>
    <a href="http://example.com/two" class="external-link" id="link2">Enlace Dos</a>
    <p>Este es otro contenido.</p>
    <div class="container">
        <ul>
            <li>Elemento 1</li>
            <li>Elemento 2</li>
        </ul>
    </div>
</body>
</html>
"""

# Crear un objeto BeautifulSoup
# 'lxml' es un analizador común y rápido; 'html.parser' está incorporado
soup = BeautifulSoup(html_doc, 'lxml')

# Imprimir el HTML analizado con formato
print(soup.prettify())

3. Navegando por el Árbol de Análisis
BeautifulSoup te permite navegar por el documento analizado utilizando el acceso orientado a objetos.

Accediendo a las Etiquetas
Puedes acceder a las etiquetas directamente como atributos del objeto BeautifulSoup u otras etiquetas.

# Obtener la primera etiqueta <head>
head_tag = soup.head
print(f"Etiqueta Head: {head_tag}")

# Obtener la primera etiqueta <title> dentro de <head>
title_tag = soup.title
print(f"Etiqueta Title: {title_tag}")

# Obtener el nombre de la etiqueta
print(f"Nombre de la Etiqueta Title: {title_tag.name}")

# Obtener el contenido de la cadena de la etiqueta
print(f"Contenido de la Etiqueta Title: {title_tag.string}")

# Accediendo a los atributos de una etiqueta
link_one = soup.a
print(f"Href del Enlace Uno: {link_one['href']}")
print(f"Clase del Enlace Uno: {link_one['class']}")

# Obtener todos los atributos como un diccionario
print(f"Atributos del Enlace Uno: {link_one.attrs}")

Navegando hacia Abajo
.contents: Una lista de los hijos directos de la etiqueta.

.children: Un iterador de los hijos directos de la etiqueta.

.descendants: Un iterador de todos los hijos, nietos, etc.

body_tag = soup.body
print("\nContenidos de la Etiqueta Body:")
for child in body_tag.contents:
    if child.name: # Solo imprimir etiquetas reales
        print(child.name)

print("\nDescendientes de la Etiqueta Body (Ejemplos):")
for descendant in body_tag.descendants:
    if descendant.name:
        print(descendant.name, end=" ")
        if descendant.name == 'li': break # Detenerse después de algunos ejemplos

Navegando hacia Arriba
.parent: El padre directo de una etiqueta.

.parents: Un iterador de todos los antepasados.

# Encontrar el padre de la etiqueta de título
p_tag = soup.p
print(f"\nPadre de <p>: {p_tag.parent.name}")

# Iterar a través de los padres de un enlace específico
link2 = soup.find(id="link2")
print(f"Padres de <a id='link2'>:")
for parent in link2.parents:
    if parent is None:
        continue
    if parent.name:
        print(parent.name)

Navegando Lateralmente
.next_sibling: El siguiente hermano después de la etiqueta actual.

.previous_sibling: El hermano anterior antes de la etiqueta actual.

.next_siblings: Un iterador de todos los hermanos siguientes.

.previous_siblings: Un iterador de todos los hermanos precedentes.

first_p_tag = soup.p
print(f"\nSiguiente hermano del primer <p>: {first_p_tag.next_sibling.next_sibling.name}") # Omitir nueva línea
print(f"Hermano anterior del primer <p>: {first_p_tag.previous_sibling.previous_sibling.name}") # Omitir nueva línea

print("\nSiguientes hermanos del primer <p> (ejemplos):")
for sibling in first_p_tag.next_siblings:
    if sibling.name:
        print(sibling.name)

4. Buscando en el Árbol (find() y find_all())
Estos son los métodos más potentes para localizar elementos específicos.

find_all(name, attrs, recursive, string, limit)
Encuentra todas las ocurrencias de una etiqueta que coincidan con los criterios. Devuelve una lista de etiquetas.

name: Nombre de la etiqueta (p. ej., 'a', 'p'). Puede ser una cadena, lista, expresión regular o función.

attrs: Un diccionario de valores de atributos (p. ej., {'class': 'external-link'}).

recursive: Si es False, solo examina los hijos directos. El valor predeterminado es True.

string: Busca cadenas en lugar de etiquetas.

limit: Detiene la búsqueda después de un cierto número de coincidencias.

# Encontrar todas las etiquetas <a>
all_links = soup.find_all('a')
print(f"\nTodos los enlaces: {all_links}")

# Encontrar todas las etiquetas <p> con la clase 'title'
title_p = soup.find_all('p', class_='title') # 'class_' porque 'class' es una palabra clave de Python
print(f"Párrafos con la clase 'title': {title_p}")

# Encontrar todas las etiquetas que tienen un atributo 'id'
tags_with_id = soup.find_all(id=True)
print(f"Etiquetas con un atributo 'id': {tags_with_id}")

# Encontrar todas las etiquetas <li>
list_items = soup.find_all('li')
for item in list_items:
    print(f"Elemento de Lista: {item.string}")

# Encontrar etiquetas que contienen texto específico (usando 'string')
p_with_content = soup.find_all(string="Este es otro contenido.")
print(f"Etiquetas con contenido de cadena específico: {p_with_content}")

find(name, attrs, recursive, string)
Similar a find_all(), pero devuelve solo la primera coincidencia.

# Encontrar la primera etiqueta <a>
first_link = soup.find('a')
print(f"\nPrimer enlace encontrado: {first_link}")

# Encontrar el primer párrafo <p> con la clase 'title'
first_title_p = soup.find('p', class_='title')
print(f"Primer párrafo con la clase 'title': {first_title_p}")

Patrones de Búsqueda Comunes
# Por nombre de etiqueta
print(f"\nEncontrar todas las etiquetas 'p': {soup.find_all('p')}")

# Por clase CSS (¡nota el guion bajo!)
print(f"Encontrar todas las etiquetas 'a' con la clase 'external-link': {soup.find_all('a', class_='external-link')}")

# Por ID
print(f"Encontrar etiqueta con id 'link1': {soup.find(id='link1')}")

# Por valor de atributo (cualquier atributo)
print(f"Encontrar todas las etiquetas con href='http://example.com/one': {soup.find_all(href='http://example.com/one')}")

# Usando una lista de nombres de etiquetas
print(f"Encontrar todas las etiquetas 'p' o 'a': {soup.find_all(['p', 'a'])}")

# Usando expresiones regulares
import re
print(f"Encontrar todas las etiquetas cuyo nombre comienza con 'b': {soup.find_all(re.compile('^b'))}") # p. ej., <body>, <b>
print(f"Encontrar todas las etiquetas con 'link' en su ID: {soup.find_all(id=re.compile('link'))}")

5. Modificando el Árbol
BeautifulSoup te permite modificar el árbol de análisis.

# HTML de muestra para modificación
html_mod = """
<html>
<body>
    <p>Texto original.</p>
    <div id="target">Contenido aquí</div>
</body>
</html>
"""
soup_mod = BeautifulSoup(html_mod, 'lxml')

# Cambiar el nombre de la etiqueta
p_tag_mod = soup_mod.p
p_tag_mod.name = "div"
print(f"\nDespués de cambiar p a div: {soup_mod.prettify()}")

# Modificar los atributos de la etiqueta
div_tag_mod = soup_mod.find(id="target")
div_tag_mod['class'] = 'new-class'
div_tag_mod['data-type'] = 'example'
print(f"Después de modificar los atributos: {soup_mod.prettify()}")

# Añadir nuevo contenido
new_tag = soup_mod.new_tag("span")
new_tag.string = "Texto de span añadido."
div_tag_mod.append(new_tag) # Añadir dentro del div
print(f"Después de añadir una nueva etiqueta: {soup_mod.prettify()}")

# Reemplazar contenido
div_tag_mod.string = "Nuevo contenido reemplazado."
print(f"Después de reemplazar el contenido del div: {soup_mod.prettify()}")

# Eliminar contenido
span_to_remove = soup_mod.find('span')
if span_to_remove:
    span_to_remove.decompose() # Elimina la etiqueta y su contenido
print(f"Después de eliminar el span: {soup_mod.prettify()}")

6. Selectores CSS (select() y select_one())
BeautifulSoup también admite selectores CSS utilizando el método select() (devuelve una lista) y select_one() (devuelve la primera coincidencia).

# Seleccionar todas las etiquetas <p>
print(f"\nSeleccionar todas las etiquetas 'p': {soup.select('p')}")

# Seleccionar etiquetas por clase
print(f"Seleccionar todos los elementos con la clase 'external-link': {soup.select('.external-link')}")

# Seleccionar etiqueta por ID
print(f"Seleccionar elemento con id 'link2': {soup.select('#link2')}")

# Seleccionar hijos directos
print(f"Seleccionar hijos directos <li> de .container: {soup.select('div.container > ul > li')}")

# Seleccionar descendientes
print(f"Seleccionar todos los descendientes <li> de .container: {soup.select('div.container li')}")

# Seleccionar selectores combinados
print(f"Seleccionar etiquetas 'p' o 'a': {soup.select('p, a')}")

# Seleccionar etiquetas con valores de atributos específicos
print(f"Seleccionar etiquetas 'a' con href que comience con 'http://example.com': {soup.select('a[href^=\"http://example.com\"]')}")

# Seleccionar el primer elemento coincidente
print(f"Seleccionar primer enlace: {soup.select_one('a')}")
