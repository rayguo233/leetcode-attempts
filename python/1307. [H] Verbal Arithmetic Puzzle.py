import collections
from typing import Dict, List, Set, Tuple


class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        res_dict = collections.defaultdict(int)
        for i, c in enumerate(reversed(result)):
            res_dict[c] += 10**i
        word_dict = collections.defaultdict(int)
        for word in words:
            for i, c in enumerate(reversed(word)):
                word_dict[c] += 10**i
        digit_to_used = [False] * 10
        none_zero_c = set()  # type: Set[str]
        for num in words + [result]:
            none_zero_c.add(num[0])
        chars = list(set(list(res_dict.keys()) + list(word_dict.keys())))

        def dfs(i: int, curr_left: int, curr_right: int) -> bool:
            if i == len(chars):
                return curr_left == curr_right
            char = chars[i]
            for digit, used in enumerate(digit_to_used):
                if used or (digit == 0 and (char in none_zero_c)):
                    continue
                digit_to_used[digit] = True
                if dfs(
                        i + 1,
                        curr_left + digit * word_dict[char],
                        curr_right + digit * res_dict[char],
                ):
                    return True
                digit_to_used[digit] = False
            return False

        # print(chars, non_zero_c, word_dict, res_dict)
        return dfs(0, 0, 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSolvable(['asdf', 'gfsd'], 'asdf'))