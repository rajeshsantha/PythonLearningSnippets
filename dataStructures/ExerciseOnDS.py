# get Most repeated character in this below text
sentence = "This is a common interview question"

char_frequency = {}
for i in sentence:
    if i in char_frequency:
        # update the count
        char_frequency.update({i: char_frequency[i]+1})
    else:
        # insert the entry with value 1 , as it is first time occuring
        char_frequency[i] = 1

print(char_frequency)

for key, value in char_frequency.items():
    print(key, value)
# T 1
# h 1
# i 5
# s 3
#   5
# a 1
# c 1
# o 3
# m 2
# n 3
# t 2
# e 3
# r 1
# v 1
# w 1
# q 1
# u 1
