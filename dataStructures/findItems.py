letters = ["a", "b", "c", "d", "b", "c", "b", "c"]
print(letters.index("b"))  # 1
# print(letters.index("x"))  # ValueError: 'x' is not in list

# To prevent the above error, see if the item is there then get the index of the value
inputValue = "b"
if inputValue in letters:
    print(letters.index(inputValue))  # 1
    numberOfOccurancesInList = letters.count(inputValue)
    print(f"{inputValue} occured {numberOfOccurancesInList} times in the list")
else:
    print(f"\" {inputValue} \" doesn't exist in the list")
