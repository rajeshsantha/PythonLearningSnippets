"""
Problem: Compute running average

Description:
Solve the interview problem: compute running average. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [10, 20, 30]
Output: [10.0, 15.0, 20.0]

Pattern: Arrays
Difficulty: Medium
"""


class Solution:
    def running_average(self, data, *args):
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
    print(sol.running_average([10, 20, 30]))
