# Custom exceptions

def calc_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age


try:
    calc_xfactor(-1)
except ValueError as ex:
    print(ex)


# ValueError: Age cannot be zero or less
