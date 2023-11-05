class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        broken = set()
        for c in brokenLetters:
            broken.add(c)
        res = 0
        for word in words:
            can_fully_type = True
            for c in word:
                if c in broken:
                    can_fully_type = False
                    break
            if can_fully_type:
                res += 1
        return res
