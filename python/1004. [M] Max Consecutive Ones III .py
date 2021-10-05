class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        num_zeros = 0
        left_i = 0
        nums_size = len(nums)
        res = 0
        for right_i in range(nums_size):
            num_zeros += nums[right_i] == 0
            while num_zeros > k:
                num_zeros -= nums[left_i] == 0
                left_i += 1
            res = max(res, right_i - left_i + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestOnes([0,0,0,0], 6))
