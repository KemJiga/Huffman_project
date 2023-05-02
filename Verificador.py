
###############################################################################################
##                                  Verificador Mágico                                       ##
###############################################################################################

Lines = []
for line in open(r"/workspaces/Compresor_Descompresor/Archivos/LaBiblia.txt", 'r', encoding="latin-1").readlines():
  Lines.append(line)
Lines2 = []
for line in open(r"/workspaces/Compresor_Descompresor/Archivos/descomprimido-elmejorprofesor.txt", 'r', encoding="latin-1").readlines():
  Lines2.append(line)
if(Lines == Lines2):
  print("Ok")
else:
  print("Nok")