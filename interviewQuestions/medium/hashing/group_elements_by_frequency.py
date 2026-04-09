"""
Problem: Group elements by frequency

Description:
Solve the interview problem: group elements by frequency. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ['a', 'b', 'a', 'c', 'b', 'a']
Output: {3: ['a'], 2: ['b'], 1: ['c']}

Pattern: Hashing
Difficulty: Medium
"""


class Solution:
    def group_frequency(self, data, *args):
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
    print(sol.group_frequency(['a', 'b', 'a', 'c', 'b', 'a']))
