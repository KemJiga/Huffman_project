from huffman import HuffmanCoding
import time

path = "LaBiblia.txt"

h = HuffmanCoding(path)

st = time.time()
output_path = h.compress()
ft = time.time()
print("Compressed file path: " + output_path + "\n Time: " + str(round(ft-st)) + "s")
