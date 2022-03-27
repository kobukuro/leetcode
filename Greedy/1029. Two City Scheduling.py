# Array, Greedy, Sorting
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costs.sort()
        # print(costs)
        # print([max(cost)-min(cost) for cost in costs])
        # 184+259+54+577+118+667

        left_num = 0
        right_num = 0
        left_diff = []
        right_diff = []
        ans = 0
        for i in range(len(costs)):
            if costs[i][0] < costs[i][1]:
                print(i, 'left')
                left_num += 1
                ans += costs[i][0]
                left_diff.append((i, costs[i][1] - costs[i][0]))
            else:
                print(i, 'right')
                right_num += 1
                ans += costs[i][1]
                right_diff.append((i, costs[i][0] - costs[i][1]))

            if left_num > len(costs) / 2:
                print(left_diff)
                print(min(left_diff, key=lambda x: x[1]))
                index = min(left_diff, key=lambda x: x[1])[0]
                ans -= costs[index][0]
                ans += costs[index][1]
                remove_diff_index = -1
                for i in range(len(left_diff)):
                    if left_diff[i][0] == index:
                        remove_diff_index = i
                left_diff.pop(remove_diff_index)
                left_num -= 1
            elif right_num > len(costs) / 2:
                print(right_diff)
                print(min(right_diff, key=lambda x: x[1])[0])
                index = min(right_diff, key=lambda x: x[1])[0]
                ans -= costs[index][1]
                ans += costs[index][0]
                remove_diff_index = -1
                for i in range(len(right_diff)):
                    if right_diff[i][0] == index:
                        remove_diff_index = i
                right_diff.pop(remove_diff_index)
                right_num -= 1
        return ans
