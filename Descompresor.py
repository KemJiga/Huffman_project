from huffman import HuffmanCoding
import time
import sys

#path = "comprimido.elmejorprofesor"
path = sys.argv[1]

h = HuffmanCoding(path)

st = time.time()
output_path = h.decompress(path)
ft = time.time()
print(ft-st)
