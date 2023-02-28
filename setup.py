# Este archivo creado en la raiz del paquete es para instalar el paquete mensajes (de manera local) en python 
# para poder utilizarlo en cualquier otro lado

# Lo que vamos a hacer aca es crear una configuracion para la biblioteca setup tools

from setuptools import setup

setup(
    name = 'mensajes',
    version = '1.1', # Antes tenia el 1.0
    description = 'Un paquete para saludar y despedir',
    author = 'Joaquin Corbo Pereira',
    author_email = 'jokin5249149@gmail.com',
    url = '',
    packages = ['mensajes', 'mensajes.hola', 'mensajes.adios'], # Escribo los paquetes y subpaquetes
    scripts = ['test.py']
)

# En la terminal ejecutamos el fichero con el siguiente comando: python3 setup.py sdist
# Para instalar el paquete, en la terminal entramos a la carpeta dist e instalamos el archivo mensajes-1.0.tar.gz 
# de la siguiente manera: pip install mensajes-1.0.tar.gz

# Si hacemos cambios y queremos actualizar la version lo que hacemos es modificar el "setup" e instalar de la misma manera
# con el comando: python3 setup.py sdist, despues lo upgradeamos entrando a la carpeta dist
# y usamos el siguiente comando: pip install mensajes-1.1.tar.gz --upgrade

# Para borrar el paquete usamos el comando: pip uninstall mensajes