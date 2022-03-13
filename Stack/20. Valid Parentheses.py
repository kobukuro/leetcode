# String, Stack
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack1 = []
        for sub in s:
            stack1.append(sub)
        stack2 = []
        while stack1:
            curr = stack1.pop()
            if curr not in mapping.keys():
                stack2.append(curr)
            else:
                if not stack2:
                    return False
                else:
                    temp = stack2.pop()
                    if mapping[curr] != temp:
                        return False
        if stack2:
            return False
        return True
