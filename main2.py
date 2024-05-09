import modul1
from modul2 import adeu, dia2, temps2

saludo1 = modul1.hola(modul1.dia)
print(saludo1)

saludo2 = modul1.hola(modul1.dia, modul1.temps)
print(saludo2)

despedida1 = adeu(dia2)
print(despedida1)

despedida2 = adeu(temps2)
print(despedida2)
