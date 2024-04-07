# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Runtime: 55 ms -> beats 75.10% of users with Python3

class Solution:
    # # Runtime: O(n*m)
    # def dp(self, boughtIdx, currIdx):
    #     if currIdx == self.pricesLen: return 0
    #     if (boughtIdx, currIdx) in self.memo: return self.memo[(boughtIdx, currIdx)]
    #     self.memo[(boughtIdx, currIdx)] = 0
    #     buySellShare = 0
    #     if boughtIdx is None:
    #         if currIdx + 1 < self.pricesLen and self.prices[currIdx] < self.prices[currIdx + 1]:
    #             # buy
    #             buySellShare = self.dp(currIdx, currIdx + 1)
    #     elif self.prices[currIdx] > self.prices[boughtIdx]:
    #         # sell
    #         buySellShare = self.prices[currIdx] - self.prices[boughtIdx] + self.dp(None, currIdx + 1)
    #     holdShare = self.dp(boughtIdx, currIdx + 1)
    #     self.memo[(boughtIdx, currIdx)] = max(buySellShare, holdShare)
    #     return self.memo[(boughtIdx, currIdx)]
    # # end dp

    # def maxProfit(self, prices: list[int]) -> int:
    #     self.prices = prices
    #     self.pricesLen = len(prices)
    #     self.memo = {}
    #     return self.dp(None, 0)
    # # end maxProfit

    # Improved solution

    # Runtime: O(n)
    def maxProfit(self, prices: list[int]) -> int:
        pricesLen = len(prices)
        profit = 0
        for i in range(1, pricesLen):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
    # end maxProfit
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 7
    assert sol.maxProfit([1,2,3,4,5]) == 4
    assert sol.maxProfit([7,6,4,3,1]) == 0
