# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a
# single digit. Add the two numbers and return the sum
# as a linked list.
#
# You may assume the two numbers do not contain any
# leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        overflow = 0
        while l1 is not None or l2 is not None or overflow != 0:
            curr_val = overflow
            if l1 is not None:
                curr_val += l1.val
                l1 = l1.next
            if l2 is not None:
                curr_val += l2.val
                l2 = l2.next

            overflow = 0
            if curr_val > 9:
                overflow = 1
                curr_val = curr_val - 10

            curr.next = ListNode(val=curr_val)
            curr = curr.next

        return dummy.next




if __name__ == '__main__':
    sol = Solution()
    # print(sol.merge([[1,2]]))
    print(sol.merge_try2([[1,2],[0,9],[6,7]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
