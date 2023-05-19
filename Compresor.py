from huffman import HuffmanCoding
import time, sys

#path = "sample2.txt"
path = sys.argv[1]

h = HuffmanCoding(path)

st = time.time()
output_path = h.compress()
ft = time.time()
print(ft-st)
