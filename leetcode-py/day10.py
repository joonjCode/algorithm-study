'''
Missing Number
https://leetcode.com/problems/missing-number/

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''

from typing import List

def missing_number(nums: List[int]) -> int:

    # 1st solution
    #length = len(nums)
    #return sum(range(length+1)) - sum(nums)

    # 2nd solution
    length = len(nums)
    expected_sum = (length * (length+1)) // 2
    return expected_sum - sum(nums)

class TestMissingNumber:
    def test_one(self):
        nums = [3,0,1]
        assert missing_number(nums) == 2
    def test_two(self):
        nums = [0,1]
        assert missing_number(nums) == 2
    def test_three(self):
        nums = [9,6,4,2,3,5,7,0,1]
        assert missing_number(nums) == 8