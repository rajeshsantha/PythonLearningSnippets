"""
Problem: Flatten nested JSON

Description:
Solve the interview problem: flatten nested json. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: {'id': 1, 'info': {'city': 'NY'}}
Output: {'id': 1, 'info.city': 'NY'}

Pattern: Recursion
Difficulty: Advanced
"""


class Solution:
    def flatten_json(self, data, *args):
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
    print(sol.flatten_json({'id': 1, 'info': {'city': 'NY'}}))
