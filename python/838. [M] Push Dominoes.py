from typing import List

RIGHT, LEFT = 0, 1
FAKE_INT_MAX = 10 ** 6 + 1

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # iterate for rightward force
        forces = []  # type: List[List[int, int]]
        right_force_by = FAKE_INT_MAX  # type: int
        for i, dmn in enumerate(dominoes):
            if dmn == 'R':
                right_force_by = i
            elif dmn == 'L':
                right_force_by = FAKE_INT_MAX
            forces.append([right_force_by])
        # iterate for leftward force
        left_force = []
        left_force_by = FAKE_INT_MAX  # type: int
        for i in reversed(range(len(dominoes))):
            dmn = dominoes[i]
            if dmn == 'L':
                left_force_by = i
            elif dmn == 'R':
                left_force_by = FAKE_INT_MAX
            forces[i].append(left_force_by)
        # sum up forces to get result
        res = ''
        for i, f in enumerate(forces):
            right_i, left_i = f
            if left_i == right_i == FAKE_INT_MAX or abs(left_i - i) == abs(right_i - i):
                res += '.'
            elif abs(left_i - i) > abs(right_i - i):
                res += 'R'
            else:
                res += 'L'
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.pushDominoes(''))
    print(sol.pushDominoes('L.R'))
    print(sol.pushDominoes('R.L'))
    print(sol.pushDominoes('RR..LL'))
    print(sol.pushDominoes('RR...LL'))
    print(sol.pushDominoes('RR...L'))
