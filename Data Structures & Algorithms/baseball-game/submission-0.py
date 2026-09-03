class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            curr = operations[i]
            if curr == '+':
                stack.append(stack[-1] + stack[-2])
            elif curr == 'D':
                stack.append(stack[-1]*2)
            elif curr == 'C':
                stack.pop()
            else:
                stack.append(int(curr))

        return sum(stack)