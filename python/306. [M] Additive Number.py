from math import floor, ceil


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, ceil(n/2)):
            for j in range(i+1, n):
                if (len(num[:i]) > 1 and num[:i][0] == '0') or (len(num[i:j]) > 1 and num[i:j][0] == '0'):
                    continue
                first_num = int(num[:i]) + int(num[i:j])
                if self.is_additive_seq(num[i:j], str(first_num), num[j:]):
                    return True
        return False

    def is_additive_seq(self, prev:str, target: str, num: str) -> bool:
        if target == num:
            return True
        len_target = len(target)
        if len(num) < len_target or target != num[:len_target]:
            return False
        return self.is_additive_seq(target, str(int(prev) + int(target)), num[len_target:])


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAdditiveNumber('123'))
    print(sol.isAdditiveNumber('336'))
    print(sol.isAdditiveNumber('336915'))
    print(sol.isAdditiveNumber('33639'))
