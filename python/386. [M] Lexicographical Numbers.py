from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        str_n = str(n)
        def helper(prefix: str) -> List[str]:
            len_pre = len(prefix)
            if int(prefix) > n:
                return []
            if len_pre == len(str_n):
                return ['']
            sub_res = ['']
            for c in '0123456789':
                sub_res += [c + suf for suf in helper(prefix + c)]
            return sub_res
        res = []
        for c in '123456789':
            res += [c + ans for ans in helper(c)]
        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    s = Solution()
    print(s.lexicalOrder(4))
    print(s.lexicalOrder(12))
    print(s.lexicalOrder(20))
    print(s.lexicalOrder(29))
    print(s.lexicalOrder(126))