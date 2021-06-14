# https://leetcode-cn.com/problems/merge-intervals/

# Given an array of intervals where
# intervals[i] = [starti, endi], merge all overlapping
# intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.
#
# 1 <= intervals.length
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        res = []

        for itv in intervals[1:]:
            if itv[0] <= prev[1]:
                prev[1] = max(prev[1], itv[1])
            else:
                res.append(prev)
                prev = itv
        if len(res) == 0 or prev[1] != res[-1][1]:
            res.append(prev)
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.merge([[1,2]]))
    print(sol.merge([[1,2],[0,9],[6,7]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
