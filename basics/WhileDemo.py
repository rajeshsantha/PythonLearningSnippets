# number = 100
# while number > 0:
#     number //= 2
#     print(number)

# Normal while loop
command = ""
while command.lower().strip() != "quit":
    command = input(">")
    print("ECHO", command)
# Infinite loops

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower().strip() == "quit":
        break
