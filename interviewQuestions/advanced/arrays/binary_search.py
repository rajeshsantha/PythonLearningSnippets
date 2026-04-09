"""
Problem: Binary search

Description:
Solve the interview problem: binary search. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ([1, 3, 5, 7], 5)
Output: 2

Pattern: Arrays
Difficulty: Advanced
"""


class Solution:
    def binary_search(self, data, *args):
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




if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.binary_search([1, 3, 5, 7], 5))
