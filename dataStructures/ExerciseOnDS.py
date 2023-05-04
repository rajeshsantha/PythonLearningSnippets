# get Most repeated character in this below text
sentence = "This is a common interview question"


# APPROACH : BY USING DICTIONARY
char_frequency = {}
for i in sentence:
    if i in char_frequency:
        # update the count
        char_frequency[i] += 1
        # YOU CAN ALSO DO THIS BY
        # char_frequency[i] = char_frequency[i] + 1
        # char_frequency.update({i: char_frequency[i]+1}) // same thing.
    else:
        # insert the entry with value 1 , as it is first time occuring
        char_frequency[i] = 1

# print(char_frequency)
# print("************")

newSortedList = sorted(list(char_frequency.items()),
                       key=lambda x: x[1], reverse=True)
# print(newSortedList)
print(f"****The most repeated character is : {newSortedList[0]} ")

if newSortedList:
    mostRepeatedCharacter = newSortedList[0][0]
else:
    print("input sentence is empty")


print(f"The most repeated character is : {mostRepeatedCharacter} ")
# The most repeated character is : i
