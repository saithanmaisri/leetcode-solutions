import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        operations = ['+', '-', '*', '/']
        ops = {
            '+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul,
            '/': operator.truediv,
        }
        stack = [] 
        for i, n in enumerate(tokens):
            if n in operations:
                newVal = ops[n](int(stack[-2]), int(stack[-1])) 
                stack.pop()
                stack.pop()
                stack.append(newVal) 
            else:
                stack.append(n)
        return int(stack[0])
