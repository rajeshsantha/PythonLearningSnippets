"""
Problem: Merge two sorted lists without built-ins

Description:
Solve the interview problem: merge two sorted lists without built-ins. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ([1, 3, 5], [2, 4, 6])
Output: [1, 2, 3, 4, 5, 6]

Pattern: Two Pointers
Difficulty: Easy
"""


class Solution:
    def merge_sorted_lists(self, data, *args):
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
    print(sol.merge_sorted_lists([1, 3, 5], [2, 4, 6]))
