from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        two_fruit_types = set()
        two_fruit_freq = 0
        one_fruit_type = -1
        one_fruit_freq = 0
        res = 0
        fruits.append(10 ** 7)
        for f in fruits:
            if f == 10 ** 7 or (f not in two_fruit_types and len(two_fruit_types) == 2):
                res = max(res, two_fruit_freq)
                two_fruit_types = {f, one_fruit_type}
                two_fruit_freq = one_fruit_freq + 1
                one_fruit_type = f
                one_fruit_freq = 1
            else:
                two_fruit_types.add(f)
                two_fruit_freq += 1
                if f != one_fruit_type:
                    one_fruit_type = f
                    one_fruit_freq = 1
                else:
                    one_fruit_freq += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.totalFruit([1,2,1,2,3]), 4)
    print(sol.totalFruit([3,2,1,2,3]), 3)
    print(sol.totalFruit([3,2,1,3,4,2,3]), 2)
    print(sol.totalFruit([3]), 1)