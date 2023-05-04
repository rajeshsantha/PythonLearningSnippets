try:
    name = input("Name: ")
    age = int(input("Age: "))
    xfactor = 10 / age
    print("hi! ", name, ":  your age is ", age)

except (ValueError, ZeroDivisionError) as ex:
    print("entered invalid age. ", ex)
else:
    print("No exceptions reported")  # only in case no exceptions raised
print("Execution contiues")


# Name: ed
# Age: 0
# entered invalid age.  division by zero
# Execution contiues

# Name: sd
# Age: sad
# entered invalid age.  invalid literal for int() with base 10: 'sad'
# Execution contiues
