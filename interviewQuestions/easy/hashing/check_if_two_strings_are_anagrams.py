"""
Problem: Check if two strings are anagrams

Description:
Solve the interview problem: check if two strings are anagrams. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ('listen', 'silent')
Output: True

Pattern: Hashing
Difficulty: Easy
"""


class Solution:
    def are_anagrams(self, data, *args):
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
    print(sol.are_anagrams('listen', 'silent'))
