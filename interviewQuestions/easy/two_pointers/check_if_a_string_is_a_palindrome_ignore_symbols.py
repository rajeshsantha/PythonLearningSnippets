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
    def is_palindrome(self, data, *args):
        """
        Approach:
        - Identify the primary data structure and iterate efficiently.
        - Handle edge cases first (empty input, single item, invalid shape).
        - Return output in the exact format expected by the interviewer.

        Time Complexity:
        - O(n) to O(n log n), depending on the chosen implementation.

        Space Complexity:
        - O(n) auxiliary space in the general case.
        """
        pass


if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.is_palindrome('A man, a plan, a canal: Panama'))
