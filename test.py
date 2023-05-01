import pickle
val = pickle.dumps(int(75))
print(val.__len__())

dic = {"a":2, "b":5, "c":8}

val2 = pickle.dumps(dic)

with open("test.bin", "wb") as file:
    file.write(bytes(val))
    file.write(bytes(val2))
    file.close()

with open("test.bin", 'rb') as file:
    sz_dic = file.read(20)
    print(sz_dic)
    #print(pickle.loads(sz_dic))
    file.close()

   






