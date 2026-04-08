"""
Problem: Detect loop in linked list

Description:
Solve the interview problem: detect loop in linked list. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: '1->2->3->2'
Output: True

Pattern: Linked List
Difficulty: Advanced
"""


class Solution:
    def detect_cycle(self, data, *args):
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
    print(sol.detect_cycle('1->2->3->2'))
