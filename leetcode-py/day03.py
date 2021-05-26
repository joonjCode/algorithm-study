'''
Find N Unique integers sum up to zero

https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

Constraints
- 1 <= n <= 1000
'''
from typing import List

def sum_zero(n:int) -> List[int]:
    return list(range(1-n,n, 2))


class TestSumZero:
    def test_one(self):
        assert sum_zero(5) == [-4,-2,0,2,4]
    def test_two(self):
        assert sum_zero(3) == [-2,0,2]
    def test_three(self):
        assert sum_zero(1) == [0]