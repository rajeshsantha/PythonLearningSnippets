try:
    file = open("exceptions01.py")
    print("File is opened..")
    age = int(input("Age: "))

except (ValueError, ZeroDivisionError) as ex:
    print("entered invalid age. ", ex)
else:
    print("No exceptions reported")  # only in case no exceptions raised
finally:
    file.close()
    print("cleaned up the resources")


print("Execution contiues")


# File is opened..
# Age: 23
# No exceptions reported
# cleaned up the resources
# Execution contiues

# File is opened..
# Age: ihjk
# entered invalid age.  invalid literal for int() with base 10: 'i'
# cleaned up the resources
# Execution contiues
