# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# prices = [7,1,5,3,6,4]
# correct output : 5
# Explanation :
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


def get_max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
# prices = [7,6,4,3,1]
print(get_max_profit(prices))