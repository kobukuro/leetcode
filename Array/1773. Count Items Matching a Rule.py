# Array, String
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for item in items:
            num = None
            if ruleKey == 'type':
                num = 0
            elif ruleKey == 'color':
                num = 1
            else:
                num = 2
            if item[num] == ruleValue:
                res += 1
        return res
