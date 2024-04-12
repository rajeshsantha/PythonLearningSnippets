FULLSTOP = "."
SPACE = " "
INPUT = 5
for number in range(1, 11):
    print(f"{INPUT} * {number}{(3 - len(str(number))) * SPACE}= {(2 - len(str(INPUT * number))) * SPACE}{INPUT * number}")

#        f"attempt number {number+1}{(3-len(str(number+1)))*space}{(number+1)*pullstop}")
# 5 * 1 = 5
