# Hash Table, Math, Two Pointers
# reference:https://www.youtube.com/watch?v=ljz85bxOYJ0
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sum_of_square(n)
            if n == 1:
                return True
        return False

    def sum_of_square(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit * digit
            output += digit
            n = n // 10
        return output


if __name__ == '__main__':
    n = 19
    print(Solution().isHappy(n=n))
