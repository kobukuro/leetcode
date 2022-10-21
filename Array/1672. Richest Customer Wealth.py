# Array, Matrix
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for account in accounts:
            total_balance = 0
            for bank_balance in account:
                total_balance += bank_balance
            res = max(res, total_balance)
        return res
