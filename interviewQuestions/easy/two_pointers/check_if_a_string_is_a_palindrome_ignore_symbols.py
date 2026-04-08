"""
Problem: Check if a string is a palindrome (ignore symbols)

Description:
Solve the interview problem: check if a string is a palindrome (ignore symbols). Implement the core logic in a clean,
readable, and testable way.

Example:
Input: 'A man, a plan, a canal: Panama'
Output: True

Pattern: Two Pointers
Difficulty: Easy
"""


class Solution:
    def is_palindrome(self, data:str) -> bool:
        left = 0
        right = len(data)-1
    
        while left < right:
            if not data[left].isalnum() and not data[right].isalnum:
                if data[left].lower()!=data[right].lower():
                    return False
            left+=1
            right-=1
        return True

    def is_palindrome_clean(self, data:str) -> bool:
        left = 0
        cleaned_data = ''.join([i.lower() for i in data if i.isalnum()])
        right=len(cleaned_data)-1

        while left < right:
            if cleaned_data[left]!=cleaned_data[right]:
                return False
            left+=1
            right-=1
        return True
        

        

if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.is_palindrome('A man, a plan, a canal: Panama'))
    print(sol.is_palindrome('amanaplanacanalpanama'))

    print(sol.is_palindrome_clean('A man, a plan, a canal: Panama'))
    print(sol.is_palindrome_clean('amanaplanacanalpanama'))
