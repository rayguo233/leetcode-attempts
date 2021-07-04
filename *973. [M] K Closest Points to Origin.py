# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        l, r = 0, len(points) - 1
        while l <= r:
            mid = (l + r) // 2
            mid = self.helper(points, mid, l, r)
            if mid == k - 1: return points[:k]
            if mid < k - 1: l = mid + 1
            if mid > k - 1: r = mid - 1
        raise AssertionError

    def helper(self, points, pivot, l, r) -> int:
        self.swap(points, pivot, r)
        pivot, r = r, r - 1
        while l <= r:
            if self.lessOrEqual(points, l, pivot): l += 1
            elif self.lessOrEqual(points, r, pivot):
                self.swap(points, l, r)
                l, r = l + 1, r - 1
            else: r -= 1
        self.swap(points, l, pivot)
        return l

    def lessOrEqual(self, points, l, r):
        return (points[l][0]**2 + points[l][1]**2) <= (points[r][0]**2 + points[r][1]**2)

    def swap(self, points, l, r):
        points[l], points[r] = points[r], points[l]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.merge([[1,2]]))
    print(sol.helper([1,2,3,8,2,3,4,5,6], 3, 0, 8))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
