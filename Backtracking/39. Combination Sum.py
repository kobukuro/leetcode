# Array, Backtracking
from typing import List


# Let N be the number of candidates, T be the target value,
# and M be the minimal value among the candidates.
# Time Complexity: O(N^(T/M + 1))
# The execution of the backtracking is unfolded as a DFS traversal in a n-ary tree.
# The total number of steps during the backtracking would be the number of nodes in the tree.
# At each node, it takes a constant time to process,
# except the leaf nodes which could take a linear time to make a copy of combination.
# So we can say that the time complexity is linear to the number of nodes of the execution tree.
# Here we provide a loose upper bound on the number of nodes.
#  ■ First of all, the fan-out of each node would be bounded to N, i.e. the total number of candidates.
#  ■ The maximal depth of the tree, would be T/M ,
#  where we keep on adding the smallest element to the combination.
#  ■ As we know, the maximal number of nodes in N-ary tree of T/M height would be N^(T/M + 1)
# Note that, the actual number of nodes in the execution tree
# would be much smaller than the upper bound,
# since the fan-out of the nodes are decreasing level by level.

# Space Complexity: O(T/M)
# We implement the algorithm in recursion,
# which consumes some additional memory in the function call stack.
# The number of recursive calls can pile up to T/M,
# where we keep on adding the smallest element to the combination.
# As a result, the space overhead of the recursion is O(T/M)
# In addition, we keep a combination of numbers during the execution,
# which requires at most O(T/M) space as well.
# To sum up, the total space complexity of the algorithm would be O(T/M).
# Note that, we did not take into the account the space used to hold the final results
# for the space complexity.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            print(candidates[start], comb)
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()
            # print(comb)

        backtrack(target, [], 0)

        return results


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))
