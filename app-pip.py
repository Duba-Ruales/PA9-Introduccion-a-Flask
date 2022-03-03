# Este es un comentario

"""
Este es un comentario de multiples lineas
"""

'''
Este es un comentario de multiples lineas
'''


# Variables
from array import array


nombrePersona = 'Duban' #de tipo string
edad = '20' #de tipo entero
numeroDecimal='10.2' #tipo float
esMayorEdad = True # Tipo False Bolean

#Debug
print(nombrePersona) # Mostraria Duban

# Array= Arreglos = Listas []

diasSemana = ['Lunes','Martes','Miercoles','Jueves'] #Esto es un arreglo o lista.
#Que imprima miercoles
print(diasSemana[2]) # Aqui se imprime dia Miercoles

#Array Multiple
arrayMultiple = [1,'hola',[5,6]]
#Imprimer en numero 6-->
print(arrayMultiple[2][1]) # Accedo al segundo arreglo e imprimi el numero 6


#Objetos
# se llaman JSON Diccionarios{}
persona={
    'nombre':'Duban',
    'apellido':'ruales',
    'edad':'20',
    'lenguaje':['python','Javascript']
}

# Acceder a un Diccionario e imprimir 
print(persona['nombre']) # Aqui imprime Duban
# imprima Javascript
print(persona['lenguaje'][1]) #Imprime posicion 1 de lenguaje en diccionario persona.


#----------------------------
#declaramos una lista de perslonas
personas = [
{
    'nombre':'Duban',
    'apellido':'ruales',
    'edad':'20',
    'lenguaje':['python','Javascript']
},
{
    'nombre':'Juan',
    'apellido':'Perez',
    'edad':'20',
    'lenguaje':['python','.net']
},
{
    'nombre':'Pepito',
    'apellido':'Perez',
    'edad':'20',
    'lenguaje':['python','rush']
},
]
#imprimimos .net
print(personas[1]['lenguajes'][1]) #aqui se imprime el .net


#lo ultimo: Preguntamos si es mayor de edad

#CONDICIONES:
if esMayorEdad == True:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')  #OJO LA TABULACION



    #TEMA DE CLASE 2

    #PIP_ instalador de paquetes
    #Entornos virtuales: Crea espacio libre de instalaciones
    #Flask_ frameword de desarrollo web

    #aplicaciones full stack_monolitos

    