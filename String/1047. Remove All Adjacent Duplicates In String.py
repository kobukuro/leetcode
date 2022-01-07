# String
# reference:https://www.youtube.com/watch?v=Ec2SJvjxYEs
# class Solution:
#     def removeDuplicates(self, s):
#         stack = ''
#         for item in s:
#             if not stack:
#                 stack += item
#                 continue
#             if item == stack[-1]:
#                 stack = stack[:-1]
#             else:
#                 stack += item
#         return stack

# better solution
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    s = 'abbaca'
    print(Solution().removeDuplicates(s=s))
