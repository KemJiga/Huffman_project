import time
###############################################################################################
##                                    Compresor Mágico                                       ##
###############################################################################################
start_time = time.time()

# Se crea una lista de caracteres que va a tener cada linea del archivo a comprimir (Lines),
# luego usamos otra lista para guardar cada letra (my_string)
Lines = []
for line in open(r"/workspaces/Compresor_Descompresor/Archivos/LaBiblia.txt", 'r', encoding="latin-1").readlines():
  Lines.append(line)
my_string=[]
for h in Lines:
  for t in h:
    my_string.append(t)
len_my_string = len(my_string)

# Crea una lista de caracteres y la frecuencia de aparicion de cada uno
letters = []
only_letters = []
dic = {}

# Ciclo calcula la frecuencia con la que se repite un caracter
for letter in my_string:
  if letter not in only_letters:
    dic[letter] = 1
    only_letters.append(letter)
  else:
    dic[letter] +=1
for clave in dic:
  letters.append([dic[clave],clave])

# Genera la base de level para la frecuencia del arbol de Huffman
nodes = letters
nodes.sort()
huffman_tree = []

def sustituir_valores(arreglo, diccionario):
  # Crea una función lambda que devuelve el valor correspondiente del diccionario para una clave dada
  f = lambda x: diccionario[x] if x in diccionario else x

  # Aplica la función lambda al arreglo utilizando la función vectorizada map()
  resultado_lista = list(map(f, arreglo))

  # Retorna un string con todos los elementos del arreglo unidos
  return ''.join(resultado_lista)

def bin_to_base64(binary):
  # Convertimos la cadena binaria a una cadena de caracteres
  binary_str = str(binary)
    
  # Agregamos ceros a la izquierda para que la longitud sea divisible por 6
  while len(binary_str) % 6 != 0:
      binary_str = "0" + binary_str
    
  # Dividimos la cadena en grupos de seis caracteres
  chunks = [binary_str[i:i+6] for i in range(0, len(binary_str), 6)]
    
  # Convertimos cada grupo de seis caracteres en un número decimal
  decimal_nums = [int(chunk, 2) for chunk in chunks]
    
  # Convertimos cada número decimal en su equivalente en la tabla de caracteres de base 64
  base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  base64_str = "".join([base64_chars[num] for num in decimal_nums])
    
  return base64_str


def combine(nodes):

  htree = []
  while len(nodes)>1:
    pos = 0
    newnode = []
    nodes.sort()
    # Agrega el 1 o el 0 dependiendo si sube o baja de nivel
    nodes[pos].append("0")
    nodes[pos+1].append("1")
    huffman_tree.append(nodes[pos])
    huffman_tree.append(nodes[pos+1])
    combined_node1 = (nodes[pos][0]+nodes[pos+1][0])
    combined_node2 = ("@"+nodes[pos][1]+"@"+nodes[pos+1][1]+"@")
    newnode.append(combined_node1)
    newnode.append(combined_node2)
    newnodes = []
    newnodes.append(newnode)
    newnodes = newnodes + nodes[2:]
    nodes = newnodes
  huffman_tree.append(nodes[0])
  return huffman_tree

def aplicar_diccionario_binario(cadena, diccionario):
  # Invertir el diccionario para tener los códigos binarios como claves y las letras como valores
  diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}

  # Dividir la cadena en subcadenas de longitud menor o igual a la longitud máxima de los códigos binarios en el diccionario
  longitudes = set(len(cod_binario) for cod_binario in diccionario.keys())
  max_longitud = max(longitudes)
  subcadenas = [cadena[i:i+n] for i in range(0, len(cadena)) for n in longitudes if i+n <= len(cadena)]

  # Aplicar la función lambda a cada subcadena utilizando la función vectorizada map()
  f = lambda x: diccionario_invertido[x] if x in diccionario_invertido else x
  resultado_lista = list(map(f, subcadenas))

  # Unir las subcadenas resultantes en un solo string
  resultado = "".join(resultado_lista)

  # Retornar el string resultante
  return resultado
newnodes = combine(nodes)

# Hace que el arbol empiece descendentemente
huffman_tree.sort(reverse=True)
checklist = huffman_tree

# Construye un código binario para cada caracter
letter_binary = {}
if len(only_letters) == 1:
  letter_code = [only_letters[0], "0"]
  letter_binary.append(letter_code*len(my_string))
else:
  cont = 1
  for letter in only_letters:
    cont+=1
    lettercode = ""
    for node in checklist:
      if len(node) > 2 and ("@"+letter+"@" in node[1] or node[1] == letter):
        lettercode = lettercode + node[2]
    letter_binary[letter]=lettercode

# Letras con el código binario
arbol = ""
for lette in letter_binary:
  arbol = arbol+str(lette)+"@"+letter_binary[lette]+"@"

# Crea una secuencia de bits con los códigos nuevos
bitstring = ""
bitstring =sustituir_valores(my_string, letter_binary)
id = ""
for i in range(8):
  if bitstring[i] =="0":
    bitstring = bitstring[1:]
    id = id+"0"
  else:
    break
pint = bin_to_base64(bitstring)

# Generar archivo comprimido
fic = open(r"/workspaces/Compresor_Descompresor/Archivos/comprimido.elmejorprofesor", "w", encoding="latin-1")
fic.write(arbol+id+"@"+pint)
fic.close()

# Indicadores
print("Archivo comprimido exitosamente")
end_time = time.time()
tiempo_ejecucion = end_time - start_time
tiempo_ejecucion_r = round(tiempo_ejecucion, 2)
print("El tiempo de ejecución fue:",tiempo_ejecucion_r,"segundos")