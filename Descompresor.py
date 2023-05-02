from huffman import HuffmanCoding
import time

path = "LaBiblia.bin"

h = HuffmanCoding(path)

st = time.time()
print("Descomprimiendo")
decom_path = h.decompress(path)
ft = time.time()
print("Decompressed file path: " + decom_path + "\n Time: " + str(round(ft-st)) + "s")