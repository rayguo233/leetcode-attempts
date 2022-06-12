from typing import List


class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        d = {}
        max_seq_end = None
        max_seq_len = 0
        for num in nums:
            seq_len, prev_ans = 1, None
            for num1, (num1_seq_len, _) in d.items():
                if (num % num1) or (num1_seq_len + 1 <= seq_len):
                    continue
                seq_len = num1_seq_len + 1
                prev_ans = num1
            d[num] = (seq_len, prev_ans)
            if seq_len > max_seq_len:
                max_seq_len = seq_len
                max_seq_end = num
        res = []
        while max_seq_end is not None:
            res.append(max_seq_end)
            max_seq_end = d[max_seq_end][1]
        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestDivisibleSubset([1, 2, 3]))
    print(sol.largestDivisibleSubset([1, 2, 4, 8]))
