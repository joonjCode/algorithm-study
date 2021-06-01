'''
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list
'''

class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head:LinkedNode)-> bool:
    from collections import deque
    q = deque()
    if not head:
        return True
    
    node = head
    while node:
        q.append(node.val)
        node = node.next
    while len(q)>1:
        if q.popleft() != q.pop():
            return False
    return True


class TestIsPalindrome:
    def test_one(self):
        node1 = LinkedNode(1, LinkedNode(2))
        assert is_palindrome(node1) == False
    def test_two(self):
        node = LinkedNode(1, LinkedNode(2, LinkedNode(2, LinkedNode(1))))
        assert is_palindrome(node) == True