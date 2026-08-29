# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = head
        sp = head

        # fp moves twice and sp moves one 
        while fp and fp.next:  # while first pointer (with next) is not null
            fp = fp.next.next 
            sp = sp.next

            if (fp == sp):
                return True

        return False

