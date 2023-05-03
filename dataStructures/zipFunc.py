list1 = [1, 2, 3]
list2 = [10, 20, 30, 40]

# combine lists

print(list(zip(list1, list2)))
# [(1, 10), (2, 20), (3, 30)]

print(list(zip("123", list1, list2)))
# [('1', 1, 10), ('2', 2, 20), ('3', 3, 30)]

print(list(zip("123456789", list1, list2)))
# [('1', 1, 10), ('2', 2, 20), ('3', 3, 30)]

# It will take the shortest list as base and merge the values into tuple according to the indexes.
