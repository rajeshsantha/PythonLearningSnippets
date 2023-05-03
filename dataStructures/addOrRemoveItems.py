letters = ["a", "b", "c", "d"]

# add at the end
letters.append("e")
# add at the mentioned index
letters.insert(0, "-")
print(letters)

# remove by index
letters.pop(0)  # can only remove one item
print(letters)
# remove by value
letters.remove("b")
print(letters)
# remove by range of values
del letters[0:3]  # removed 0th to 2nd element (3rd is exclusive) : 0 to 2
print(letters)
