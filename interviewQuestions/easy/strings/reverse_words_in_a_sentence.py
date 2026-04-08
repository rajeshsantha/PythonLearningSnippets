"""
Problem: Reverse words in a sentence

Description:
Solve the interview problem: reverse words in a sentence. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: 'I love Python'
Output: 'Python love I'

Pattern: Strings
Difficulty: Easy
"""


class Solution:
    def reverse_words(self, data, *args):
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
    print(sol.reverse_words('I love Python'))
