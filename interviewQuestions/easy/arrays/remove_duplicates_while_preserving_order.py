"""
Problem: Remove duplicates while preserving order

Description:
Solve the interview problem: remove duplicates while preserving order. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [1, 2, 2, 3, 1]
Output: [1, 2, 3]

Pattern: Arrays
Difficulty: Easy
"""


class Solution:
    def remove_duplicates_ordered(self, data, *args):
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
    print(sol.remove_duplicates_ordered([1, 2, 2, 3, 1]))
