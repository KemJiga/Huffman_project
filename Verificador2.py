def are_files_equal(file_path_1, file_path_2):
    with open(file_path_1, 'r') as file1, open(file_path_2, 'r') as file2:
        for line1, line2 in zip(file1, file2):
            if line1 != line2:
                return False
        if file1.readline() != file2.readline():
            return False
    return True

print(are_files_equal("LaBiblia.txt", "descomprimiedo_elmejorprofesor.txt"))