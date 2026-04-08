"""
Problem: Sliding window max

Description:
Solve the interview problem: sliding window max. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ([1, 3, -1, -3, 5, 3, 6, 7], 3)
Output: [3, 3, 5, 5, 6, 7]

Pattern: Sliding Window
Difficulty: Advanced
"""


class Solution:
    def sliding_window_max(self, data, *args):
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
    print(sol.sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
