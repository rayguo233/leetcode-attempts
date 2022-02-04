import bisect
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [1]  # type: List[int]
        preorder = preorder.split(',')
        for node in preorder:
            # print(stack, node)
            if not stack: return False
            if stack:
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
            if node != '#':
                stack.append(2)
        return not stack



if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSerialization("0,#,92,#,#"))
    print(sol.isValidSerialization("9,3,4,#,#,1,#,#,#,2,#,6,#,#"), False)
    print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"), True)
    print(sol.isValidSerialization("9,#"))
    print(sol.isValidSerialization("#"), True)
