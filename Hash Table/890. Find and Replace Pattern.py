from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            mapping = {}
            is_valid = True
            for i in range(len(word)):
                if word[i] not in mapping:
                    for key, value in mapping.items():
                        if value == pattern[i]:
                            is_valid = False
                            break
                    if is_valid:
                        mapping[word[i]] = pattern[i]
                    else:
                        break
                else:
                    if mapping[word[i]] != pattern[i]:
                        is_valid = False
                        break
            if is_valid:
                res.append(word)
        return res
