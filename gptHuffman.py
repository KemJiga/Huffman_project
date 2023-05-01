# Python3 code to demonstrate working of
# Interconversion between Dictionary and Bytes
# Using encode() + dumps() + decode() + loads()
import json

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using encode() + dumps() to convert to bytes
res_bytes = json.dumps(test_dict).encode('utf-8')

# printing type and binary dict
print("The type after conversion to bytes is : " + str(type(res_bytes)))
print("The value after conversion to bytes is : " + str(res_bytes))

# using decode() + loads() to convert to dictionary
res_dict = json.loads(res_bytes.decode('utf-8'))

# printing type and dict
print("The type after conversion to dict is : " + str(type(res_dict)))
print("The value after conversion to dict is : " + str(res_dict))
