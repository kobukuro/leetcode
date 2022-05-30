# String, Sorting
class Solution:
    def sortSentence(self, s: str) -> str:
        hash_map = {}
        sentences = s.split(' ')
        for sentence in sentences:
            hash_map[int(sentence[-1])] = sentence[:-1]
        output = ''
        i = 1
        print(hash_map)
        while i in hash_map:
            output += hash_map[i] + ' '
            i += 1
        print(output)
        return output[:-1]
