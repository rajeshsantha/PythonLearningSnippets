
# if number divided by 3 => fizz
# if number divided by 5 => buzz
# if number divided by both 3,5 => fizzBuzz

def isDivideByn(number, n):
    return number % n == 0


def fizzBuzz(input):
    result = ""

    if isDivideByn(input, 3) and isDivideByn(input, 5):
        print("fizzBuzz")
    elif isDivideByn(input, 3):
        print("fizz")
    elif isDivideByn(input, 5):
        print("buzz")
    else:
        print("invalid input ", input)


fizzBuzz(10)
