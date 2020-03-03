# given array of numbers representing the stock prices of a company in chronological order
# given an int k representing the number of buys and sells you get
# req : buy a stock -> sell that stock before buying a new one
# req: can't sell until you buy
# ex input [5, 2, 4, 0, 1] and k = 2 buy at 5 sell at 2 buy at 0 sell at 1 -> 2 transactions with 3 profit total
# return 3

# let dp[i][j] represented maximum profit we can get using i transactions up to day j
# so dp[0 transactions left] [j days] = 0 because we can't profit with no transactions
# also dp[i transactions] [0 days left] = 0 because with no time left we have no way of profiting

# on the last day we either sold a stock or didn't own a stock so it's the max of selling a stock on last day vs
# the cost of selling the stock on the day before. The day before is between selling a stock on that day or the day
# before that. With this logic we can use dynamic programming to find an O(m * n) solution
from math import inf

def max_profit(prices, k):
    n = len(prices)
    dp = [[0 for _ in range(n)] for _ in range(k + 1)]

    print(dp)

    # no time left
    for i in range(k + 1):
        dp[i][0] = 0
    # no transactions left
    for j in range(n):
        dp[0][j] = 0

    for i in range(1, k + 1):
        for j in range(1, n):
            best_so_far = -inf
            for m in range(j):
                best_so_far = max(best_so_far, prices[j] - prices[m] + dp[i - 1][m])
            dp[i][j] = max(best_so_far, dp[i][j - 1])

    return dp[k][n-1]




test = [5, 2, 4, 0, 1]
test_k = 2
print(max_profit(test, test_k))
