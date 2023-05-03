# Tuple is kind a read only list that will store different values together.

point1 = 1, 2
print(point1)  # (1, 2)

point2 = 1,
print(point2)  # (1,)

print(point2)  # (1,)

emptyTuple = ()
print(type(emptyTuple))  # <class 'tuple'>

point3 = (1, 2) + (4, 5)
print(point3)  # (1, 2, 4, 5)


point4 = (1, 2) * 4
print(point4)  # (1, 2, 1, 2, 1, 2, 1, 2)

list1 = [1, 2]
tupleFromAList = tuple(list1)
print(type(tupleFromAList))  # <lass 'tuple'>
print(tupleFromAList)  # (1, 2)

# ACCESSING TUPLES

point5 = (1, 2, 3, 4, 5, 6, 7, 8)
print(point5[1])  # 2
print(point5[1:5])  # (2, 3, 4, 5)
# REVERSING : (8, 7, 6, 5, 4, 3, 2, 1) # same as list except removing and modifying
print(point5[::-1])


# We cannot remove / modify the elements in the tuple so we use tuples in scenarios where we do not accidentally want to change the elements in the collection.
