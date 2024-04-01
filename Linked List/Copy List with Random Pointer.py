"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        dummy.next = head
        dummy.random = None
        curr = dummy
        old_new = dict()
        while curr:
            new_node = Node(curr.val)
            old_new[curr] = new_node
            curr = curr.next
        
        curr = dummy
        while curr:
            new_node = old_new[curr]
            if curr.next:
                new_node.next = old_new[curr.next]
            else:
                new_node.next = None
            if curr.random:
                new_node.random = old_new[curr.random]
            else:
                new_node.random = None
            curr = curr.next

        return old_new[dummy].next
