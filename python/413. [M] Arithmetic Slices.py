from typing import List

DEFAULT_DIFF = 3000
LAST_NUM = 9000

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def num_subarr(length: int) -> int:
            # print(f'len: {length}')
            if length < 3:
                return 0
            length -= 2
            if length == 1:
                return 1
            return (1 + length) * length // 2
        nums.append(LAST_NUM)
        prev_diff = DEFAULT_DIFF
        start_i = -1
        res = 0
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i-1]
            if curr_diff == prev_diff:
                continue
            # print(f'i: {i}; start_i: {start_i}')
            res += num_subarr(i - start_i)
            start_i = i - 1
            prev_diff = curr_diff

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1,2,3,4]))
    print(s.numberOfArithmeticSlices([1,2,3,4,5]))
    print(s.numberOfArithmeticSlices([1,2,3,4,6,8,10]))
    print(s.numberOfArithmeticSlices([1,2,3,4,6,8]))