'''
Array Partition1
https://leetcode.com/problems/array-partition-i/
'''
from typing import List

def array_pair_sum(nums:List[int]) -> int:
    return sum(sorted(nums)[::2])
    pass

class TestArrayPairSum:
    def test_one(self):
        nums = [1,4,3,2]
        assert array_pair_sum(nums) == 4
    def test_two(self):
        nums = [6,2,6,5,1,2]
        assert array_pair_sum(nums) == 9
