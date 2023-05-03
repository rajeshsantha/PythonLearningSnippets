pullstop = "."
space = " "
input = 5
for number in range(1, 11):
    print(f"{input} * {number}{(3-len(str(number)))*space}= {(2-len(str(input * number)))*space}{input * number}")

#        f"attempt number {number+1}{(3-len(str(number+1)))*space}{(number+1)*pullstop}")
# 5 * 1 = 5
