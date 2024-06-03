# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false


class ValidParentheses:
    def isValid(self, s: str) -> int:
        stack = []

        # Traversing the Expression
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:

                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False
        return len(stack) == 0

    def isValid_improvised(self, s: str) -> int:
        stack = []
        openToClosedBrackets = {")": "(", "]": "[", "}": "{"}
        isValid = False
        for i in s:
            print(i)
            if i in "{[(":
                stack.append(i)
            else:
                if not stack:
                    return False

                if stack[-1] == openToClosedBrackets[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


print(ValidParentheses().isValid("(){}}{"))
print(ValidParentheses().isValid_improvised("(]"))
print(ValidParentheses().isValid_improvised("({{{{}}}))"))
