/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        int count = 1;
        while (curr != null && curr.next != null) {
            count++;
            curr = curr.next;
        }
        int nodeToRemove = count - n;
        
        if (nodeToRemove == 0) return head.next;
        ListNode next = getNode(nodeToRemove + 1, head);
        ListNode prev = getNode(nodeToRemove - 1, head);
        prev.next = next;
        return head;
    }
    
    public ListNode getNode(int index, ListNode head) {
        ListNode curr = head;
        for (int i = 0; i < index && curr != null; i++) {
            curr = curr.next;
        }
        return curr;
    }
}
