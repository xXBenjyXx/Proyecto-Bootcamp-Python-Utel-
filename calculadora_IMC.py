# Programa para calcular el "Indice de masa corporal"

"""  Tabla de clasificacion de IMC

<15.99 -- Delgadez severa.
>16.00 <16.99 -- Delgadez moderada.
>17.00 <18.49 -- Delgadez leve.
>18.50 <24.99 -- Normal
>25.00 <29.99 -- Sobrepeso
>30.00 <34.99 -- Obesidad leve
>35.00 <39.00 -- Obesidad media
>40.00 -- Obesidad morbida

"""

# funcion para calcular el IMC peso entre la altura al cuadrado
def cal_IMC(p, a):
    return p / (a * a)

# esta funcion sirve para catalogar el IMC con el numero calculado de la funcion anterior
def categoria_de_peso(IMC):
    if IMC <15.99:
        return "Delgadez severa"
    elif 16.00 <= IMC <= 16.99:
        return "Delgadez moderada"
    elif 17.00 <= IMC <= 18.49:
        return "Delgadez leve"
    elif 18.50 <= IMC <= 24.99:
        return "Normal"
    elif 25.00 <= IMC <= 29.99:
        return "Sobrepeso"
    elif 30.00 <= IMC <= 34.99:
        return "Obesidad leve"
    elif 35.00 <= IMC <= 39.00:
        return "Obesidad media"
    elif  IMC > 40.00:
        return "Obesidad morbida" 

# mensaje de bienvenida al usuario
    
print("Bienvenido a su calculadora de Indice de Masa Corporal (IMC) ")

# Utilice los While True para un ciclo que no permita al usuario saltar la secuencia de ingreso y captura de datos

while True:
    try:
        name_s = str(input("¿Cual es su nombre(s)?: "))#Guardamos los datos ingresados en la variable "name_s"
        while not name_s: # si el usuario presiona enter sin ingresar ningun nombre ejecutaremos el while anidado
            print("\t ¿Error!: Debe ingresar su nombre \n") #imprimiremos un mensaje de error 
            name_s = str(input("¿Cual es su nombre(s)?: ")) # pediremos que vuelva a ingresar su nombre
        else: #una vez que ingrese su nombre saldremos el while principal
             break
    except (ValueError, TypeError, IndexError): #esta parte del codigo funciona si el usuario provoca algun tipo de error, se le pedira ingresar su nombre de nuevo
        print ("\t ¡Error!: debe ingresar su nombre \n")
"""
basicamente utilice el mismo concepto para el resto de inputs, en el caso de los float e int si no son del
tipo de dato correcto se enviara un mensaje de error y volvera a pedir la captura del dato
evitando que el usuario deje espacios en blanco o ingrese letras en lugar de numeros
"""

while True:
    try:
        frist_n = str(input("ingrese su apellido paterno: "))
        while not frist_n:
            print("\t ¿Error!: Debe ingresar su apellido paterno \n")
            frist_n = str(input("ingrese su apellido paterno: "))
        else:
            break
    except (ValueError, TypeError, IndexError):
        print ("\t ¡Error!: debe ingresar apellido \n")

while True:
    try:
        last_n = str(input("ingrese su apellido materno: "))
        while not last_n:
            print("\t ¿Error!: Debe ingresar su apellido materno \n")
            last_n = str(input("ingrese su apellido materno: "))
        else:
            break
    except (ValueError, TypeError, IndexError): 
        print ("\t ¡Error!: debe ingresar su apellido \n")

while True:
    try:
        weight = float(input("Ingrese su peso (Kg): "))
        while weight <= 0 or weight > 600:
            print("\t ¡Error!: ingrese un peso valido \n")
            weight = float(input("Ingrese su peso (Kg): "))
        else:
            break
    except (ValueError, TypeError, IndexError):
        print ("\t ¡Error!: ingrese su peso en Kg (Numero decimal) \n")

while True:
    try:
        age = int(input("Cuantos años tiene: "))
        while age <= 0 or age > 150:
            print("\t ¡Error!: ingrese una edad valida \n")
            age = int(input("Cuantos años tiene: "))
        else:
            break
    except (ValueError, TypeError, IndexError):
        print ("\t ¡Error!: ingrese su edad como un Numero \n")

height = 0
while True:
    try:
        height = float(input("Ingrese su altura (m): "))
        while height <= 0 or height > 3:
            print("\t ¡Error!: ingrese una altura valida \n")
            height = float(input("Ingrese su altura (m): "))
        else:
            break
    except (ValueError, TypeError, IndexError):
        print ("\t ¡Error!: ingrese su altura como un numero decimal \n")
        
# mostramos al usuario los datos ingresados junto con su IMC
print(f" Hola usuario: {name_s} {frist_n} {last_n} su edad es: {age} años, su peso de: {weight} Kg, y su altura: {height} m. \n Su categoria de IMC:", categoria_de_peso( cal_IMC(weight, height)))

#fin del programa
print("\n \n \t El programa ha finalizado \n")
