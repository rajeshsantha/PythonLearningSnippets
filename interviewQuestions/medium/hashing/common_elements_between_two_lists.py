"""
Problem: Common elements between two lists

Description:
Solve the interview problem: common elements between two lists. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ([1, 2, 3], [2, 3, 4])
Output: [2, 3]

Pattern: Hashing
Difficulty: Medium
"""


class Solution:
    def common_elements(self, data, *args):
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
    print(sol.common_elements([1, 2, 3], [2, 3, 4]))
