# Time complexity : O(N) both for encode and decode,
# where N is a number of strings in the input array.
# Space complexity : O(1) for encode to keep the output,
# since the output is one string.
# O(N) for decode keep the output, since the output is an array of strings.
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + length + 1])
            i = j + length + 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
