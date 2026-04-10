"""
Problem: Merge two sorted lists without built-ins

Description:
Solve the interview problem: merge two sorted lists without built-ins. Implement the core logic in a clean,
readable, and testable way.

Example:
Input: ([1, 3, 5], [2, 4, 6])
Output: [1, 2, 3, 4, 5, 6]

Pattern: Two Pointers
Difficulty: Easy
"""


from typing import Tuple


class Solution:
    def merge_sorted_lists(self, list1:list[int], list2:list[int]) -> list[int]:
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
        
        merged_list = []
        if not list1 and not list2:
            return merged_list
        if not list1:
            return list2
        if not list2:
            return list1
        i,j=0,0
        while i<len(list1) and j<len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i+=1
            else:
                merged_list.append(list2[j])
                j+=1


        while i<len(list1):
            merged_list.append(list1[i])
            i+=1


        while j<len(list2):
            merged_list.append(list2[j])
            j+=1


        return merged_list
        




if __name__ == "__main__":
    sol = Solution()
    # Example run
    print(sol.merge_sorted_lists([1, 3, 5], [2, 4, 6]))
    # Edge case: empty lists
    print(sol.merge_sorted_lists([], []))
    
    # Edge case: one empty list
    print(sol.merge_sorted_lists([], [1, 2, 3]))
    print(sol.merge_sorted_lists([1, 2, 3], []))
    
    # Edge case: single elements
    print(sol.merge_sorted_lists([1], [2]))
    print(sol.merge_sorted_lists([2], [1]))
    
    # Edge case: duplicates
    print(sol.merge_sorted_lists([1, 1, 1], [1, 1, 1]))
    
    # Edge case: all elements in one list are smaller
    print(sol.merge_sorted_lists([1, 2, 3], [4, 5, 6]))
    
    # Edge case: all elements in one list are larger
    print(sol.merge_sorted_lists([4, 5, 6], [1, 2, 3]))
    
    # Edge case: negative numbers
    print(sol.merge_sorted_lists([-3, -1, 2], [-2, 0, 1]))

        # Edge case: all elements in one list are smaller
    print(sol.merge_sorted_lists([1, 2, 3], [4]))
