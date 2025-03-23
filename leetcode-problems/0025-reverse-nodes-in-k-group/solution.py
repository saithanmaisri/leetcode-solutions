class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        end = head
        count = 0
        while end:
            end = end.next
            count += 1
        if count == 1:
            return head
        end = head
        begin = dumpNode = ListNode(0, head)
        for j in range(count // k):
            for i in range(k - 1):
                next_node = end.next
                end.next = next_node.next  # 1->3
                next_node.next = begin.next  # 2->1
                begin.next = next_node  # begin -> 2
            begin = end  # another round begin->1
            end = end.next  # another round end->3
        return dumpNode.next
