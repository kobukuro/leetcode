# String, Stack
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        need_to_delete_indice = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((i, s[i]))
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    need_to_delete_indice.append(i)
        if stack:
            for ele in stack:
                need_to_delete_indice.append(ele[0])
        s = list(s)
        for index in sorted(need_to_delete_indice, reverse=True):
            del s[index]
        return ''.join(s)
