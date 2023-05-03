# Dictionary is collection of key value pairs

dict1 = {"key1": 12, "key2": 22}
# OR
dict2 = dict(x=1, y=2)

print(dict2["x"])  # we can access values only by key # output : 1

# updating the value of key as below:
dict1["key1"] = 14
print(dict1)  # {'key1': 14, 'key2': 22}
# dict1["xyz"]  # if key doesnt exists : KeyError: 'xyz'

# to avoid the above error, always check if key exists before getting the value by using key
inputKey = "y"
if inputKey in dict2:
    print(dict2[inputKey])  # 2

# OR one more way of above check is ,:
print(dict2.get("r", 0))  # its kind of getOrElse from Scala : Ouput = 0

# If you want to delete a key
del dict2["y"]
print(dict2)  # {'x': 1}

# iterating a keys dictionary
for key in dict1:
    print(key)
# key1
# key2


# iterating a values dictionary
for value in dict1.values():
    print(value)
# 14
# 22

# iterating a both from dictionary
for key, value in dict1.items():
    print(key, value)
# key1 14
# key2 22
