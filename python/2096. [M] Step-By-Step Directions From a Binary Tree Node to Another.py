from enum import Enum, auto
from typing import Optional, Tuple, Union


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ReturnFound(Enum):
    FOUND_S = 0
    FOUND_D = 1
    FOUND_NONE = auto()
    FOUND_BOTH = auto()


class Solution:

    def getDirections(self, root: Optional[TreeNode], startValue: int,
                      destValue: int) -> str:

        def find_vals(node: Optional[TreeNode]) -> Tuple[ReturnFound, str]:
            if node is None:
                return ReturnFound.FOUND_NONE, ''
            paths = [None, None]
            if node.val == startValue:
                paths[ReturnFound.FOUND_S.value] = ''
            elif node.val == destValue:
                paths[ReturnFound.FOUND_D.value] = ''

            right_res, right_str = find_vals(node.right)
            if right_res == ReturnFound.FOUND_BOTH:
                return right_str
            left_res, left_str = find_vals(node.left)
            if left_res == ReturnFound.FOUND_BOTH:
                return left_str

            for is_left, (res1, str1) in enumerate([(right_res, right_str),
                                                    (left_res, left_str)]):
                if res1 == ReturnFound.FOUND_S:
                    paths[ReturnFound.FOUND_S.value] = str1 + 'U'
                elif res1 == ReturnFound.FOUND_D:
                    paths[ReturnFound.FOUND_D.value] = ('L' if is_left else
                                                        'R') + str1

            if all(path is not None for path in paths):
                return ReturnFound.FOUND_BOTH, paths[0] + paths[1]
            if paths[ReturnFound.FOUND_S.value] is not None:
                return ReturnFound.FOUND_S, paths[ReturnFound.FOUND_S.value]
            if paths[ReturnFound.FOUND_D.value] is not None:
                return ReturnFound.FOUND_D, paths[ReturnFound.FOUND_D.value]
            else:
                return ReturnFound.FOUND_NONE, ''

        return find_vals(root)[1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.champagneTower(1, 0, 0))
    print(sol.champagneTower(2, 1, 0))
    print(sol.champagneTower(1, 1, 0))
    print(sol.champagneTower(100000009, 33, 17))
