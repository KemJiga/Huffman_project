from huffman import HuffmanCoding
import time, sys

#path = "sample.txt"
path = sys.argv[1]

h = HuffmanCoding(path)

st = time.time()
output_path = h.compress()
ft = time.time()
print("Compression time: " + str(round(ft-st, 5)) + "s")
