from typing import List
import collections


class Solution:
    def comp(self, x: List) -> List:
        total_digit_x = sum([x[i] for i in range(1, 18, 2)])
        return [total_digit_x] + x

    def largestNumber(self, cost: List[int], target: int) -> str:
        cost_to_i = collections.defaultdict(int)
        for i, c in enumerate(cost):
            cost_to_i[c] = max(cost_to_i[c], i)
        print(cost_to_i)
        init_list = []
        for num in '987654321':
            init_list += [num, 0]
        dp = [init_list.copy() for _ in range(target+1)]
        print(dp)
        for c, i in cost_to_i.items():
            if c <= target:
                dp[c][2*(8-i) + 1] += 1
        for sub_target in range(target+1):
            for c, i in cost_to_i.items():
                if sub_target - c <= 0:
                    continue
                if not any([dp[sub_target-c][i] for i in range(1, 18, 2)]):
                    continue
                candidate = dp[sub_target-c].copy()
                candidate[2*(8-i) + 1] += 1
                dp[sub_target] = max(dp[sub_target], candidate, key=self.comp)
        if False:
            for i, l in enumerate(dp):
                print(i, l)
        res = ''
        for i in range(9):
            if dp[target][2*i + 1]:
                res += dp[target][2*i] * dp[target][2*i + 1]
        if not res:
            res = '0'
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.largestNumber([1,2,3,4,5,6,7,8,9], 11))
    # print(sol.largestNumber([4,3,2,5,6,7,2,5,5],9))
    print(sol.largestNumber([2,4,6,2,4,6,4,4,4],5))
    # assert(sol.rob([2,1,4]) == 6)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 10)
    # assert(sol.rob([2,1,4,8,9]) == 15)
