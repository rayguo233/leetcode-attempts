# https://leetcode-cn.com/problems/interval-list-intersections/

# You are given two lists of closed intervals, firstList and
# secondList, where firstList[i] = [starti, endi] and
# secondList[j] = [startj, endj]. Each list of intervals
# is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# A closed interval [a, b] (with a < b) denotes the set of
# real numbers x with a <= x <= b.
#
# The intersection of two closed intervals is a set of real
# numbers that are either empty or represented as a closed
# interval. For example, the intersection of [1, 3] and [2, 4]
# is [2, 3].
#
# 0 <= firstList.length, secondList.length
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/interval-list-intersections
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def intervalIntersection(self, firstList: list[list[int]],
                             secondList: list[list[int]]) -> list[list[int]]:

        def findOverlap(l: list[list[int]]) -> list[int]:
            l.sort(key=lambda x: x[0])

            # -----
            #       ---
            if l[0][1] < l[1][0]: return []

            # ------
            #  ---
            if l[0][1] >= l[1][1]: return l[1]

            # ----
            #   ----
            return [l[1][0], l[0][1]]

        res = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            itv1, itv2 = firstList[ptr1], secondList[ptr2]
            overlap = findOverlap([itv1, itv2])
            if len(overlap) != 0: res.append(overlap)

            if itv1[1] < itv2[1]: ptr1 += 1
            else: ptr2 += 1

        return res



if __name__ == '__main__':
    sol = Solution()
    # print(sol.merge([[1,2]]))
    print(sol.intervalIntersection([[1,2],[3,5],[6,7]], [[2,3]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
