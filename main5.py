# main5.py

# Modos de apertura de archivos en Python:
# - 'r': Modo de solo lectura.
# - 'w': Modo de escritura, sobrescribe el archivo si existe, crea uno nuevo si no existe.
# - 'a': Modo de escritura, añade al final del archivo si existe, crea uno nuevo si no existe.
# - 'b': Modo binario, para trabajar con archivos binarios.
# - 't': Modo de texto, el modo predeterminado que se usa si no se especifica ningún modo.
# - '+': Modo de actualización, permite leer y escribir en el archivo.

# Puedes combinar los modos según tus necesidades. Por ejemplo:
# - 'rb': Modo binario de solo lectura.
# - 'w+': Modo de escritura y lectura, sobrescribe el archivo si existe, crea uno nuevo si no existe.
# - 'a+t': Modo de escritura y lectura de texto, añade al final del archivo si existe, crea uno nuevo si no existe.

# Importar el módulo os para obtener la ruta absoluta del archivo
import os

# Obtener la ruta absoluta del archivo quixot.txt
ruta_absoluta = os.path.abspath("quixot.txt")

# Abrir el archivo quixot.txt en modo de solo lectura (modo 'r') con direccionamiento absoluto
with open(ruta_absoluta, 'r') as archivo:
    # Leer los primeros 11 caracteres del archivo
    primeros_11_caracteres = archivo.read(11)
    # Mostrar los primeros 11 caracteres por pantalla
    print(primeros_11_caracteres)

    contenido = archivo.read()
    # Dividir el contenido en palabras
    palabras = contenido.split()
    # Mostrar las tres primeras palabras por pantalla
    print(" ".join(palabras[:3]))

def leer_tres_primeras_palabras(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        return " ".join(palabras[:3])

primeras_tres_palabras = leer_tres_primeras_palabras("prova.txt")
print("Las tres primeras palabras del archivo prova.txt son:", primeras_tres_palabras)

def leer_dos_primeras_lineas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline().strip()
        segunda_linea = archivo.readline().strip()
        return primera_linea, segunda_linea

primera_linea, segunda_linea = leer_dos_primeras_lineas("quixot_extended.txt")
print("Las dos primeras líneas del archivo quixot_extended.txt son:")
print(primera_linea)
print(segunda_linea)

# Copiar el contenido de quixot_extended.txt a quixot_extended2.txt
with open("quixot_extended.txt", 'r') as file:
    content = file.read()

with open("quixot_extended2.txt", 'w') as file:
    file.write(content)

# Abrir quixot_extended2.txt en modo escritura para añadir las dos líneas adicionales
with open("quixot_extended2.txt", 'a') as file:
    file.write("\n")  # Agregar una nueva línea antes de escribir las líneas adicionales
    file.write("capítol 3\n")
    file.write("Aquest capítol ha estat generat per un programa\n")

with open("quixot_extended2.txt", 'r') as file:
    contenido_final = file.read()
    print("Contenido de quixot_extended2.txt:")
    print(contenido_final)