letters = ["a", "b", "c", "d"]
print(letters.index("b"))  # 1
# print(letters.index("x"))  # ValueError: 'x' is not in list

# To prevent the above error, see if the item is there then get the index of the value
inputValue = "x"
if inputValue in letters:
    print(letters.index(inputValue))  # 1
else:
    print(f"\" {inputValue} \" doesn't exist in the list")
