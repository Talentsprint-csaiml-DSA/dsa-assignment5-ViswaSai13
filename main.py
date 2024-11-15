def min_coins(coins, target_amount):
    coins.sort(reverse=True)

    no_max_coin = target_amount // coins[0]
    target_amount = target_amount % coins[0]

    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0

    for amount in range(1, target_amount+1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount],dp[amount-coin]+1)

    dp[target_amount] = dp[target_amount] + no_max_coin

    return dp[target_amount] if dp[target_amount] != float('inf') else -1
