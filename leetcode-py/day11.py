'''
238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self

Could you solve it in O(n) time complexity and without using division?
Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

from typing import List

def product_except_self(nums:List[int])-> List[int]:
    s = len(nums)
    resp = [0] * s
    prev = 1
    for i in range(s):
        resp[i], prev = prev, prev*nums[i]
        
    prev = 1
    for i in range(s-1, -1, -1):
        resp[i], prev = resp[i] * prev, prev*nums[i]

    return resp

class TestProductExceptSelf:
    def test_one(self):
        nums = [1,2,3,4]
        assert product_except_self(nums) == [24,12,8,6]
    def test_one(self):
        nums = [-1,1,0,-3,3]
        assert product_except_self(nums) == [0,0,9,0,0]