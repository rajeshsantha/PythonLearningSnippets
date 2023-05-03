# 1 perform a task

def greet():
    print("Hi!!  There ...")
    print("Welcome aboard")


def greetName(firstName, lastName):
    print(f"Hi!! {firstName} {lastName} ...")
    print("Welcome aboard")


greetName("Rajesh", 5)
greetName("Rajesh", True)


# 2 return a value

def getGreet(name):
    return f"Hi {name}"


# writing output to a file
message = getGreet("Rajesh")
file = open("content.txt", "w")
file.write(message)

print(greet())  # will return None

print("***********named args**********")


def increment(number, by):
    return number + by


# result = increment(number=2, by=1) // more readable named args
result = increment(2, 1)
print(result)

print("*********** Default args **********")

# all the default values are applied only for last paramters
# no non-default args after default args.


def incrementBy(number, by=1):
    return number + by


print(incrementBy(4, 10))
print(incrementBy(5))


print("*********** Xargs **********")


def multiply(x, y):
    return x*y


def multiplyVarArgs(*numbers):
    total = 1
    for n in numbers:
        total *= n
    return total


print(multiply(3, 4))
print(multiplyVarArgs(3, 4, 5))

print("*********** XXargs **********")

# **user is a dictionary


def save_user(**user):
    print(user["age"])


save_user(id=1, name="Rajesh", age=29)


print("*********** Scope **********")
message = "a"  # its a global variable : Dont use them often.


def greet_scopeDemo(NAME):
    global message  # its used to modify global variable. its a bad practice.
    message = 'b'  # local variable
    # NAME here is valid and in scope

# NAME here is out of scope and invalid


print(greet_scopeDemo("Rajesh"))
print(message)



