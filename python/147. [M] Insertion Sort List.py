# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:

    def insertionSortList(self,
                          head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(next=head)
        dummy = ListNode(val=-9999)
        while head.next:
            node = head.next
            head.next = node.next
            ptr = dummy
            while ptr.next and ptr.next.val < node.val:
                ptr = ptr.next
            node.next = ptr.next
            ptr.next = node
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    a = [2, 0]
    a = [0]
    a = [1, 2]
    a = [1, 0, 2]
    sol.sortColors(a)
    print(a)
    # print(sol.sortColors("a", 'aa'))
    # print(sol.minWindow_clean("ASDF", ''))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
