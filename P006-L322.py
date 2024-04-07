# https://leetcode.com/problems/coin-change/
# Runtime: 1251 ms -> beats 10.38% of users with Python3
#     - next time, use bottom-up approach for DP to be faster

class Solution:
    MAX_INT = 9223372036854775807   # sys.maxint

    # Incorrect approach

    # # Runtime: O(n*m)
    # def dp(self, coinIdx, amount) -> int:
    #     if amount == 0: return 0
    #     if coinIdx == len(self.sortedCoins): return self.MAX_INT
    #     if (coinIdx, amount) in self.memo: return self.memo[(coinIdx, amount)]
    #     coin = self.sortedCoins[coinIdx]
    #     numCoins = amount // coin
    #     ifUseCoin = self.MAX_INT
    #     if numCoins > 0:
    #         ifUseCoin = numCoins + self.dp(coinIdx + 1, amount - numCoins * coin)
    #     ifNoUseCoin = self.dp(coinIdx + 1, amount)
    #     self.memo[(coinIdx, amount)] = min(ifUseCoin, ifNoUseCoin)
    #     return self.memo[(coinIdx, amount)]

    # def coinChange(self, coins: list[int], amount: int) -> int:
    #     if amount == 0: return 0
    #     coins.sort(reverse=True)
    #     self.sortedCoins = coins
    #     self.memo = {}
    #     retval = self.dp(0, amount) if self.dp(0, amount) != self.MAX_INT else -1
    #     print(self.memo)
    #     return retval
    # # end coinChange

    # Runtime: O(n*m)
    def dp(self, amount: int) -> int:
        if amount == 0: return 0
        if amount in self.memo: return self.memo[amount]
        self.memo[amount] = self.MAX_INT
        for coin in self.coins:
            if coin <= amount:
                useCoin = self.dp(amount - coin)
                if useCoin != self.MAX_INT:
                    self.memo[amount] = min(self.memo[amount], 1 + useCoin)
        return self.memo[amount]
    # end dp

    def coinChange(self, coins: list[int], amount: int) -> int:
        self.coins = coins
        self.memo = {}
        retval = self.dp(amount)
        return retval if retval != self.MAX_INT else -1
    # end coinChange
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    print(sol.coinChange([186,419,83,408], 6249))   # 20
