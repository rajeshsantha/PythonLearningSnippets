
# Python Basics for Scala Developers - 1 Week Crash Course

# Day 1: Basics & Data Types
a = 10
b = 3.14
s = "Hello"
is_valid = True

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n * n)

person = {"name": "Alice", "age": 30}
print(person["name"])

# Day 2: Functions, Args, and Scope
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))

def avg(*args):
    return sum(args) / len(args)

print("Average:", avg(10, 20, 30))

# Day 3: Classes (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name}"

p = Person("Bob", 25)
print(p.greet())

# Day 4: Modules and Libraries
import datetime
import math
import random
from collections import Counter

print(math.sqrt(16))
print(random.randint(1, 100))

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))

words = ["apple", "banana", "apple", "orange"]
print(Counter(words))

# Day 5: File I/O & Exceptions
with open("test.txt", "w") as f:
    f.write("Hello Python!\n")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)

try:
    x = int("abc")
except ValueError as e:
    print("Caught:", e)

# Day 6: Functional Style + Comprehensions
squares = [x*x for x in range(10) if x % 2 == 0]
print(squares)

nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))
print(doubled)

# Day 7: Mini Project
def process_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    names = []
    ages = []

    for line in lines:
        name, age = line.strip().split(",")
        names.append(name)
        ages.append(int(age))

    avg_age = sum(ages) / len(ages)
    common_name = Counter(names).most_common(1)[0][0]

    output_file = f"results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, "w") as out:
        out.write(f"Average Age: {avg_age}\n")
        out.write(f"Most Common Name: {common_name}\n")

    print(f"Results written to {output_file}")

# Uncomment to run with a sample file
# process_file("names.txt")
