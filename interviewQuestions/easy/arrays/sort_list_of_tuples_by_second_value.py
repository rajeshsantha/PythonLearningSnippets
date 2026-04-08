"""
Problem: Sort list of tuples by second value

Description:
Solve the interview problem: sort list of tuples by second value. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [(1, 5), (2, 3), (3, 4)]
Output: [(2, 3), (3, 4), (1, 5)]

Pattern: Arrays
Difficulty: Easy
"""


class Solution:
    def sort_by_second(self, data, *args):
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
    print(sol.sort_by_second([(1, 5), (2, 3), (3, 4)]))
