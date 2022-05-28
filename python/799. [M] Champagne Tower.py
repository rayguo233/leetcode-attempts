class Solution:

    def champagneTower(self, poured: int, query_row: int,
                       query_glass: int) -> float:
        pyramid = [[0. for _ in range(101)] for _ in range(101)]
        pyramid[0][0] = poured
        for row in range(query_row + 1):
            for col in range(row + 1):
                amt_overflow = pyramid[row][col] - 1
                if amt_overflow <= 0:
                    continue
                pyramid[row + 1][col] += amt_overflow / 2.
                pyramid[row + 1][col + 1] += amt_overflow / 2.
        return min(1., pyramid[query_row][query_glass])


if __name__ == '__main__':
    sol = Solution()
    print(sol.champagneTower(1, 0, 0))
    print(sol.champagneTower(2, 1, 0))
    print(sol.champagneTower(1, 1, 0))
    print(sol.champagneTower(100000009, 33, 17))
