'''
Group anagram
https://leetcode.com/problems/group-anagrams/
'''
from typing import List
def group_anagrams(strs:List[str]) -> List[List[str]]:
    from collections import defaultdict
    import bisect
    resp = defaultdict(list)
    for s in strs:
        bisect.insort(resp[''.join(sorted(s))], s)

    return sorted(list(resp.values()), key=len)

class TestGroupAnagrams:
    def test_one(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        assert group_anagrams(strs) ==  [['bat'],['nat','tan'],['ate','eat','tea']]

    def test_two(self):
        strs = [""]
        assert group_anagrams(strs) == [['']]
    
    def test_three(self):
        strs = ["a"]
        assert  group_anagrams(strs) == [['a']]
