# 10 Días de Código con IA

Este repositorio contiene las notas del curso y los ejemplos de código del curso [10 Días de Python con IA]. El curso está dirigido a programadores curiosos de Vibe sin experiencia en programación que desean obtener una visión global de programación con tecnologías de IA y las habilidades para depurar, especificar y examinar el código que se produce principalmente con IA.

El curso ha sido creado en [Inglés] y traducido al [Español] y [Portugués]. 

El curso está enfocado principalmente al uso de [Visual Studio Code] y [Github Copilot]; y una gran parte de él usa python para automatización, llamadas a API, programación web, programación de IA y más.

Las notas del curso se pueden encontrar en [notas del curso 10 Días de Código con IA] y los ejemplos de código en [ejemplos de código de git hub]. Una vez que [Visual Studio Code] y [python] estén instalados en su máquina, puede ejecutar los ejemplos simplemente escribiendo en su terminal:

```python
python <nombre_archivo>.py
```

## Clonando el Repositorio

Si lo desea, puede instalar git en su vs code y clonar este repositorio en su máquina local.

### Instalando Bash en Visual Studio Code

Si está en Windows y desea usar Bash en VS Code, puede instalar [Git para Windows](https://git-scm.com/download/win), que incluye Git Bash.

1. Descargue e instale Git para Windows.
2. Después de la instalación, abra VS Code.
3. Presione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> y escriba `Terminal: Select Default Profile`.
4. Elija `Git Bash` de la lista.

Ahora, cuando abra una nueva terminal en VS Code, usará Bash.

> **Nota:** La instalación de Git para Windows también instalará Git Bash. No necesita instalar Git por separado. Git Bash se incluye como parte del paquete de instalación de Git.

### Crear un entorno virtual y activarlo
Un **entorno virtual** en Python es un espacio de trabajo aislado que le permite instalar y administrar paquetes por separado de su instalación global de Python. Esto significa que cada proyecto puede tener sus propias dependencias, versiones y configuraciones sin interferir con otros proyectos o el Python del sistema.

**¿Por qué usar un entorno virtual?**

- Aislamiento: Mantiene las dependencias del proyecto separadas, evitando conflictos entre los paquetes requeridos por diferentes proyectos.
- Reproducibilidad: Facilita compartir su proyecto con otros, ya que puede especificar exactamente qué paquetes y versiones se necesitan.
- Seguridad: Evita cambios accidentales en los paquetes de Python de todo el sistema.

Flujo de trabajo típico:
- Crear un entorno virtual para su proyecto.
- Activarlo antes de trabajar.
- Instalar paquetes usando pip—estos solo van al entorno virtual.
- Desactivar cuando haya terminado.

Este enfoque es especialmente útil en entornos colaborativos o de producción, asegurando la consistencia y minimizando los problemas de dependencia.

Para crear un entorno virtual de Python, ejecute el siguiente comando en su terminal:

```bash
python -m venv venv
```

Esto creará un nuevo directorio llamado `venv` que contiene el entorno virtual.

Para activar el entorno virtual:

- En Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- En macOS/Linux/terminal bash:
  ```bash
  source .venv/bin/activate
  ```

Una vez activado, puede instalar paquetes usando `pip` y estarán aislados en este entorno.

Para desactivar el entorno virtual de Python, simplemente ejecute:

```bash
deactivate
```

Esto devolverá su terminal al entorno global de Python.


### Clonar este repositorio

Para clonar este repositorio en su máquina local, abra su terminal y ejecute:

```bash
git clone https://github.com/StructuralWizard/10DiasDePython_es.github.io.git
```

Esto creará una copia local del repositorio en su directorio actual.

### Instalar las dependencias de este repositorio
Para instalar las dependencias enumeradas en `requirements.txt`, asegúrese de que su entorno virtual esté activado, luego ejecute:

```bash
pip install -r requirements.txt
```

Esto instalará todos los paquetes de Python necesarios para el proyecto.

### Ejecutar el sitio en un servidor local
Este sitio ha sido creado usando el tema [Just the Docs] y alojado en [GitHub Pages]. Puede [Navegar por nuestra documentación] para obtener más información.

Para visualizar el sitio de github en el navegador en lugar de editar su markdown, puede ejecutar `bundle exec jekyll serve` desde la carpeta principal de 10DaysOfCode donde tiene el archivo _config.yml.

Suponiendo que [Jekyll] y [Bundler] están instalados en su computadora:

1.  Cambie su directorio de trabajo al directorio raíz de su sitio.

2.  Ejecute `bundle install`.

3.  Ejecute `bundle exec jekyll serve` para construir su sitio y previsualizarlo en `localhost:4000`.

    El sitio construido se almacena en el directorio `_site`.


Nota: Si está utilizando una versión de Jekyll inferior a 3.5.0, use la clave `gems` en lugar de `plugins`.



----

[Visual Studio Code]: https://code.visualstudio.com/
[Github Copilot]: https://code.visualstudio.com/docs/copilot/overview
[python]: https://www.python.org/downloads/
[Jekyll]: https://jekyllrb.com
[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[GitHub Pages]: https://docs.github.com/en/pages
[Bundler]: https://bundler.io
[10 Días de Python con IA]: https://youtube.com/@10diasdepythonconia?si=WBjCQ5O0CzIxm8Mg
[Structural Wizard]: https://github.com/StructuralWizard/ 
[notas del curso 10 Días de Código con IA]: https://structuralwizard.github.io/10DiasDePython_es.github.io/
[ejemplos de código de git hub]: https://github.com/StructuralWizard/10DiasDePython_es.github.io/tree/main/_python_code
[Inglés]: https://structuralwizard.github.io/10DaysOfCode.github.io/
[Español]: https://structuralwizard.github.io/10DiasDePython_es.github.io/
[Portugués]: https://structuralwizard.github.io/10DiasDePython_pt.github.io/
