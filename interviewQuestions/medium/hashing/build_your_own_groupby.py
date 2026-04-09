"""
Problem: Build your own groupBy

Description:
Solve the interview problem: build your own groupby. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ([{'dept': 'eng', 'name': 'A'}, {'dept': 'eng', 'name': 'B'}], 'dept')
Output: {'eng': [{'dept': 'eng', 'name': 'A'}, {'dept': 'eng', 'name': 'B'}]}

Pattern: Hashing
Difficulty: Medium
"""


class Solution:
    def group_by_key(self, data, *args):
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
    print(sol.group_by_key([{'dept': 'eng', 'name': 'A'}, {'dept': 'eng', 'name': 'B'}], 'dept'))
