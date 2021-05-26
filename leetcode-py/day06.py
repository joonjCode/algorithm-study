'''
Longest Palindrome Substring
https://leetcode.com/problems/longest-palindromic-substring/
'''

def longest_palindrome(s:str)-> str:
    if len(s) < 2:
        return s
    i,l=0,0
    for j in range(len(s)):
        if s[j-l: j+1] == s[j-l: j+1][::-1]:
            i, l = j-l, l+1
        elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
            i, l = j-l-1, l+2
    return s[i: i+l]


class TestLongestPalindrome:
    def test_one(self):
        s = 'babad'
        assert longest_palindrome(s) == 'bab'
    def test_two(self):
        s = 'cbbd'
        assert longest_palindrome(s) == 'bb'
    def test_three(self):
        s = 'ac'
        assert longest_palindrome(s) == 'a'