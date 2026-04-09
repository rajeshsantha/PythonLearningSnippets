"""
Problem: Convert list of dicts to dict of lists

Description:
Solve the interview problem: convert list of dicts to dict of lists. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]
Output: {'id': [1, 2], 'name': ['A', 'B']}

Pattern: Hashing
Difficulty: Medium
"""


class Solution:
    def listdict_to_dictlist(self, data, *args):
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
    print(sol.listdict_to_dictlist([{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]))
