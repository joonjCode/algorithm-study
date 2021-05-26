'''
reverse string
https://leetcode.com/problems/reverse-string/

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

'''
from typing import List

def reverse(s: List[str]):
    return s[::-1]


class TestReverse:
    def test_one(self):
        s = ["h","e","l","l","o"]
        assert reverse(s) == ["o","l","l","e","h"]
    def test_two(self):
        s = ["H","a","n","n","a","h"]
        assert reverse(s) == ["h","a","n","n","a","H"]
 