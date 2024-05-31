from typing import List


# https://leetcode.com/problems/shuffle-the-array/
# 1470. Shuffle the Array

# #Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# Example 1:
#
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# Example 2:
#
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# Example 3:
#
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]

# Solution : We just need to print

# list => [2, 5, 1, 3, 4, 7] => [2,3,5,4,1,7]
# index=> [0, 1, 2, 3, 4, 5] => [0,3,1,4,2,5]
# so the required index order is [0,3,1,4,2,5] .
# Either derive a formula with two for loops(shuffle2) or append based on index (as shuffle1)
# Easiest is shuffle3

class ShuffleTheArray:
    def shuffle1(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(nums[i // 2])
            else:
                result.append(nums[n + i // 2])
        return result

    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        return [nums[i + (j % 2) * n] for i in range(n) for j in range(2)]

    def understandTheFormula(self, n: int):
        for i in range(n):
            for j in range(2):
                print(f" when i = {i} and j= {j} then {i} + ({j} % 2) * {n} => {i + (j % 2) * n}")

    def shuffle3(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3
print(ShuffleTheArray().understandTheFormula(n))
print(ShuffleTheArray().shuffle3(nums, n))
