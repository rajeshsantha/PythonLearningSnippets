from typing import List


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Solution : its a two pointer - inplace shifting problem

class RemoveDuplicatesfromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:

        # below two are edge cases , for safe side
        if not nums:
            return len(nums)
        if len(nums) == 1:
            return 1

        # use duplicate index value to point where to replace the value
        # use index as a general for loop counter for scanning across the list
        # START both of them at 1st index as 0th index will not required to change in any of the test cases.

        duplicateIndexPointer = 1
        for index in range(1, len(nums)):
            # checking if the values adjacent are having same value/also checking if we are seeing the right side value for the first time̵̵
            if nums[index] != nums[index - 1]:
                # if so we have to swap the right side value with left
                nums[duplicateIndexPointer] = nums[index]
                # and move the duplicatePointer to next̵̵
                duplicateIndexPointer += 1
                # right side pointer will any way move forward as its part of the for loop
                # so the duplicateIndexPointer is indirectly also the number of unique items.
        return duplicateIndexPointer


a = [1, 2, 3, 4]
b = [1, 1, 1, 1]
c = [1, 2, 2, 3, 4, 4]
d = [1, 1, 2, 2, 3, 3]

print(RemoveDuplicatesfromSortedArray().removeDuplicates([1, 1, 2]))
print(RemoveDuplicatesfromSortedArray().removeDuplicates(a))
print(RemoveDuplicatesfromSortedArray().removeDuplicates(b))
print(RemoveDuplicatesfromSortedArray().removeDuplicates(c))
print(RemoveDuplicatesfromSortedArray().removeDuplicates(d))
