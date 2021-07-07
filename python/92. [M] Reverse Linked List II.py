# https://leetcode-cn.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two
# integers left and right where left <= right, reverse
# the nodes of the list from position left to position
# right, and return the reversed list.
#
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        def reverseNextN(head_a, next_a, n_a) -> (ListNode, ListNode):
            if n_a == 0:
                return head_a, next_a
            next_next_a = next_a.next
            next_a.next = head_a
            return reverseNextN(next_a, next_next_a, n_a - 1)

        dummy = ListNode(next=head)
        pre = cur = dummy
        i = 0

        # find starting point and store in `curr`
        while i < left:
            pre = cur
            cur = cur.next
            i += 1

        pre.next, nex = reverseNextN(cur, cur.next, right - left)
        # print(pre.next.val)
        # print(cur.val, nex.val)
        cur.next = nex

        return dummy.next

    def reverse_between(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: return head
        dummy = ListNode(next=head)
        curr = dummy
        while left > 1:
            left, right = left - 1, right - 1
            curr = curr.next

        left, first = curr, curr.next
        prev, curr = left.next, left.next.next
        while right > 1:
            right -= 1
            next = curr.next
            prev, curr.next = curr, prev
            curr = next

        left.next, first.next = prev, curr
        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    n = sol.reverse_between(ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5))))),
                             2,4)
    m = 0
    while n is not None and m < 10:
        print(n.val, m)
        n = n.next
        m += 1
    # print(sol.merge([[1,2],[0,9],[6,7]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
