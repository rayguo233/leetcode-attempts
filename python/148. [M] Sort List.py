from typing import List, Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        smaller, larger = ListNode(), ListNode()
        ptr_sm, ptr_lg = smaller, larger
        pivot = head
        ptr = head.next
        head.next = None
        while ptr:
            if ptr.val <= pivot.val:
                ptr_sm.next = ptr
                ptr_sm = ptr
            else:
                ptr_lg.next = ptr
                ptr_lg = ptr
            next_ptr = ptr.next
            ptr.next = None
            ptr = next_ptr
        smaller = self.sortList(smaller.next)
        larger = self.sortList(larger.next)
        pivot.next = larger
        if smaller is None:
            return pivot
        self.get_last_node(smaller).next = pivot
        return smaller

    def get_last_node(self, ptr):
        while ptr.next:
            ptr = ptr.next
        return ptr


if __name__ == '__main__':
    sol = Solution()
    node = sol.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
