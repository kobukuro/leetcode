# Array, Greedy
# reference: https://www.youtube.com/watch?v=lJwbPZGo05A
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]
    print(Solution().canCompleteCircuit(gas=gas, cost=cost))
