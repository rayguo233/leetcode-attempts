# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked
# list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to
# the length of the linked list. If the number of nodes
# is not a multiple of k then left-out nodes, in the end,
# should remain as it is.
#
# You may not alter the values in the list's nodes,
# only nodes themselves may be changed.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        print('--------------------')
        while head is not None:
            print(head.val)
            head = head.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(next=head)

        # traverse `k` nodes
        pre, cur = dummy, head
        for _ in range(k):
            if cur is None:
                return head
            pre = cur
            cur = cur.next

        left, first = dummy, dummy.next
        last, right = pre, cur

        prev, curr = None, left.next
        for _ in range(k):
            nex = curr.next
            curr.next = prev
            prev, curr = curr, nex

        left.next, first.next = last, self.reverseKGroup(right, k)
        # self.printList(left)


        return dummy.next

    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    #     dummy = ListNode(next=head)
    #     stack = []
    #
    #     while True:





if __name__ == '__main__':
    sol = Solution()
    head = sol.reverseKGroup(ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4)))), 2)
    sol.printList(head)
    # print(sol.minWindow_clean("a", 'aa'))
    # print(sol.minWindow_clean("ASDF", ''))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
    # print(sol.minWindow_clean("ADOBECODEBANC", 'ABC'))
