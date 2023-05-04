# try not to raise own exceptions for performance reasons
# The performance will be noticiable when the application scale increases.
# For exampel, here in timeit we mentioned number=10000 means it will calculate the time by executing the 10000 runs.
# The difference will not be noticiable if the number is very less
from timeit import timeit

code1 = """def calc_xfactor(age):
    if age <= 0:
        None
    return 10/age



xfactor = calc_xfactor(-1)
if xfactor == None:
    pass
"""

code2 = """def calc_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age


try:
    calc_xfactor(-1)
except ValueError as ex:
    pass#print(ex)
"""


print("Time taken for code1 execution: ", timeit(code1, number=10000))
print("Time taken for code2 execution: ", timeit(code2, number=10000))
print("Hello")

# Time taken for code1 execution:  0.0017641250015003607
# Time taken for code2 execution:  0.02324445800331887
