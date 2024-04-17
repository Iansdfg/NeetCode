"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        old_new = dict()
        while queue:
            curr = queue.popleft()
            if curr in old_new:
                new_node = old_new[curr]
            else:
                new_node = Node(curr.val)
                old_new[curr] = new_node
                
            for neighbor in curr.neighbors:
                if neighbor in old_new:
                    new_neighbor = old_new[neighbor]
                else:
                    new_neighbor = Node(neighbor.val)
                    old_new[neighbor] = new_neighbor
                    queue.append(neighbor)

                new_node.neighbors.append(new_neighbor)

        return old_new[node]

        
