"""
Problem: Count character frequency in a string

Description:
Solve the interview problem: count character frequency in a string. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: 'banana'
Output: {'b': 1, 'a': 3, 'n': 2}

Pattern: Hashing
Difficulty: Easy
"""


class Solution:
    def char_frequency(self, data:str)-> dict[str, int]:
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
        frequency_counter = {}
        for character in data:
            if character in frequency_counter:
                print(f"{character} exists in freq")
                frequency_counter[character] = frequency_counter.get(character)+1
            else:
                print(f"{character} doesnt exist so add")
                frequency_counter[character] = 1
        
        return frequency_counter
        


if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.char_frequency('banana'))
