# Array, Stack, Simulation
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        ans = 0
        for op in ops:
            if op == '+':
                temp1 = int(stack.pop())  # 9
                temp2 = int(stack.pop())  # -4
                stack.append(temp2)
                stack.append(temp1)
                new = temp1 + temp2
                stack.append(new)
                ans += new
            elif op == 'D':
                temp = int(stack.pop())
                stack.append(temp)
                stack.append(temp * 2)
                ans += temp * 2
            elif op == 'C':
                ans -= int(stack.pop())
            else:
                stack.append(int(op))
                ans += int(op)
            print(op, stack, ans)
        return ans
