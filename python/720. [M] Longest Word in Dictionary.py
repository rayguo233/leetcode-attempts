import bisect
import functools
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:

    def compare(self, w1: str, w2: str) -> int:
        if len(w1) == len(w2):
            if w1 < w2: return -1
            if w1 == w2: return 0
            return 1
        if len(w1) < len(w2):
            return -1
        return 1

    def longestWord(self, words: List[str]) -> str:
        words.sort(key=functools.cmp_to_key(self.compare))
        prev_set = {''}
        curr_set = set()
        curr_str_len = 1
        res = ''
        for w in words:
            len_w = len(w)
            if len_w > curr_str_len:
                if len_w > curr_str_len + 1:
                    break
                curr_str_len = len_w
                prev_set = curr_set
                curr_set = set()

            if w[:-1] not in prev_set:
                continue
            curr_set.add(w)
            if len(res) < len_w:
                res = w

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestWord(['ab', 'b', 'a', 'd', 'ba']))
    print(sol.longestWord(['a']))
    print(sol.longestWord(['a', 'abbc', 'abb', 'ab', 'abc', 'c']))
    print(
        sol.longestWord(["a", "banana", "app", "appl", "ap", "apply",
                         "apple"]))
