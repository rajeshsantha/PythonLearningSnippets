class GCDOfStrings:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        elif (str1 + str2) == (str2 + str1):
            if len(str1) > len(str2):
                print(f" str1 = {str1} and str2 = {str2}")
                return self.gcdOfStrings(str1[len(str2):], str2)
            else:
                print(f" str1 = {str1} and str2 = {str2}")
                return self.gcdOfStrings(str1, str2[len(str1):])
        else:
            return ""


str1 = "ABCABC"
str2 = "ABC"
print(GCDOfStrings().gcdOfStrings(str1, str2))
str1 = "ABABAB"
str2 = "ABAB"
print(GCDOfStrings().gcdOfStrings(str1, str2))