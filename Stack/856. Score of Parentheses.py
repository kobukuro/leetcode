# String, Stack
# reference:https://www.youtube.com/watch?v=Pv35fyoKtUA

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        stack = []
        for ele in s:
            val = 0
            if ele == '(':
                stack.append(0)
            else:
                while stack[-1] != 0:
                    val += stack.pop()
                val = max(2 * val, 1)
                stack.pop()
                stack.append(val)
        while stack:
            count += stack.pop()
        return count


if __name__ == '__main__':
    pass
