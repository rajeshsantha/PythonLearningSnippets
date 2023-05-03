values = []
for x in range(5):
    values.append(x*5)

print(values)  # [0, 5, 10, 15, 20]

# OR
values2 = [i*5 for i in range(5)]
print(values2)  # [0, 5, 10, 15, 20]


# Now for Dictionaries

dict1 = {i: i*20 for i in range(5)}
print(dict1)  # {0: 0, 1: 20, 2: 40, 3: 60, 4: 80}
