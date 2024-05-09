import sys

builtin_modules = sys.builtin_module_names

print("Módulos incorporados por defecto en Python:")
for module in builtin_modules:
    print(module)

# main4.py

# Modos de apertura de archivos en Python:
# - 'r': Modo de solo lectura. Permite leer el contenido de un archivo existente.
# - 'w': Modo de escritura. Crea un nuevo archivo si no existe o sobrescribe el archivo existente.
# - 'a': Modo de añadir al final del archivo. Permite escribir al final de un archivo existente o crear uno nuevo si no existe.
# - 'b': Modo binario. Se utiliza junto con los modos anteriores para trabajar con archivos binarios.
# - 't': Modo de texto. Es el modo predeterminado y se utiliza para archivos de texto.

# La letra que identifica los diferentes modos de escritura es:
# - 'r', 'w' y 'a': Para leer, escribir y añadir al final del archivo, respectivamente.

# Diferencia entre abrir y crear un archivo:
# - Abrir un archivo ('r', 'w', 'a') simplemente lo abre para su lectura o escritura, respectivamente.
# - Crear un archivo ('w', 'a') también lo abre para escritura, pero si el archivo no existe, lo crea; si existe, lo sobrescribe o añade contenido al final según el modo.

