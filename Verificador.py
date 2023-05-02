#f1 = input("f1:")
#f2 = input("f2:")

f1 = "LaBiblia.txt"
f2 = "descomprimiedo_elmejorprofesor.txt"

def compare_text_files(file1_path: str, file2_path: str) -> bool:
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        val = file1.read() == file2.read()
        if val:
            return "ok"
        else:
            return "nok"
    
print(compare_text_files(f1,f2))
