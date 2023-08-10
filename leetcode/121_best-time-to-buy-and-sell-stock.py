# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diff = 0
        minimum_price_to_buy = prices[0]
        for i in range(1, n):
            if prices[i] < minimum_price_to_buy:
                minimum_price_to_buy = prices[i]

            if prices[i] - minimum_price_to_buy > diff:
                diff = prices[i] - minimum_price_to_buy

        return diff
