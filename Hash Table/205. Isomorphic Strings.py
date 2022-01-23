# Hash Map, String
# TODO need to be improved
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0
        hash_map = {}
        if len(s) != len(t):
            return False
        while i < len(s):
            if s[i] not in hash_map and t[i] not in hash_map.values():
                hash_map[s[i]] = t[i]
            elif s[i] in hash_map and t[i] not in hash_map.values():
                return False
            elif s[i] not in hash_map and t[i] in hash_map.values():
                return False
            else:
                if hash_map[s[i]] != t[i]:
                    return False
            i += 1
        return True


if __name__ == '__main__':
    s = "bcb"
    t = "bcc"
    print(Solution().isIsomorphic(s=s, t=t))
