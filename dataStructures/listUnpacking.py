numbers = list(range(20))

print(numbers)

# Not a good way to assgin like this

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

first, second, *rest = numbers
print(first)
print(second)
print(rest)


def multiplyWith10(nums):
    return [x * 10 for x in nums]


print(multiplyWith10(numbers))

my_list = [2, 4, 6]
result = [item * 10 for item in my_list]
print(result)  # 👉️ [20, 40, 60]
