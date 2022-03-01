import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


USED = -1

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        start = 0
        while start < len(hand):
            i = start + 1
            prev = hand[start]
            hand[start] = USED
            for _ in range(groupSize - 1):
                while i < len(hand) and (hand[i] in [prev, USED]):
                    i += 1
                if i >= len(hand) or hand[i] - prev > 1:
                    return False
                prev = hand[i]
                hand[i] = USED
                i += 1
            while start < len(hand) and hand[start] == USED:
                start += 1
        return True



if __name__ == '__main__':
    sol = Solution()
    print(sol.isNStraightHand([2,1,4,7,3,2,5], 2) == False)
    print(sol.isNStraightHand([2,1,4,7,3,2,5,6], 2) == True)
    print(sol.isNStraightHand([2,1], 2) == True)
    print(sol.isNStraightHand([2,1], 1) == True)
    print(sol.isNStraightHand([3,1], 2) == False)
