import filecmp

#f1 = input("f1:")
#f2 = input("f2:")

f1 = "sample.txt"
f2 = "sample_decompressed.txt"

# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
