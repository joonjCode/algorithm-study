'''
valid palindrome
link : https://leetcode.com/problems/valid-palindrome/

'''

def valid_palindrome(text: str)-> bool:
    resp = ''.join([t.lower() for t in text if t.isalnum()])

    return resp == resp[::-1] 


class TestPalindrome:
    """
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome. 
    """
    def test_one(self):
        assert valid_palindrome('race a car') == False

    def test_two(self):
        assert valid_palindrome('A man, a plan, a canal: Panama') == True




