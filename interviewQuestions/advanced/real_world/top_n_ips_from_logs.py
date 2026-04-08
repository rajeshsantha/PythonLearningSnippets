"""
Problem: Top N IPs from logs

Description:
Solve the interview problem: top n ips from logs. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ('access.log', 3)
Output: [('10.0.0.1', 120), ('10.0.0.2', 98), ('10.0.0.3', 76)]

Pattern: Real-World
Difficulty: Advanced
"""


class Solution:
    def top_ips(self, data, *args):
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
    print(sol.top_ips('access.log', 3))
