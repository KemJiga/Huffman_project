from huffman import HuffmanCoding
import time

path = "LaBiblia.txt"

h = HuffmanCoding(path)

st = time.time()
output_path = h.compress()
ft = time.time()
print("Compressed file path: " + output_path + "\n Time: " + str(round(ft-st)) + "s")

#st = time.time()
#decom_path = h.decompress("sample.bin")
#ft = time.time()
#print("Decompressed file path: " + decom_path + "\n Time: " + str(round(ft-st)) + "s")