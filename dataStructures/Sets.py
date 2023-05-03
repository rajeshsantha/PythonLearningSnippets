# Sets are lists without duplicates (that comes with random ordering, so we cant access by using index)

numbers = [1, 2, 1, 3, 3, 4, 5]
uniques = set(numbers)
print(numbers)  # [1, 2, 1, 3, 3, 4, 5]
print(uniques)  # {1, 2, 3, 4, 5}

uniques.add(1)
uniques.remove(1)

first = {1, 2, 3, 6}
second = {1, 3, 5, 7}

# union
print(first | second)  # {1, 2, 3, 5, 6, 7}

# intersecion
print(first & second)  # {1, 3}

# minus
print(first - second)  # {2, 6}

# symmetric / exclusive
print(first ^ second)  # {2, 5, 6, 7}
