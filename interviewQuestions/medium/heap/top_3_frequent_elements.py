"""
Problem: Top 3 frequent elements

Description:
Solve the interview problem: top 3 frequent elements. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ([1, 1, 1, 2, 2, 3], 2)
Output: [1, 2]

Pattern: Heap
Difficulty: Medium
"""


class Solution:
    def top_k_frequent(self, data, *args):
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
    print(sol.top_k_frequent([1, 1, 1, 2, 2, 3], 2))
