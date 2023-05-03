# If we are using large list of numbers , if we get any performance issue , then replace list with Array
# Array is efficient data strcuture than list for large list of values
from array import array
numbers = array("i", [1, 2, 3, 4, 5])
print(numbers)  # array('i', [1, 2, 3, 4, 5])
# Array is typed . i.e  during creation of array. here Int
# add
numbers.append(99)
# remove
numbers.remove(5)
# update
numbers[2] = 100
# TypeError: 'float' object cannot be interpreted as an integer
# numbers[2] = 100.0

print(numbers)
# array('i', [1, 2, 100, 4, 99])
