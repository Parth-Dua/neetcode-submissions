class Solution:
    def open_of(self, i):
        if i == '}':
            return '{'
        if i == ']':
            return '['
        if i == ')':
            return '('

    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0 or stack.pop() != self.open_of(i):
                    return False

        return len(stack) == 0