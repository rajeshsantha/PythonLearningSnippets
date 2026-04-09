"""
Problem: Compare two JSON files

Description:
Solve the interview problem: compare two json files. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ('a.json', 'b.json')
Output: {'added': [], 'removed': [], 'changed': []}

Pattern: Real-World
Difficulty: Advanced
"""


class Solution:
    def compare_json(self, data, *args):
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
    print(sol.compare_json('a.json', 'b.json'))
