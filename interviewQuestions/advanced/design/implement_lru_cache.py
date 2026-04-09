"""
Problem: Implement LRU cache

Description:
Solve the interview problem: implement lru cache. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: (2, [('put', 1, 1), ('put', 2, 2), ('get', 1)])
Output: [None, None, 1]

Pattern: Design
Difficulty: Advanced
"""


class Solution:
    def lru_cache(self, data, *args):
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
    print(sol.lru_cache(2, [('put', 1, 1), ('put', 2, 2), ('get', 1)]))
