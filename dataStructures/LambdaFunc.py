# Lambda is one line anonmyous function

# sorting list of tuples: (complex objects) by lambda
items = [
    ("product1", 10),
    ("product2", 88),
    ("product3", 34)
]

items.sort(key=lambda tempVariable: tempVariable[1])
print(items)
