from typing import List


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def find_powers_of_2(leng: int) -> List[str]:
            res = []
            curr_power = 1
            while len(str(curr_power)) <= leng:
                if len(str(curr_power)) == leng:
                    res.append(sorted(str(curr_power)))
                curr_power *= 2
            return res
        length = len(str(n))
        targets = find_powers_of_2(length)
        print(targets)
        n_str = sorted(str(n))
        return any(all(t_char == n_char for t_char, n_char in zip(target, n_str)) for target in targets)



if __name__ == '__main__':
    s = Solution()
    print(s.reorderedPowerOf2(312))
    print(s.reorderedPowerOf2(125))
    print(s.reorderedPowerOf2(1))
    print(s.reorderedPowerOf2(4))
    print(s.reorderedPowerOf2(1))
    print(s.reorderedPowerOf2(1))