#Ejemplos de cadenas

# split para separar una cadena
cad= "La noche esta muy oscura"
cad.split()

#separacion en bloques con /
fecha = '17/05/2012'
datos = fecha.split('/') 
print datos

# la lista contiene los trozos, sin el separador
['17', '05', '2012']         
print 'día:', datos[0], 'mes:', datos[1], 'año:', datos[2]

# replace para reemplazar una parte de una cadena por otra
cadena = "Esto (hola) sera reemplazado: hola"
print cadena.replace('hola', 'hello')



