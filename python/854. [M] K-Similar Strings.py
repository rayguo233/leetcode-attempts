from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        N = len(s1)
        next_set = {s1}
        red_1_set, red_2_set = set(), set()
        steps = 1
        while next_set:
            for s in next_set:
                for i in range(N):
                    for j in range(i, N):
                        if s[i] == s2[i] and s[j] == s2[j]:
                            continue
                        swapped_s = ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))
                        if swapped_s == s2:
                            return steps
                        if s[i] == s2[i] or s[j] == s2[j]:
                            if s[j] == s2[i] and s[i] == s2[j]:
                                red_1_set.add(swapped_s)
                        elif s[j] == s2[i] and s[i] == s2[j]:
                            red_2_set.add(swapped_s)
                        elif s[j] == s2[i] or s[i] == s2[j]:
                            red_1_set.add(swapped_s)
            next_set = red_2_set or red_1_set
            red_1_set, red_2_set = set(), set()
            steps += 1
        return -1






if __name__ == '__main__':
    sol = Solution()
    print(sol.kSimilarity('ab', 'ba'))
    print(sol.kSimilarity('abc', 'bca'))
