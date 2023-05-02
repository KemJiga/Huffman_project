import time
###############################################################################################
##                                 Descompresor Mágico                                       ##
###############################################################################################
start_time = time.time()

# Usamos una función para pasar de base 64 a binario y definir nuestro abecedario
def base64_to_bin(base64_num):
  # Creamos la cadena de referencia para la conversión a base 64
  base64_ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
  # Convertimos la cadena en base 64 en una lista de números decimales
  decimal_nums = [base64_ref.index(char) for char in base64_num]
    
  # Convertimos cada número decimal en una cadena binaria de 6 bits
  binary_chunks = [format(num, "06b") for num in decimal_nums]
    
  # Unimos todas las cadenas binarias para formar el número binario completo
  binary_str = "".join(binary_chunks)   
  # Aseguramos que la longitud del número binario sea un múltiplo de 8
  pos = 0
  for i in range(8):
    if binary_str[0] =="0":
      binary_str = binary_str[1:]     
    else:
      break
  return binary_str

# Leemos nuestro archivo comprimido y lo separamos por el indice que usamos para separarlos "@"
hexi = []
lin = open(r"/workspaces/Compresor_Descompresor/Archivos/comprimido.elmejorprofesor", "r", encoding="latin-1").read()
linea = lin.split("@")

# Hacemos un ciclo para leer todas las lineas del archivo hasta el ultimo caractér
letter_binary2 = {}
i=0
while i < len(linea)-2 :
  letter_binary2[linea[i+1]]=linea[i]
  i=i+2
wr =linea[len(linea)-2] + base64_to_bin(linea[len(linea)-1])

uncompressed_string = ""
code = ""

for digit in wr:
  code = code+digit
  if code in letter_binary2:    
    uncompressed_string = uncompressed_string+letter_binary2[code]
    code = ""        

# Se guarda el archivo en la ubicación especificada
fic = open(r"/workspaces/Compresor_Descompresor/Archivos/descomprimido-elmejorprofesor.txt", "w", encoding="latin-1")
fic.write(uncompressed_string)
fic.close()

# Indicadores
print("Archivo descomprimido exitosamente")
end_time = time.time()
tiempo_ejecucion = end_time - start_time
tiempo_ejecucion_r = round(tiempo_ejecucion, 2)
print("El tiempo de ejecución fue:",tiempo_ejecucion_r,"segundos")