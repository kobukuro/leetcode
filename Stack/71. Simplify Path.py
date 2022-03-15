# String, Stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [ele for ele in path.split('/') if ele != '']
        print(stack)
        delete_index = []
        for i in range(len(stack)):
            if stack[i] == '.':
                delete_index.append(i)
            elif stack[i] == '..':
                prev_index = i - 1
                if 0 <= prev_index < len(stack):
                    while prev_index in delete_index:
                        prev_index -= 1
                    if 0 <= prev_index < len(stack):
                        delete_index.append(prev_index)
                delete_index.append(i)
        print(sorted(delete_index))
        for index in sorted(delete_index, reverse=True):
            del stack[index]
        print(stack)
        ans = '/'
        for ele in stack:
            ans += f'{ele}/'
        return ans[:-1] if len(ans) > 1 else ans
