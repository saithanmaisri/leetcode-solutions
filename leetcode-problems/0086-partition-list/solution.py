# Definition for singly-linked list. 
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 
class Solution(object):
    def partition(self, head, x):
        if head is None or x is None: 
            return head
        dummy1 = ListNode(0) 
        dummy2 = ListNode(0)
        less = dummy1 
        greater = dummy2 
        temp = head
        while temp:
            if temp.val < x:
                less.next = temp 
                less = less.next
            else:
                greater.next = temp 
                greater = greater.next
            temp = temp.next 
        greater.next = None 
        less.next = dummy2.next
        return dummy1.next
