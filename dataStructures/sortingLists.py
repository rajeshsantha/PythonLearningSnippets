numbers = [4, 2, 74, 8, 34, 99, 35]

# numbers.sort() : This will not return any new list.
#  This will going to modify the original list and Return None
# Now `numbers` in line 1 is sorted
# so sort() is "inplace" modifier

print(numbers.sort())  # It will not return anything. i.e None
print(numbers)

# sort descending order
numbers.sort(reverse=True)
print(numbers)

# If you want a sort function that will not modify original input list
# and want to return a new sorted list use `sorted()`
print(sorted(numbers))
# sorted() reverse
print(sorted(numbers, reverse=True))

# sorting list of tuples: (complex objects)
items = [
    ("product1", 10),
    ("product2", 88),
    ("product3", 34)
]


def sort_items_function(item):
    return item[1]  # return price of product


items.sort(key=sort_items_function)
print(items)

# above implementation has a function called `sort_items_function` which we only used once here.
# We could have written an anonmous/unnamed function for that kind of temporary use.
# This is when you use lambda functions, refer file LambdaFunc.py
