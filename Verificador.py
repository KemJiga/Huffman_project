#f1 = input("f1:")
#f2 = input("f2:")

f1 = "LaBiblia.txt"
f2 = "LaBiblia_decompressed.txt"

def compare_text_files(file1_path: str, file2_path: str) -> bool:
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        return file1.read() == file2.read()
    
print(compare_text_files(f1,f2))
