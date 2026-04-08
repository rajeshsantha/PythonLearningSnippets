"""
Problem: Find second largest number (no sorting)

Description:
Solve the interview problem: find second largest number (no sorting). Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [10, 5, 20, 8]
Output: 10

Pattern: Arrays
Difficulty: Easy
"""


class Solution:
    def second_largest(self, data, *args):
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
    print(sol.second_largest([10, 5, 20, 8]))
