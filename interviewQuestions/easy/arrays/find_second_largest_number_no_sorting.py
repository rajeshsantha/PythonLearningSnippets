"""
Problem: Find second largest number (no sorting)

Description:
Solve the interview problem: find second largest number (no sorting). Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [10, 5, 20, 8]
Output: 10

Pattern: Arrays
Difficulty: Easy
"""


class Solution:
    def second_largest(self, data: list[int]) -> int:
        second_max = float("-inf")
        largest = float("-inf")
        n = len(data)
        for i in range(n):
            largest = max(largest, data[i])

        for i in range(0, n):
            if largest > data[i] > second_max:
                second_max = data[i]
        return second_max

    @staticmethod
    def find_second_largest_number(data: list[int]) -> int:
        n = len(data)
        first_max = float("-inf")
        second_max = float("-inf")
        for i in range(n):
            if data[i]> first_max:
                second_max = first_max
                first_max = data[i]
            elif data[i]>second_max and data[i]!=first_max:
                second_max = data[i]

        return second_max


if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.second_largest([11, 51, 20, 8]))
    print(Solution.find_second_largest_number([34, 51,51, 576]))
