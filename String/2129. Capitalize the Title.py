class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []
        words = title.split(' ')
        for word in words:
            if len(word) == 1 or len(word) == 2:
                res.append(word.lower())
            else:
                temp = ''
                for i in range(len(word)):
                    if i == 0:
                        temp += word[i].upper()
                    else:
                        temp += word[i].lower()
                res.append(temp)
        return ' '.join(res)
