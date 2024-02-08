# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq 
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        val_lists = []
        for l in lists:
            if not l:
                continue
            val_lists.append([l.val, l])
        
        heapq.heapify(val_lists)

        res_head = res = ListNode(-1)
        while val_lists:
            smallest_val_pt = heapq.heappop(val_lists)
            smallest_val = smallest_val_pt[0]
            smallest_pt = smallest_val_pt[1]

            if smallest_pt:
                if smallest_pt.next:
                    smallest_next = smallest_pt.next
                    heapq.heappush(val_lists, [smallest_next.val, smallest_next])

                res.next = ListNode(smallest_val)
                res = res.next
        
        return res_head.next
            
            

        
