# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(val=head.val)
        slow, fast = head, head.next
        # find the mid point
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next is not None:
            fast = fast.next
        mid = slow.next
        slow.next = None
        return TreeNode(val=mid.val,
                        left=self.sortedListToBST(head),
                        right=self.sortedListToBST(mid.next))


if __name__ == '__main__':
    sol = Solution()
    print(sol.triangleNumber([0, 0, 0]))
    print(sol.triangleNumber([2, 1]))
    print(sol.triangleNumber([2, 2, 3, 4]))
    print(sol.triangleNumber([4, 2, 3, 4]))
