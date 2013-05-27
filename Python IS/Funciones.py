from lib.operaciones import *
from lib.operaciones import HttpRequestResponeRedirect as RE


valor = float(raw_input('Ingresa un valor'))
valor2 = float(raw_input('Ingresa otro valor'))
operacion = raw_input('Que operacion desea realizar: {s - r - m - d}')

if operacion.lower() == 's':
        print suma(valor, valor2)
elif operacion.lower() == 'r':
        print resta(valor, valor2)

elif operacion.lower() == 'm':
        print multiplicar(valor, valor2)

elif operacion.lower() == 'd':
        print dividir(valor, valor2)

print RE







