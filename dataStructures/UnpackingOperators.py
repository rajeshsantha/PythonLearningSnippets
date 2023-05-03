numbers = [1, 2, 3]
print(*numbers)  # 1 2 3
print(1, 2, 3)  # 1 2 3

values = list(range(5))
print(values)  # [0, 1, 2, 3, 4]


values = [*range(5), *"Hello"]  # `*` generated a list from the String "hello"
print(values)  # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']


first = [1, 2]
second = [3, 4]

# unpacking multple collection and merging together
values = [*first, *"abcd", *second, *"Rajesh"]
print(values)  # [1, 2, 'a', 'b', 'c', 'd', 3, 4, 'R', 'a', 'j', 'e', 's', 'h']


# unpacking dictionary
first = dict(x=1)
second = dict(x=10, y=20)
combined = {**first, **second}
# {'x': 10, 'y': 20} Since the key is same in both , it took the last occurance value i.e x =10
print(combined)


combined2 = {**first, **second, "z": 45}
print(combined2)  # {'x': 10, 'y': 20, 'z': 45}
