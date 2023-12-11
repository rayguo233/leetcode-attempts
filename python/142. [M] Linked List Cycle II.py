import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        steps = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            steps += 1
            if slow is fast:
                return
        return None

if __name__ == '__main__':
    sol = Solution()
    print(sol.racecar(1), 1)
    print(sol.racecar(2), 4)
    print(sol.racecar(3), 2)
    print(sol.racecar(6))
