list1 = ["a", "b", "c", "d", "e"]
numbers = list(range(20))


# get first element
print("get first element")
print(list1[0])

# get last element
print("get last element")
print(list1[-1])

# get list except first element
print("get list except first element")
print(list1[1:])

# get list except last element
print("get list except last element")
print(list1[:-1])

# get list from n index to to m index
print("get list from n index to to m index")
print(list1[2:4])

# get list from n index till end of the list
print("get list from n index till end of the list")
print(list1[2:-1])

# reverse the list
print("reverse the list")
print(list1[::-1])

# get list divide by number 'n'
print("get list divide by number 'n'")
print(numbers[::2])

# reverse the above list after getting even numbers without assgining a new variable
print("reverse the above list after getting even numbers without assgining a new variable")
print(numbers[::2][::-1])
