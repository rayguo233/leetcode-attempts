# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it
# can trap after raining.

# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5


class Solution:

    def trap_0(self, height: list[int]) -> int:
        if not height: return 0
        res = 0
        lefts = [(height[0], 0)]
        for i, h in enumerate(height[1:], start=1):
            # print(i, h, res, lefts)
            base = None
            while lefts:
                left_h, left_i = lefts[-1]
                # print(left_h, left_i, base, res)
                if base is None and h > left_h:
                    base = left_h
                    lefts.pop(-1)
                    continue
                elif base is None and h == left_h:
                    lefts[-1] = (h, i)
                    break
                elif base is None and h < left_h: lefts.append((h, i))
                elif base is not None and h >= left_h:
                    # print('adding', (left_h - base) * (i - left_i - 1))
                    res += (left_h - base) * (i - left_i - 1)
                    base = left_h
                    lefts.pop(-1)
                    continue
                else:
                    res += (h - base) * (i - left_i - 1)
                    lefts.append((h, i))
                break
            if not lefts: lefts.append((h, i))
        return res

    def trap(self, height: list[int]) -> int:
        LEFT, RIGHT = 0, 1
        maxes = [-1, -1]
        indices = [0, len(height) - 1]
        res = 0
        print('-----start-----')
        while indices[LEFT] <= indices[RIGHT]:
            curr = maxes[LEFT] > maxes[RIGHT]
            if height[indices[curr]] < maxes[curr]:
                res += maxes[curr] - height[indices[curr]]
            maxes[curr] = max((height[indices[curr]], maxes[curr]))
            indices[curr] += (-1 if curr else 1)
            # print(indices, curr)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([]))
    print(sol.trap([1,0,1]), 1)
    print(sol.trap([0,1,0,0]), 0)
    print(sol.trap([0,1,6,4,5,8,9,0]), 3)

    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
