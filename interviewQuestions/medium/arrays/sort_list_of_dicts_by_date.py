"""
Problem: Sort list of dicts by date

Description:
Solve the interview problem: sort list of dicts by date. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [{'date': '2024-01-02'}, {'date': '2023-12-31'}]
Output: [{'date': '2023-12-31'}, {'date': '2024-01-02'}]

Pattern: Arrays
Difficulty: Medium
"""


class Solution:
    def sort_by_date(self, data, *args):
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
    print(sol.sort_by_date([{'date': '2024-01-02'}, {'date': '2023-12-31'}]))
