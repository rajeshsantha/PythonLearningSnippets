letters = ["a", "b", "c", "d"]

items = (0, "a")
index, letter = items  # This is unpacking the collection


# enumerate object will give a tuple2 (index, value).
for index, letter in enumerate(letters):
    print(index, letter)
