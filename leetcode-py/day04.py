'''
Most common word
https://leetcode.com/problems/most-common-word/

Wanted to avoid regex
regex : [^\w]
'''
from typing import List


def most_common(paragraph:str, banned:List[str]):
	from collections import Counter
	words = [word.translate(str.maketrans("!?',;.", "      ")).strip()for word in paragraph.lower().split()]
	
	for b in banned:
		words.remove(b)
	c = Counter(words)
	
	return c.most_common(1)[0][0]

class TestMostCommon:
	def test_one(self):
		paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
		banned = ['hit']
		assert most_common(paragraph, banned) == 'ball'
	
	def test_two(self):
		paragraph = 'a.'
		banned=[]
		assert most_common(paragraph, banned) == 'a'