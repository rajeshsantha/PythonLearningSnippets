# finally clause is used as a standard to release resources
# But shorter and cleaner way is `with` statement as below
try:
    with open("exceptions01.py") as file1, open("CleaningUp.py") as file2:
        print("opened files are ..", file1.name, " and ", file2.name)
        # file.__exit__ # This method automatically called when we use with statement : used to release the resources
    age = int(input("Age: "))
except (ValueError, ZeroDivisionError) as ex:
    print("entered invalid age. ", ex)
except FileNotFoundError as fx:
    print("File cannot be found: ", fx)
else:
    print("No exceptions reported")  # only in case no exceptions raised
# finally:
#     file.close()
#     print("cleaned up the resources")
# REMOVED FINALLY CLAUSE AS WITH STATEMENT WILL TAKE CARE OF THIS
print("Execution contiues")


# RUN 1 : normally

# opened files are .. exceptions01.py  and  CleaningUp.py
# Age: 23
# No exceptions reported
# Execution contiues

# RUN 2 : given invalid filename C1leaningUp.py

# File cannot be found:  [Errno 2] No such file or directory: 'C1leaningUp.py'
# Execution contiues
