'''
Best time to buy and sell stock
link : https://leetcode.com/problmes/best-time-to-buy-and-sell-stock

Things to study
- Kadane's Algorithm
- Descriptive Statistics
- For max, min size of a variable use : float('inf'),  math.inf, sys.maxsize


'''

from typing import List
import math

def max_profit(prices: List[int])-> int:
    profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price- min_price)
    
    return profit


class TestMaxProfit:
    def test_one(self):
        prices = [7,1,5,3,6,4]
        
        assert max_profit(prices) == 5