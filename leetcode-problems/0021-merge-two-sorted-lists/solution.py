class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # <-- 1)
        if not l2: return l1  #
        ptr = ans = ListNode(None)  # <-- 2)
        while l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1  # <-- 3)
            ptr.next, l1 = l1, l1.next  # <-- 4)
            ptr = ptr.next  #
        ptr.next = l1 if l1 else l2  # <-- 5)
        return ans.next  # <-- 6)
