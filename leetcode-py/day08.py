'''
two-sum
https://leetcode.com/problems/two-sum/
'''
from typing import List

def two_sum(nums: List[int], target:int)-> List[int]:
    resp = {}
    for k,v in enumerate(nums):
        if target - v in resp:
            return [resp[target-v], k]
        resp[v] = k

class TestTwoSum:
    def test_one(self):
        nums = [2,7,11,15]
        target = 9
        assert two_sum(nums, target) == [0,1]

    def test_two(self):
        nums = [3,2,4]
        target = 6
        assert two_sum(nums, target) == [1,2]
    
    def test_three(self):
        nums= [3,3]
        target = 6
        assert two_sum(nums, target) == [0,1]