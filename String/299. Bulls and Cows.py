# String, Hash Table, Counting
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        s = defaultdict(int)
        g = defaultdict(int)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
            else:
                s[secret[i]] += 1
                g[guess[i]] += 1
        for key in s.keys():
            if key in g:
                cow += min(s[key], g[key])
        return f'{bull}A{cow}B'


if __name__ == '__main__':
    secret = '1807'
    guess = '7810'
    print(Solution().getHint(secret=secret, guess=guess))
