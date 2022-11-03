class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        eles = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        for word in words:
            temp = ''
            for cha in word:
                temp += eles[ord(cha) - ord('a')]
            if temp not in res:
                res.add(temp)
        return len(res)
