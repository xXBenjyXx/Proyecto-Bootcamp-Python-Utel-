# Proyecto-Bootcamp-Python-Utel-

Esta es una calculadora de indice de masa corporal.
Entregada como requisito de primer proyecto de bootcamp fundamentos de python.

En el programa como comentario se muestra una tabla de clasificacion de IMC.

Apartir de la linea 17 del codigo, declaramos la primera funcion que utilzaremos,
la cual nos sirve para calcular el IMC como un numero
atravez de la formula: "peso/ altura elevado al cuadrado"

La segunda funcion en la linea 21, nos sirve para, atravez del numero obtenido
del calculo anterior, se pueda clasificar el IMC.
Utilizamos condicionales "if" para calcular el IMC del usuario y saber asi, dentro de cual categoria 
entra el usuario, devolviendo en cada caso la categoria como string.

En la linea 41 se le da la bienvenida al usuario al programa. el mensaje de salida
muestra el nombre del programa para que el usuario sepa que podemos calcular su IMC.

Apartir de la Linea 45 y hasta la 115 del codigo estaremos pidiendo al usuario que
ingrese sus datos.
estos datos son:
Nombre, Apellido paterno, aellido materno, su peso, edad y su altura.

Utilizamos "While True" para crear un ciclo por cada dato ingresado.
Usando "Try y execpt" para manejar los errores: 
mostramos un input el cual le pedira al usuario que ingrese su nombre. 
(igual con los demas datos) y lo guardaremos en una variable. 
(transformando el dato de string a float e int segun requiera el caso)

Con "while not" validamos que el usuario no deje el espacio del nombre vacio.
(igual con los demas datos).
Si el usuario deja el espacio vacio, mostramos un mensaje de error y le pediremos que vuelva a
ingresar el dato correcto. Una vez que el usuario ingrese el dato correctamente,
utilizaremos un else con un break para romper ciclo del while. asi seguiremos con la
ejecucion del programa.

Se utiliza la misma estructura para los demas inputs, en el caso de las variables:
"age, weight y height" utilizaremos tambien un while que condicione la edad, 
el peso y la altura como numeros "validos" evitando el uso de numeros negativos 
y superiores a lo humanamente posible.

ejemplo: el humano resgistrado con mas peso segun los record guiness pesaba
594.8 Kg, por lo que el limite del programa es de 600 kg. 
tambien restringimos la edad a 150 años, 
y la altura a 3 metros.
el limite inferior para estas tres variables es 0.
Evitamos tambien numeros negativos y evitamos que el usuario ingrese letras en lugar
de numeros gracias al manejo de error con "try y execpt".

Para finalizar imprimimos en pantalla una cadena de texto con formato.
Mostrando los datos ingresados por el usuario y dandole su clasificacion de IMC.
finalmente informamos que el programa finalizo.

En este curso he aprendido: 
A manejar de manera sencila el ingreso de datos para un formulario,
decalracion de variables, tipos de datos, como declarar una funcion
condicionales, ciclos, manejo de errores simples
y como funionan algunas de las palabras reservadas para el lenguaje python.
espero que sigan eseñandonos mas de como utilizar este lenguaje.
