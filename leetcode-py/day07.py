'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List

def max_profit(prices:List[int]) -> int:
    res, sell = 0,prices.pop(0)

    for price in prices:
        sell = min(sell, price)
        res = max(res, price-sell)

    return res


class TestMaxProfit:
    def test_one(self):
        prices = [7,1,5,3,6,4]
        assert max_profit(prices) == 5
    def test_two(self):
        prices = [7,6,4,3,1]
        assert max_profit(prices) == 0
    def test_three(self):
        prices = [2,4,1]
        assert max_profit(prices) == 2