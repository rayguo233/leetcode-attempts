import collections
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        num_to_freq = collections.defaultdict(int)
        for num in deliciousness:
            num_to_freq[num] += 1
        powers = [2 ** i for i in range(22)]
        res = 0
        for num, freq in num_to_freq.items():
            for power in powers:
                if power <= num:
                    continue
                need = power - num
                if need < num or need not in num_to_freq:
                    continue
                if need == num:
                    if freq == 1:
                        continue
                    res = (res + (freq * (freq - 1) // 2)) % (10 ** 9 + 7)
                    continue
                res = (res + freq * num_to_freq[need]) % (10 ** 9 + 7)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPairs([1048576,1048576]))
