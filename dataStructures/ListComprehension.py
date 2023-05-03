items = [
    ("product1", 10),
    ("product2", 88),
    ("product3", 34)
]


# to get prices of items from list of tuples
pricesWithMapfun = list(map(lambda i: i[1], items))
# is same as below
pricesWithListComprehension = [item[1] for item in items]

# get items with price more than 20
filteredWithFilterFunc = list(filter(lambda item: item[1] > 20, items))
# is same as below
filteredWithListComprehension = [item for item in items if item[1] > 20]
