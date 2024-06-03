from typing import List


# 1929. Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/description/
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# Example 1:
#
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

# Easiest problem on all of leetcode.
class ConcatenationOfArray:
    def getConcatenation1(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans

    def getConcatenation3(self, nums: List[int]) -> List[int]:
        ans = nums * 2
        return ans


print(ConcatenationOfArray().getConcatenation1([1, 2, 1]))
print(ConcatenationOfArray().getConcatenation2([1, 2, 1]))
print(ConcatenationOfArray().getConcatenation3([1, 2, 1]))
