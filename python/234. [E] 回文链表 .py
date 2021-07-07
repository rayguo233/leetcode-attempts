# https://leetcode-cn.com/problems/palindrome-linked-list/

# 请判断一个链表是否为回文链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None: return True
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow if fast is None else slow.next

        prev, curr = None, mid
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev, curr = curr, nex

        left, right = head, prev
        while right is not None:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True





if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('sdffssdfgghjk'))
    print(sol.lengthOfLongestSubstring('sdfsdfs'))
    print(sol.lengthOfLongestSubstring(''))
