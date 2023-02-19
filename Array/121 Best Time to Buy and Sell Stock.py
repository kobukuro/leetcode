# Array, Dynamic Programming
# Time: O(n) Only a single pass is needed.
# Space:O(1) Only two variables are used.
def maxProfit(prices):
    max_profit = 0
    buy_price = float('inf')
    for i in range(len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]
        elif prices[i] > buy_price:
            curr_profit = prices[i] - buy_price
            max_profit = max(max_profit, curr_profit)
    return max_profit


if __name__ == '__main__':
    input_list = [7, 1, 5, 3, 6, 4]
    # input_list = [7, 6, 4, 3, 1]
    print(maxProfit(input_list))
