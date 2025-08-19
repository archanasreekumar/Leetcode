# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# prices = [7,1,5,3,6,4]
# correct output : 5
# Explanation :
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
# Approach
# For prices = [7, 1, 5, 3, 6, 4]:
# Initialization: profit = 0, day = 7
# Iteration:
# i = 1: diff = 1 - 7 = -6, profit = max(-6, 0) = 0, day = 1 (since diff <= 0)
# i = 2: diff = 5 - 1 = 4, profit = max(4, 0) = 4
# i = 3: diff = 3 - 1 = 2, profit = max(2, 4) = 4
# i = 4: diff = 6 - 1 = 5, profit = max(5, 4) = 5
# i = 5: diff = 4 - 1 = 3, profit = max(3, 5) = 5
# Result: 5


def get_max_profit(prices):
    n = len(prices)
    max_profit = 0
    # assuming we buy on the first day initially
    buy_day_price = prices[0]

    # Loop through the prices starting from the second day (index 1)
    for i in range(1, n):
        # Calculate the difference (potential profit) between the
        # current day's price and the initial buy price
        profit = prices[i] - buy_day_price
        # Update the maximum profit if the current difference is greater
        # than the previous maximum profit
        max_profit = max(max_profit, profit)
        # If the current day's price is lower than or equal to the initial buy price,
        # update the initial buy price to the current day's price
        # This allows us to consider buying on the current day for future calculations
        if profit <= 0:
            buy_day_price = prices[i]
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(get_max_profit(prices))
