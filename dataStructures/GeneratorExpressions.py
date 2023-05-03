from sys import getsizeof
values = (i*2 for i in range(1000000))
# <class 'generator'> # like an iterator object in Scala , kind of lazy list for large collections
print(type(values))


print("gen:", getsizeof(values))  # gen: 104 : size is constant

for x in values:
    print(x)
