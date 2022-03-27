class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_n = str(n)
        l = 0
        res= ''
        while l < len(str_n):
            r = l + 1
            while r < len(str_n) and str_n[r] == str_n[l]:
                r += 1
            if r < len(str_n) and str_n[r] < str_n[l]:
                res += str(int(str_n[l]) - 1) + '9' * (len(str_n) - 1 - l)
                return str(int(res))
            res += str_n[l:r]
            l = r
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.monotoneIncreasingDigits(121))
    print(sol.monotoneIncreasingDigits(122))
    print(sol.monotoneIncreasingDigits(101))
    print(sol.monotoneIncreasingDigits(1))
    print(sol.monotoneIncreasingDigits(10))
    print(sol.monotoneIncreasingDigits(123))