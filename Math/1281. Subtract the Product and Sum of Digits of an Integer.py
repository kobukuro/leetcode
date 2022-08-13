# Math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        product_res = 1
        sum_res = 0
        for cha in n:
            product_res *= int(cha)
            sum_res += int(cha)
        return product_res - sum_res
