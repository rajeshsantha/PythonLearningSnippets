try:
    name = input("Name: ")
    age = int(input("Age: "))
    print("hi! ", name, ":  your age is ", age)
except ValueError as ex:
    print("entered invalid age. ", ex)
else:
    print("No exceptions reported")  # only in case no exceptions raised
print("Execution contiues")

# Name: rajesh
# Age: 21q
# entered invalid age.  invalid literal for int() with base 10: '21q'
# Execution contiues
