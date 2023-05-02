import heapq
import pickle

def build_huffman_tree(huffman_codes):
    heap = [[len(code), char] for char, code in huffman_codes.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low1, node1 = heapq.heappop(heap)
        low2, node2 = heapq.heappop(heap)
        heapq.heappush(heap, [low1 + low2, (node1, node2)])
    return heap[0][1]

def decode_text(encoded_text, huffman_tree):
    decoded_text = ''
    node = huffman_tree
    for bit in encoded_text:
        node = node[bit]
        if isinstance(node, str):
            decoded_text += node
            node = huffman_tree
    return decoded_text

def decompress_file(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as input_file:
        huffman_codes, encoded_text = pickle.load(input_file)
    huffman_tree = build_huffman_tree(huffman_codes)
    decoded_text = decode_text(encoded_text, huffman_tree)
    with open(output_file_path, 'w') as output_file:
        output_file.write(decoded_text)

input_file_path = 'sample.bin'
output_file_path = 'sample_decompressed.txt'
decompress_file(input_file_path, output_file_path)
