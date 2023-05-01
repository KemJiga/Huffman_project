import filecmp

f1 = input("f1:")
f2 = input("f2:")

# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
