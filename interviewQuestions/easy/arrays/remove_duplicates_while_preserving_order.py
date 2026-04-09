"""
Problem: Remove duplicates while preserving order

Description:
Solve the interview problem: remove duplicates while preserving order. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: [1, 2, 2, 3, 1]
Output: [1, 2, 3]

Pattern: Arrays
Difficulty: Easy
"""


class Solution:
    def remove_duplicates_ordered(self, data, *args):
        deduplicated_list = []
        for i in data:
            if i not in deduplicated_list:
                deduplicated_list.append(i)

        return deduplicated_list

    @staticmethod
    def remove_duplicates_ordered_optimal(data:list[int])-> list[int]:
        return list(dict.fromkeys(data))

    @staticmethod
    def remove_duplicates_interview(data: list[int])-> list[int]:
        uniquelist= set()
        result = []
        for item in data:
            if item not in uniquelist:
                uniquelist.add(item)
                result.append(item)

        return result

if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.remove_duplicates_ordered([1, 2, 2, 3, 1]))
    print(Solution.remove_duplicates_ordered_optimal([1, 2, 2, 3, 1]))
    print(Solution.remove_duplicates_interview([1, 2, 2, 3, 1]))
