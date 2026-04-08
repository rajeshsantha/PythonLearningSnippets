"""
Problem: Extract digits from string

Description:
Solve the interview problem: extract digits from string. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: 'ab12c3'
Output: '123'

Pattern: Strings
Difficulty: Medium
"""


class Solution:
    def extract_digits(self, data, *args):
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
    print(sol.extract_digits('ab12c3'))
