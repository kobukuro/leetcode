# Two Pointers, String, Stack, Simulation
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for i in range(len(s)):
            if s[i] != '#':
                s_stack.append(s[i])
            else:
                if s_stack:
                    s_stack.pop()
        t_stack = []
        for i in range(len(t)):
            if t[i] != '#':
                t_stack.append(t[i])
            else:
                if t_stack:
                    t_stack.pop()
        return s_stack == t_stack
