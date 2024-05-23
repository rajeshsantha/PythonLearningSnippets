class MergeStringAlternately:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        l1 = len(word1)
        l2 = len(word2)
        commonRange = min(l1, l2)

        leftoverString = ""
        if l1 == l2:
            leftoverString = ""
        elif l1 < l2:
            leftoverString = word2[l1:]
        else:
            leftoverString = word1[l2:]

        for i in range(0, commonRange):
            mergedWord = mergedWord + word1[i] + word2[i]
        return mergedWord + leftoverString

    def mergeAlternately2(self, word1: str, word2: str) -> str:
        mergedString = []

        for a, b in zip(word1, word2):
            mergedString.append(a + b)

        mergedString.append(word1[len(word2):])
        mergedString.append(word2[len(word1):])

        return ''.join(mergedString)





word1 = "abc"
word2 = "qwertyu"
sol = MergeStringAlternately()
print(sol.mergeAlternately2(word1, word2))
