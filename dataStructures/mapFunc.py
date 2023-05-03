# map() is used to transform one item to another item based on given logic
# It will take one element from the list at a time,
# and apply the logic on top of it ,
# create a new value and placed it in the collection (list,set...)


items = [
    ("product1", 10),
    ("product2", 88),
    ("product3", 34)
]

# From the above list if we only want to prices.

# 1. first we use without map()

# Take new empty list to store prices
prices = []
# iterate each item one at a time and add it to `prices` list
for item in items:
    prices.append(item[1])

print(prices)

# 2. This time we use map(). which is ideal and readable
prices_ = list(map(lambda item: item[1], items))

# UNDERSTANDING SYNTAX:

# (lambda item: item[1], items) : HERE `items` is the collection. `item` is the local variable for lambda function
# map(lambda item: item[1], items)) : map(lambdaFunc) means it will transform the each item in the collection `items`
# list(map(lambda item: item[1], items)) : list(map(lambda)) means: it will going to place each newly created value in a new list

print(prices_)


# Exercise 1: reduce the price of items by 5
newItems = list(map(lambda item: (item[0], item[1]-5), items))
print(newItems)
