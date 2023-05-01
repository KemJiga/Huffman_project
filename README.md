# Huffman_project

El codigo principal esta en el archivo huffman.py

si corren el compresor no debe haber problema

el descompresor es el que presenta problemas

Problema:
si se corren la comprimida y descomprimida por separado, el diccionario que es usado para codificar y decodificar los caracteres no es trasladado en el archivo comprimido.

Solucion teorica:
añadir la informacion del diccionario al comprimido y luego esa informacion descomprimirla.

problema de la implementacion:
como el comprimido es un archivo binario, debemos saber como comprimir el diccionario y su tamaño en el mismo binario para luego en el proceso de descompresion extraer el tamaño y los bytes del diccionario. si obtenemos el diccionario sin problemas, podemos usar la funcion de descompresion que esta en huffman.py 

puche me recomendo usar el modulo pickle
