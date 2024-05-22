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


word1 = "abc"
word2 = "qwertyu"
sol = MergeStringAlternately()
print(sol.mergeAlternately(word1, word2))
