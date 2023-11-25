class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        integer = int(num)
        while integer % 10 == 0:
            integer //= 10
        return str(integer)
