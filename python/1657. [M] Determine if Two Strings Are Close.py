import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counts = [[0] * 26 for _ in range(2)]
        for i, w in enumerate((word1, word2)):
            for c in w:
                counts[i][ord(c) - ord('a')] += 1
        if any((a and not b) or (b and not a) for a, b in zip(counts[0], counts[1])):
            return False
        counts[0].sort()
        counts[1].sort()
        return all(a == b for a, b in zip(counts[0], counts[1]))


if __name__ == '__main__':
    sol = Solution()
    print(sol.closeStrings('aaaa', 'dddd'), False)
    print(sol.closeStrings('aaba', 'baaa'), True)
