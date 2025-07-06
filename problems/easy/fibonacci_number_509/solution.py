# Tags: Memoization, Dynamic Programming
class Solution:
    # Time complexity: O(N). Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1) access later on.
    # Space complexity: O(N). The size of the stack in memory is proportional to N. Also, the memoization hash table is used, which occupies O(N) space.
    def fib_memoization(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {}
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.fib_memoization(n - 1, memo) + self.fib_memoization(n - 2, memo)
        return memo[n]

    # Time complexity: O(N). Each value from 2 to N is computed once. Thus, the time it takes to find the answer is directly proportional to N where N is the Fibonacci Number we are looking to compute.
    # Space complexity: O(1). This requires 1 unit of space for the integer N and 3 units of space to store the computed values (current, prev1, and prev2) for every loop iteration. The amount of space used is independent of N, so this approach uses a constant amount of space.
    def fib_dp(self, n: int) -> int:
        if n <= 1:
            return n

        current = 0
        prev1 = 1
        prev2 = 0

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
