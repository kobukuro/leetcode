# Math, Simulation
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 -= num2
            elif num1 < num2:
                num2 -= num1
            else:
                num1 -= num2
            res += 1
        return res
