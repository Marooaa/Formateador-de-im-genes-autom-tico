# Formateador-de-im-genes-autom-tico
Escanea imágenes, quita el fondo y lo sustituye por otro blanco, y redimensiona la imagen a la resolución deseada. (default: 1000x1000)


Tutorial para Configurar y Ejecutar un Script en Python para Procesar Imágenes

Este tutorial detalla cómo configurar el entorno para eliminar el fondo de imágenes y añadir un fondo blanco mediante Python.

Requisitos Previos

Python 3.11: Descarga e instala Python 3.11 desde el sitio oficial. Asegúrate de seleccionar la opción "Add Python to PATH" durante la instalación.

Visual Studio Build Tools: Instala Visual Studio Build Tools para evitar errores relacionados con la compilación de ciertas librerías:

Ve a la página de descarga de Visual Studio Build Tools.

Descarga e instala la herramienta.

Durante la instalación, selecciona la opción "Desktop development with C++".

Configuración del Entorno

Crear y Activar un Entorno Virtual: Abre una terminal y ejecuta los siguientes comandos:

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

Actualizar pip: Asegúrate de tener la última versión de pip:

pip install --upgrade pip

Instalar Dependencias Necesarias: Ejecuta el siguiente comando para instalar las librerías requeridas:

pip install pillow numpy rembg

Estructura de Archivos

Organiza tus archivos de la siguiente manera:

project-folder/
│
├── input/              # Carpeta para imágenes originales
├── output/             # Carpeta para imágenes procesadas
├── script.py           # El script para procesar imágenes
└── venv/               # Entorno virtual

Crea las carpetas input y output manualmente dentro del directorio del proyecto.

Uso del Script

Coloca las imágenes originales en la carpeta input.

Ejecuta el script desde la terminal:

python script.py

Las imágenes procesadas se guardarán en la carpeta output con fondo blanco.

Resolución de Problemas

Error de Compilación: Si encuentras errores como "Microsoft Visual C++ 14.0 or greater is required", asegúrate de haber instalado Visual Studio Build Tools con la opción "Desktop development with C++".

Versiones de Python: Asegúrate de usar Python 3.11. Puedes verificar tu versión con:

python --version

Librerías Adicionales: Si alguna librería no se encuentra, instala manualmente utilizando pip install nombre_libreria.

¡Y eso es todo! Ahora tu entorno está configurado y listo para procesar imágenes con Python.
