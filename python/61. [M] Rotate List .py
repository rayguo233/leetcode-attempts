# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k: int):
        if k == 0 or head is None:
            return head
        fast_ptr = head
        list_len = 0
        while k and fast_ptr:
            fast_ptr = fast_ptr.next
            k -= 1
            list_len += 1
        if fast_ptr is None:
            return self.rotateRight(head, k % list_len)

        slow_ptr = head
        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        fast_ptr.next = head
        new_head = slow_ptr.next
        slow_ptr.next = None
        return new_head
