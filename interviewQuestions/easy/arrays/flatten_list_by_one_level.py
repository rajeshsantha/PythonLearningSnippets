"""
Problem: Flatten list by one level

Description:
Solve the interview problem: flatten list by one level. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [[1, 2], [3, 4]]
Output: [1, 2, 3, 4]

Pattern: Arrays
Difficulty: Easy
"""


class Solution:
    def flatten_once(self, data, *args):
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
    print(sol.flatten_once([[1, 2], [3, 4]]))
