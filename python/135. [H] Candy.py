class Solution:
    def candy(self, ratings: list[int]) -> int:
        size = len(ratings)
        res = [1] * size
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(size-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)
        return sum(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([1,2,3,2,5,2,4]))
