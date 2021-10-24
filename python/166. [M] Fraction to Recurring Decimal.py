

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if (numerator < 0) + (denominator < 0) == 1:
            res = '-'
        else:
            res = ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        remainder = numerator % denominator
        after_decimal_str = ''
        remainder_to_index = {}
        remainder_index = 0
        while remainder != 0:
            remainder *= 10
            if remainder in remainder_to_index:
                after_decimal_str = \
                    after_decimal_str[:remainder_to_index[remainder]] +\
                    '(' +\
                    after_decimal_str[remainder_to_index[remainder]:] +\
                    ')'
                break
            else:
                remainder_to_index[remainder] = remainder_index
                after_decimal_str += str(remainder // denominator)
                remainder = remainder % denominator
            remainder_index += 1
        if after_decimal_str:
            res += '.' + after_decimal_str
        return res




if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(-50, 8))
    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
