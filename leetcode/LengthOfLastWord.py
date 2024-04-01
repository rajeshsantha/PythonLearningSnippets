class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splittedwords =s.strip().split(" ")
        print("last word is = ",splittedwords[-1])
        return len(splittedwords[-1])


#print(Solution().lengthOfLastWord("hello sdfjhds fhjkdl  "))
print(Solution().lengthOfLastWord(input("enter the input string \n")))

#lstr = ['hello', '', ' ', 'world', ' ']
#>>> list(filter(lambda string: string,lstr)) #removed empty strings
#['hello', ' ', 'world', ' ']
# list(filter(lambda string: string.strip(),lstr))
#['hello', 'world'] #removed whitespaces

