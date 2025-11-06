# Tags: Array, Design
from typing import List


class Bank:

    def __init__(self, balance: List[int] = None):
        self.accounts = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.accounts) or account2 > len(self.accounts):
            return False
        if self.accounts[account1 - 1] < money:
            return False
        self.accounts[account1 - 1] -= money
        self.accounts[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.accounts):
            return False
        self.accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.accounts):
            return False
        if self.accounts[account - 1] < money:
            return False
        self.accounts[account - 1] -= money
        return True
