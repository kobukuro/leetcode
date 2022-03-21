# Hash Table, Stack, Design, Ordered Set
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 1
        else:
            self.freq[val] += 1
        f = self.freq[val]
        if f > self.max_freq:
            self.max_freq = f
        if f not in self.group:
            self.group[f] = []
            self.group[f].append(val)
        else:
            self.group[f].append(val)

    def pop(self) -> int:
        # print(self.max_freq)
        # print(self.group[self.max_freq])
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
