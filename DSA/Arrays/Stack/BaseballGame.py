# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/description/

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
#
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
#
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

# Example 1:
#
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
# Example 2:
#
# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
from typing import List


class BaseballGame:

    def multiplyGivenList(self, l: List[int]) -> int:
        product = 1
        for i in l:
            product *= i
        return product

    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            # isnumeric() will not detect -ve numbers. so add one extra check for them
            if i.isnumeric() or i.startswith("-"):
                result.append(int(i))
            else:
                if i == '+':
                    # add the last two scores
                    sumOfLastTwoScores = sum(result[-2:])
                    result.append(sumOfLastTwoScores)
                if i == 'C' and result:
                    # delete last score
                    result.pop()
                if i == 'D':
                    # double the last score
                    previousScore = result[-1]
                    result.append(previousScore * 2)
        return sum(result)


# print(BaseballGame().calPoints(["5", "2", "C", "D", "+"]))
print(BaseballGame().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
