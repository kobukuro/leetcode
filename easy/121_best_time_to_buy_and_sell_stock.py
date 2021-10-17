def maxProfit(prices):
    buy_price = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]
        if prices[i] - buy_price > max_profit:
            max_profit = prices[i] - buy_price
    return max_profit


if __name__ == '__main__':
    input_list = [7, 1, 5, 3, 6, 4]
    # input_list = [7, 6, 4, 3, 1]
    print(maxProfit(input_list))
