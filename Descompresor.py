from huffman import HuffmanCoding
import time

path = "comprimido.elmejorprofesor"

h = HuffmanCoding(path)

st = time.time()
output_path = h.decompress(path)
ft = time.time()
print("Decompression time: " + str(round(ft-st, 5)) + "s")
