"""
Problem: Unique elements in order of appearance

Description:
Solve the interview problem: unique elements in order of appearance. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [4, 5, 4, 6, 5]
Output: [4, 5, 6]

Pattern: Hashing
Difficulty: Easy
"""


class Solution:
    def unique_ordered(self, data:list[int])-> list[int]:
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
        


if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.unique_ordered([4, 5, 4, 6, 5]))
    
