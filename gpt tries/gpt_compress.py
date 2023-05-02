import heapq
import pickle

def build_huffman_tree(freq_dict):
    heap = [[weight, [char, '']] for char, weight in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low1, node1 = heapq.heappop(heap)
        low2, node2 = heapq.heappop(heap)
        for pair in node1:
            pair[1] = '0' + pair[1]
        for pair in node2:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low1 + low2, node1 + node2])
    return sorted(heapq.heappop(heap)[1], key=lambda x: (len(x[-1]), x))

def build_frequency_dict(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def encode_text(text, huffman_codes):
    encoded_text = ''
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text

def compress_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        text = input_file.read()
    freq_dict = build_frequency_dict(text)
    huffman_codes = dict(build_huffman_tree(freq_dict))
    encoded_text = encode_text(text, huffman_codes)
    with open(output_file_path, 'wb') as output_file:
        pickle.dump((huffman_codes, encoded_text), output_file)

input_file_path = 'sample.txt'
output_file_path = 'sample.bin'
compress_file(input_file_path, output_file_path)
