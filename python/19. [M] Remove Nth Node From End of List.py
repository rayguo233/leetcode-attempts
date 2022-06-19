# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
    print(sol.findMedianSortedArrays([1, 2, 3], [4]))
    print(sol.findMedianSortedArrays([1, 2, 3], [0]))
    print(sol.findMedianSortedArrays([1, 2], []))
    print(sol.findMedianSortedArrays([1], []))
    print(sol.findMedianSortedArrays([], [1]))
