# Math, Greedy
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # 反向思考
        ans = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            ans += 1
        return ans + startValue - target
