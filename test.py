# Con "import saludos" importamos todo el modulo
# Con "from saludos import saludr" importamos una def que querramos del modulo, si quisieramos mas ponemos comas o un * para todas

# La carpeta "mensajes" es un paquete que contiene los modulos y el fichero __init__
# Este fichero lo que hace es que al ejecutar el programa va a buscarlo y es lo primero que va a ejecutar,
# por eso se ve el mensaje de "Cargando" al inicio

# La carpeta "hola" es un subpaquete ya que esta adentro de "mensajes" que es un paquete
# Por ejemplo en el paquete "hola" tendriamos los modulos para dar mensajes que sean saludos
from mensajes.hola.saludos import *
from mensajes.adios.despedidias import *

saludar()
Saludo()
despedir()
Despedida()