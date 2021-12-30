class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            insert_before = lambda digit_n, digit_x:  digit_x < digit_n
        else:
            insert_before = lambda digit_n, digit_x:  digit_x > digit_n
        for i, digit in enumerate(n):
            if digit == '-':
                continue
            digit = int(digit)
            if insert_before(digit, x):
                return n[0:i] + str(x) + n[i:]
        return n + str(x)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxValue('987654', 5))
    print(sol.maxValue('-987654', 5))
    print(sol.maxValue('98765432194', 5))
    print(sol.maxValue('98765594', 5))  # => '9876559[5]4'
    print(sol.maxValue('987654', 5))
    # assert(sol.rob([0]) == 0)
    # assert(sol.rob([2,1,4]) == 6)
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 10)
    # assert(sol.rob([2,1,4,8,9]) == 15)
